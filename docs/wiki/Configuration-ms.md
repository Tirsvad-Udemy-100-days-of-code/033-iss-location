# Konfigurasi

🌐 [English](Configuration) · [Dansk](Configuration-da) · **Bahasa Melayu**

## Pemboleh ubah persekitaran

| Pemboleh ubah | Wajib | Maksud |
| --- | --- | --- |
| `ISS_NOTIFIER_LATITUDE` | ya | Latitud anda dalam darjah, -90 hingga 90 |
| `ISS_NOTIFIER_LONGITUDE` | ya | Longitud anda dalam darjah, -180 hingga 180 |
| `ISS_NOTIFIER_SMTP_HOST` | ya | Nama hos pelayan SMTP anda |
| `ISS_NOTIFIER_SMTP_PORT` | tidak | Port SMTP, lalai 587 (STARTTLS) |
| `ISS_NOTIFIER_SMTP_USER` | ya | Log masuk untuk pelayan SMTP |
| `ISS_NOTIFIER_SMTP_PASSWORD` | ya | Kata laluan atau kata laluan aplikasi |
| `ISS_NOTIFIER_MAIL_TO` | ya | Alamat yang menerima e-mel |

Pemboleh ubah yang tiada menghentikan program dengan mesej yang menyebut nama pemboleh ubah, tidak pernah nilainya. Program tidak memuatkan fail `.env`.

## Pemalar

Nilai tetap (dua alamat API, sela semakan 60 saat, margin 5 darjah, had masa dan teks e-mel) ditakrifkan sekali di `src/iss_notifier/constants.py`.
