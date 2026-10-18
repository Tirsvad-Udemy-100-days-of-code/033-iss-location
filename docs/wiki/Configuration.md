# Configuration

🌐 **English** · [Dansk](Configuration-da) · [Bahasa Melayu](Configuration-ms)

## The `config.env` file

The settings are `NAME=value` lines in `config.env`, in the folder where you run the program. Lines starting with `#` and blank lines are ignored, an `export ` prefix and quotes around a value are allowed. Start from `config.env.example`:

```text
ISS_NOTIFIER_LATITUDE=<your latitude>
ISS_NOTIFIER_LONGITUDE=<your longitude>
ISS_NOTIFIER_SMTP_HOST=smtp.example.com
ISS_NOTIFIER_SMTP_PORT=587
ISS_NOTIFIER_SMTP_USER=<your login>
ISS_NOTIFIER_SMTP_PASSWORD=<your app password>
ISS_NOTIFIER_MAIL_TO=<recipient address>
```

A variable set in the real environment overrides the file; `--config <path>` reads another file. A missing `config.env` is fine when the environment holds the settings, a missing file named with `--config` stops the program.

## Settings

| Variable | Required | Meaning |
| --- | --- | --- |
| `ISS_NOTIFIER_LATITUDE` | with the longitude | Your latitude in degrees, -90 to 90 |
| `ISS_NOTIFIER_LONGITUDE` | with the latitude | Your longitude in degrees, -180 to 180 |
| `ISS_NOTIFIER_SMTP_HOST` | yes | Host name of your SMTP server |
| `ISS_NOTIFIER_SMTP_PORT` | no | SMTP port, default 587 (STARTTLS) |
| `ISS_NOTIFIER_SMTP_USER` | yes | Login for the SMTP server |
| `ISS_NOTIFIER_SMTP_PASSWORD` | yes | Password or app password |
| `ISS_NOTIFIER_MAIL_TO` | yes | Address that receives the e-mail |

A missing variable stops the program with a message that names the variable, never its value. The program reads `config.env` only; it never reads a file named `.env`.

## Position guess

If both `ISS_NOTIFIER_LATITUDE` and `ISS_NOTIFIER_LONGITUDE` are left out, the program asks `get.geojs.io` where your public IP address is and uses that position. This sends your public IP address to that third-party service, it is only accurate to the city (enough for the 5-degree margin) and the log says the position was guessed without printing it. Setting both variables turns the guess off. Setting only one of them is an error.

## Constants

Fixed values (the two API addresses, the 60-second check interval, the 5-degree margin, timeouts and the e-mail text) are defined once in `src/iss_notifier/constants.py`.
