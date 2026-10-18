import io
import json
import urllib.error
from types import TracebackType
from typing import Any, Self

import pytest

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
        self.urls: list[str] = []
        self.timeouts: list[float] = []

    def __call__(self, url: str, timeout: float) -> FakeResponse:
        self.urls.append(url)
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
