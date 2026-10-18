"""@brief Notifier that sends e-mail over SMTP with STARTTLS."""

import smtplib
import ssl
from collections.abc import Callable
from contextlib import AbstractContextManager
from email.message import EmailMessage
from typing import Protocol

from iss_notifier.constants import SMTP_TIMEOUT_SECONDS
from iss_notifier.domain.errors import NotificationError
from iss_notifier.infrastructure.config import Settings


## @brief The part of an SMTP connection the notifier uses.
class SmtpSession(Protocol):
    """The part of an SMTP connection the notifier uses."""

    ## @brief Upgrade the connection to TLS.
    #
    # @param context TLS settings.
    # @return The server reply.
    def starttls(self, *, context: ssl.SSLContext | None = None) -> object:
        """Upgrade the connection to TLS."""
        ...

    ## @brief Authenticate.
    #
    # @param user Account name.
    # @param password Account password.
    # @return The server reply.
    def login(self, user: str, password: str) -> object:
        """Authenticate."""
        ...

    ## @brief Send a message.
    #
    # @param msg Message to send.
    # @return The server reply.
    def send_message(self, msg: EmailMessage) -> object:
        """Send a message."""
        ...


## @brief Sends the notification as an e-mail.
class SmtpNotifier:
    """Sends the notification as an e-mail."""

    ## @brief Create the notifier.
    #
    # @param settings Server, account and recipient.
    # @param smtp_factory Creates an SMTP connection; replaced in tests.
    def __init__(
        self,
        settings: Settings,
        smtp_factory: Callable[..., AbstractContextManager[SmtpSession]] = smtplib.SMTP,
    ) -> None:
        """Create the notifier."""
        ## @brief Server, account and recipient.
        self._settings = settings
        ## @brief Creates an SMTP connection.
        self._smtp_factory = smtp_factory

    ## @brief Send one e-mail.
    #
    # @param subject Subject line.
    # @param body Message text.
    # @return Nothing.
    # @throws NotificationError when the connection, login or sending fails.
    def send(self, subject: str, body: str) -> None:
        """Send one e-mail."""
        message = EmailMessage()
        message["From"] = self._settings.smtp_user
        message["To"] = self._settings.mail_to
        message["Subject"] = subject
        message.set_content(body)
        try:
            with self._smtp_factory(
                self._settings.smtp_host,
                self._settings.smtp_port,
                timeout=SMTP_TIMEOUT_SECONDS,
            ) as smtp:
                smtp.starttls(context=ssl.create_default_context())
                smtp.login(self._settings.smtp_user, self._settings.smtp_password)
                smtp.send_message(message)
        except OSError as error:
            # smtplib.SMTPException is an OSError; its text could echo the account.
            raise NotificationError(
                f"sending the e-mail failed: {type(error).__name__}"
            ) from error
