"""@brief Reader of KEY=value configuration files such as config.env."""

from pathlib import Path

from iss_notifier.domain.errors import ConfigError

## @brief Prefix a line may carry so that the file can also be sourced by a shell.
_EXPORT_PREFIX = "export "

## @brief Quote characters that may surround a whole value.
_QUOTES = ("'", '"')


## @brief Remove one pair of matching quotes around a value.
#
# @param value Text after the equals sign, already stripped.
# @return The value without the surrounding quotes.
def _unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in _QUOTES:
        return value[1:-1]
    return value


## @brief Parse one non-blank, non-comment line.
#
# @param line The stripped line.
# @param number Its 1-based line number, used in errors.
# @return The key and value.
# @throws ConfigError when there is no equals sign or the key is invalid.
def _parse_line(line: str, number: int) -> tuple[str, str]:
    if line.startswith(_EXPORT_PREFIX):
        line = line[len(_EXPORT_PREFIX) :]
    key, separator, value = line.partition("=")
    key = key.strip()
    if not separator or not key.isidentifier():
        raise ConfigError(f"malformed line {number} in configuration file")
    return key, _unquote(value.strip())


## @brief Read a KEY=value file.
#
# Blank lines and lines starting with # are skipped. A # inside a value is kept.
#
# @param path The file to read.
# @return Mapping of keys to values; a later line overrides an earlier one.
# @throws ConfigError when the file cannot be read or a line is malformed. The
#     message names the file path or the line number, never a value.
def read_env_file(path: Path) -> dict[str, str]:
    """Read a KEY=value file."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as error:
        raise ConfigError(f"cannot read configuration file {path}") from error
    values: dict[str, str] = {}
    for number, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        key, value = _parse_line(line, number)
        values[key] = value
    return values
