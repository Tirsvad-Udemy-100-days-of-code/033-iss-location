import smtplib
import ssl
from email.message import EmailMessage
from types import TracebackType
from typing import Self

import pytest

from iss_notifier.domain.errors import NotificationError
from iss_notifier.domain.models import GeoPosition
from iss_notifier.infrastructure.config import Settings
from iss_notifier.infrastructure.smtp_notifier import SmtpNotifier

SETTINGS = Settings(
    home=GeoPosition(1.0, 2.0),
    smtp_host="smtp.example.test",
    smtp_port=2525,
    smtp_user="me@example.test",
    smtp_password="s3cret-value",
    mail_to="you@example.test",
)


class FakeSmtp:
    instances: list["FakeSmtp"] = []
    fail_on: str | None = None

    def __init__(self, host: str, port: int, timeout: float) -> None:
        self.host = host
        self.port = port
        self.calls: list[str] = []
        self.messages: list[EmailMessage] = []
        self.login_args: tuple[str, str] | None = None
        self.closed = False
        FakeSmtp.instances.append(self)

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        self.closed = True

    def _step(self, name: str) -> None:
        self.calls.append(name)
        if FakeSmtp.fail_on == name:
            raise smtplib.SMTPAuthenticationError(535, b"bad credentials")

    def starttls(self, *, context: ssl.SSLContext | None = None) -> object:
        self._step("starttls")
        assert context is not None
        return None

    def login(self, user: str, password: str) -> object:
        self._step("login")
        self.login_args = (user, password)
        return None

    def send_message(self, msg: EmailMessage) -> object:
        self._step("send_message")
        self.messages.append(msg)
        return None


@pytest.fixture(autouse=True)
def reset_fake() -> None:
    FakeSmtp.instances = []
    FakeSmtp.fail_on = None


def test_send_uses_starttls_login_and_sends_one_message() -> None:
    SmtpNotifier(SETTINGS, FakeSmtp).send("Hello", "Body text")
    (smtp,) = FakeSmtp.instances
    assert (smtp.host, smtp.port) == ("smtp.example.test", 2525)
    assert smtp.calls == ["starttls", "login", "send_message"]
    assert smtp.login_args == ("me@example.test", "s3cret-value")
    assert smtp.closed
    (message,) = smtp.messages
    assert message["To"] == "you@example.test"
    assert message["From"] == "me@example.test"
    assert message["Subject"] == "Hello"
    assert message.get_content().strip() == "Body text"


def test_send_wraps_smtp_errors_without_the_server_reply() -> None:
    FakeSmtp.fail_on = "login"
    with pytest.raises(NotificationError) as info:
        SmtpNotifier(SETTINGS, FakeSmtp).send("s", "b")
    assert isinstance(info.value.__cause__, smtplib.SMTPException)
    assert "bad credentials" not in str(info.value)
    assert FakeSmtp.instances[0].closed


def test_send_wraps_connection_errors() -> None:
    def refuse(host: str, port: int, timeout: float) -> FakeSmtp:
        raise ConnectionRefusedError

    with pytest.raises(NotificationError):
        SmtpNotifier(SETTINGS, refuse).send("s", "b")
