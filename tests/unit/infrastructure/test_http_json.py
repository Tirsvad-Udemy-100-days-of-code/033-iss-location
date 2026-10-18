import io
import json
import urllib.error
import urllib.request
from email.message import Message
from types import TracebackType
from typing import Any, Self

import pytest

from iss_notifier.constants import USER_AGENT
from iss_notifier.domain.errors import RemoteRequestError
from iss_notifier.infrastructure.http_json import fetch_json


class FakeResponse:
    def __init__(self, body: bytes) -> None:
        self._stream = io.BytesIO(body)
        self.closed = False

    def read(self) -> bytes:
        return self._stream.read()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        self.closed = True


class FakeOpener:
    def __init__(self, response: FakeResponse | Exception) -> None:
        self.response = response
        self.requests: list[urllib.request.Request] = []
        self.urls: list[str] = []
        self.timeouts: list[float] = []

    def __call__(self, request: urllib.request.Request, timeout: float) -> FakeResponse:
        self.requests.append(request)
        self.urls.append(request.full_url)
        self.timeouts.append(timeout)
        if isinstance(self.response, Exception):
            raise self.response
        return self.response


def _opener_for(payload: Any) -> FakeOpener:
    return FakeOpener(FakeResponse(json.dumps(payload).encode()))


def test_fetch_json_returns_the_decoded_object() -> None:
    assert fetch_json("http://x.test/a", opener=_opener_for({"a": 1})) == {"a": 1}


def test_fetch_json_adds_query_parameters_and_timeout() -> None:
    opener = _opener_for({})
    fetch_json("http://x.test/a", {"lat": "1.5", "lng": "2"}, 7, opener)
    assert opener.urls == ["http://x.test/a?lat=1.5&lng=2"]
    assert opener.timeouts == [7]


def test_fetch_json_sends_the_user_agent_header() -> None:
    opener = _opener_for({})
    fetch_json("http://x.test/a", opener=opener)
    assert opener.requests[0].get_header("User-agent") == USER_AGENT


def test_fetch_json_names_the_http_status_without_the_url() -> None:
    failure = urllib.error.HTTPError(
        "http://x.test/a?lat=1",
        403,
        "Forbidden",
        Message(),
        None,
    )
    with pytest.raises(RemoteRequestError) as info:
        fetch_json("http://x.test/a?lat=1", opener=FakeOpener(failure))
    assert str(info.value) == "request failed: HTTPError 403"
    assert "x.test" not in str(info.value)


def test_fetch_json_keeps_the_class_name_for_other_errors() -> None:
    with pytest.raises(RemoteRequestError) as info:
        fetch_json("http://x.test/a", opener=FakeOpener(TimeoutError("slow")))
    assert str(info.value) == "request failed: TimeoutError"


def test_fetch_json_closes_the_response() -> None:
    response = FakeResponse(b"{}")
    fetch_json("http://x.test/a", opener=FakeOpener(response))
    assert response.closed


@pytest.mark.parametrize(
    "failure",
    [urllib.error.URLError("no route"), TimeoutError("slow"), ConnectionResetError()],
)
def test_fetch_json_wraps_network_errors(failure: Exception) -> None:
    with pytest.raises(RemoteRequestError) as info:
        fetch_json("http://x.test/a?lat=1", opener=FakeOpener(failure))
    assert info.value.__cause__ is failure
    assert "lat=1" not in str(info.value)


def test_fetch_json_wraps_malformed_json() -> None:
    with pytest.raises(RemoteRequestError):
        fetch_json("http://x.test/a", opener=FakeOpener(FakeResponse(b"{not json")))


def test_fetch_json_rejects_a_non_object_document() -> None:
    with pytest.raises(RemoteRequestError, match="not a JSON object"):
        fetch_json("http://x.test/a", opener=_opener_for([1, 2]))
