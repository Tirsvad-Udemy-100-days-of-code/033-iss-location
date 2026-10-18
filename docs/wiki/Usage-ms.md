# Penggunaan

🌐 [English](Usage) · [Dansk](Usage-da) · **Bahasa Melayu**

## 1. Konfigurasi

Program membaca tetapannya daripada pemboleh ubah persekitaran, tidak pernah daripada fail. Tetapkannya dalam terminal tempat anda menjalankan program. Windows (PowerShell):

```powershell
$env:ISS_NOTIFIER_LATITUDE = "<your latitude>"
$env:ISS_NOTIFIER_LONGITUDE = "<your longitude>"
$env:ISS_NOTIFIER_SMTP_HOST = "smtp.example.com"
$env:ISS_NOTIFIER_SMTP_USER = "<your login>"
$env:ISS_NOTIFIER_SMTP_PASSWORD = "<your app password>"
$env:ISS_NOTIFIER_MAIL_TO = "<recipient address>"
```

Linux dan macOS:

```bash
export ISS_NOTIFIER_LATITUDE="<your latitude>"
export ISS_NOTIFIER_LONGITUDE="<your longitude>"
export ISS_NOTIFIER_SMTP_HOST="smtp.example.com"
export ISS_NOTIFIER_SMTP_USER="<your login>"
export ISS_NOTIFIER_SMTP_PASSWORD="<your app password>"
export ISS_NOTIFIER_MAIL_TO="<recipient address>"
```

Gunakan kata laluan aplikasi daripada penyedia mel anda, bukan kata laluan biasa. Semua tetapan disenaraikan di halaman [Konfigurasi](Configuration-ms).

## 2. Jalankan

Dengan `.venv` aktif:

```bash
python -m iss_notifier
```

![ISS Overhead Notifier running](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/raw/branch/main/docs/images/notifier-run.png)

Tekan Ctrl+C untuk berhenti. Panggilan rangkaian yang gagal dicatat dan gelung diteruskan dengan semakan seterusnya. Log tidak pernah mengandungi koordinat, alamat atau kata laluan anda.

## Apa yang diputuskan

- `is_iss_overhead` benar apabila ISS berada dalam lingkungan tambah/tolak 5 darjah daripada latitud dan longitud anda (longitud berpusing pada 180 darjah).
- `is_night` benar sebelum matahari terbit dan dari matahari terbenam, menggunakan jam UTC.
- Kedua-dua fungsi mengekalkan nama tugasan, supaya anda boleh membandingkan penyelesaian anda:

```python
from iss_notifier import is_iss_overhead, is_night
```
