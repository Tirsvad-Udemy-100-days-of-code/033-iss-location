# ISS Overhead Notifier

🌐 [English](Home) · [Dansk](Home-da) · **Bahasa Melayu**

Menghantar e-mel kepada anda apabila Stesen Angkasa Antarabangsa (ISS) berada di atas anda selepas gelap. Ini ialah tugasan hari ke-33 dalam "100 Days of Code: The Complete Python Pro Bootcamp" Udemy, ditulis dalam Python 3.13 tanpa kebergantungan masa jalan.

![ISS Overhead Notifier running](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/raw/branch/main/docs/images/notifier-run.png)

_Tangkapan skrin menunjukkan program sebenar berjalan dengan respons API yang dirakam dan tetapan ruang letak._

| Halaman | Baca apabila anda mahu |
| --- | --- |
| [Pemasangan](Install-ms) | Mencipta `.venv` setempat dan memasang projek |
| [Penggunaan](Usage-ms) | Menetapkan program, menjalankannya dan memahami apa yang dilakukannya |
| [Konfigurasi](Configuration-ms) | Mencari setiap tetapan |
| [Ujian](Testing-ms) | Menjalankan ujian, semakan kualiti dan dokumentasi sumber |

## Cara ia berfungsi

1. Setiap 60 saat program bertanya API kedudukan ISS di mana stesen itu berada.
2. Ia bertanya API matahari terbit-terbenam bila matahari terbit dan terbenam di kedudukan anda.
3. Jika ISS berada dalam lingkungan 5 darjah daripada latitud dan longitud anda dan ketika itu malam, ia menghantar e-mel kepada anda.

Repositori ada [di sini](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location).
