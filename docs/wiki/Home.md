# ISS Overhead Notifier

🌐 **English** · [Dansk](Home-da) · [Bahasa Melayu](Home-ms)

Sends you an e-mail when the International Space Station (ISS) is above you after dark. It is the day 33 assignment of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp", written in Python 3.13 with no runtime dependencies.

![ISS Overhead Notifier running](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/raw/branch/main/docs/images/notifier-run.png)

_The screenshot shows the real program running against recorded API responses and placeholder settings._

| Page | Read it when you want to |
| --- | --- |
| [Install](Install) | Create the local `.venv` and install the project |
| [Usage](Usage) | Configure the program, run it and understand what it does |
| [Configuration](Configuration) | Look up every setting |
| [Testing](Testing) | Run the tests, the quality checks and the source documentation |

## How it works

1. Every 60 seconds the program asks the ISS position API where the station is.
2. It asks the sunrise-sunset API when the sun rises and sets at your position.
3. If the ISS is within 5 degrees of your latitude and longitude and it is night, it sends you an e-mail.

The repository is [here](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location).
