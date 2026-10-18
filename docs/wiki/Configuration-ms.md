# Konfigurasi

🌐 [English](Configuration) · [Dansk](Configuration-da) · **Bahasa Melayu**

## Fail `config.env`

Tetapan ialah baris `NAMA=nilai` dalam `config.env`, dalam folder tempat anda menjalankan program. Baris yang bermula dengan `#` dan baris kosong diabaikan; awalan `export ` dan tanda petikan di sekeliling nilai dibenarkan. Mulakan daripada `config.env.example`:

```text
ISS_NOTIFIER_LATITUDE=<your latitude>
ISS_NOTIFIER_LONGITUDE=<your longitude>
ISS_NOTIFIER_SMTP_HOST=smtp.example.com
ISS_NOTIFIER_SMTP_PORT=587
ISS_NOTIFIER_SMTP_USER=<your login>
ISS_NOTIFIER_SMTP_PASSWORD=<your app password>
ISS_NOTIFIER_MAIL_TO=<recipient address>
```

Pemboleh ubah yang ditetapkan dalam persekitaran sebenar mengatasi fail; `--config <laluan>` membaca fail lain. `config.env` yang tiada tidak mengapa apabila persekitaran memegang tetapan; fail yang tiada yang dinamakan dengan `--config` menghentikan program.

## Tetapan

| Pemboleh ubah | Wajib | Maksud |
| --- | --- | --- |
| `ISS_NOTIFIER_LATITUDE` | bersama longitud | Latitud anda dalam darjah, -90 hingga 90 |
| `ISS_NOTIFIER_LONGITUDE` | bersama latitud | Longitud anda dalam darjah, -180 hingga 180 |
| `ISS_NOTIFIER_SMTP_HOST` | ya | Nama hos pelayan SMTP anda |
| `ISS_NOTIFIER_SMTP_PORT` | tidak | Port SMTP, lalai 587 (STARTTLS) |
| `ISS_NOTIFIER_SMTP_USER` | ya | Log masuk untuk pelayan SMTP |
| `ISS_NOTIFIER_SMTP_PASSWORD` | ya | Kata laluan atau kata laluan aplikasi |
| `ISS_NOTIFIER_MAIL_TO` | ya | Alamat yang menerima e-mel |

Pemboleh ubah yang tiada menghentikan program dengan mesej yang menyebut nama pemboleh ubah, tidak pernah nilainya. Program hanya membaca `config.env`; ia tidak pernah membaca fail bernama `.env`.

## Teka kedudukan

Jika kedua-dua `ISS_NOTIFIER_LATITUDE` dan `ISS_NOTIFIER_LONGITUDE` ditinggalkan, program bertanya `get.geojs.io` di mana alamat IP awam anda berada dan menggunakan kedudukan itu. Ini menghantar alamat IP awam anda kepada perkhidmatan pihak ketiga itu, ia hanya tepat hingga peringkat bandar (cukup untuk margin 5 darjah) dan log menyatakan kedudukan itu diteka tanpa mencetaknya. Menetapkan kedua-dua pemboleh ubah mematikan tekaan. Menetapkan satu sahaja ialah ralat.

## Pemalar

Nilai tetap (dua alamat API, sela semakan 60 saat, margin 5 darjah, had masa dan teks e-mel) ditakrifkan sekali di `src/iss_notifier/constants.py`.
