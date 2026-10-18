# Configuration

🌐 **English** · [Dansk](Configuration-da) · [Bahasa Melayu](Configuration-ms)

## Environment variables

| Variable | Required | Meaning |
| --- | --- | --- |
| `ISS_NOTIFIER_LATITUDE` | yes | Your latitude in degrees, -90 to 90 |
| `ISS_NOTIFIER_LONGITUDE` | yes | Your longitude in degrees, -180 to 180 |
| `ISS_NOTIFIER_SMTP_HOST` | yes | Host name of your SMTP server |
| `ISS_NOTIFIER_SMTP_PORT` | no | SMTP port, default 587 (STARTTLS) |
| `ISS_NOTIFIER_SMTP_USER` | yes | Login for the SMTP server |
| `ISS_NOTIFIER_SMTP_PASSWORD` | yes | Password or app password |
| `ISS_NOTIFIER_MAIL_TO` | yes | Address that receives the e-mail |

A missing variable stops the program with a message that names the variable, never its value. The program does not load a `.env` file.

## Constants

Fixed values (the two API addresses, the 60-second check interval, the 5-degree margin, timeouts and the e-mail text) are defined once in `src/iss_notifier/constants.py`.
