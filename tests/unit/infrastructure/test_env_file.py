from pathlib import Path

import pytest

from iss_notifier.domain.errors import ConfigError
from iss_notifier.infrastructure.env_file import read_env_file


def _read(tmp_path: Path, text: str) -> dict[str, str]:
    path = tmp_path / "config.env"
    path.write_text(text, encoding="utf-8")
    return read_env_file(path)


def test_read_env_file_reads_key_value_lines(tmp_path: Path) -> None:
    assert _read(tmp_path, "A=1\nB = two \n") == {"A": "1", "B": "two"}


def test_read_env_file_skips_comments_and_blank_lines(tmp_path: Path) -> None:
    text = "# comment\n\n   \n  # indented comment\nA=1\n"
    assert _read(tmp_path, text) == {"A": "1"}


def test_read_env_file_accepts_the_export_prefix(tmp_path: Path) -> None:
    assert _read(tmp_path, "export A=1\n") == {"A": "1"}


def test_read_env_file_strips_single_and_double_quotes(tmp_path: Path) -> None:
    text = 'A=\'one two\'\nB="three"\nC=""\n'
    assert _read(tmp_path, text) == {"A": "one two", "B": "three", "C": ""}


def test_read_env_file_keeps_unbalanced_quotes(tmp_path: Path) -> None:
    assert _read(tmp_path, "A='open\nB=\"x'\n") == {"A": "'open", "B": "\"x'"}


def test_read_env_file_keeps_a_hash_inside_a_value(tmp_path: Path) -> None:
    assert _read(tmp_path, "A=pa#ss # word\n") == {"A": "pa#ss # word"}


def test_read_env_file_keeps_an_equals_sign_inside_a_value(tmp_path: Path) -> None:
    assert _read(tmp_path, "A=x=y==\n") == {"A": "x=y=="}


def test_read_env_file_lets_a_later_line_win(tmp_path: Path) -> None:
    assert _read(tmp_path, "A=1\nA=2\n") == {"A": "2"}


def test_read_env_file_returns_nothing_for_an_empty_file(tmp_path: Path) -> None:
    assert _read(tmp_path, "") == {}


def test_read_env_file_handles_windows_line_endings(tmp_path: Path) -> None:
    path = tmp_path / "config.env"
    path.write_bytes(b"A=1\r\nB=2\r\n")
    assert read_env_file(path) == {"A": "1", "B": "2"}


@pytest.mark.parametrize("line", ["no-equals-secret", "=value-secret", " =x-secret"])
def test_read_env_file_names_only_the_line_number_of_a_malformed_line(
    tmp_path: Path, line: str
) -> None:
    with pytest.raises(ConfigError) as info:
        _read(tmp_path, f"A=1\n# note\n{line}\n")
    assert "3" in str(info.value)
    assert "secret" not in str(info.value)


def test_read_env_file_rejects_an_invalid_key(tmp_path: Path) -> None:
    with pytest.raises(ConfigError, match="line 1"):
        _read(tmp_path, "bad key=1\n")


def test_read_env_file_names_the_path_of_a_missing_file(tmp_path: Path) -> None:
    path = tmp_path / "missing.env"
    with pytest.raises(ConfigError) as info:
        read_env_file(path)
    assert str(path) in str(info.value)
    assert isinstance(info.value.__cause__, OSError)


def test_read_env_file_reports_an_undecodable_file(tmp_path: Path) -> None:
    path = tmp_path / "config.env"
    path.write_bytes(b"A=\xff\xfe\n")
    with pytest.raises(ConfigError, match="cannot read"):
        read_env_file(path)
