# Penggunaan

🌐 [English](Usage) · [Dansk](Usage-da) · **Bahasa Melayu**

## 1. Konfigurasi

Program membaca tetapannya daripada fail `config.env` dalam folder tempat anda menjalankannya. Salin contoh dan sunting salinan itu. Windows (PowerShell):

```powershell
Copy-Item config.env.example config.env
```

Linux dan macOS:

```bash
cp config.env.example config.env
```

Gantikan setiap ruang letak dalam `config.env`. Fail itu diabaikan oleh git, jadi nilai anda tidak pernah dikomit. Gunakan kata laluan aplikasi daripada penyedia mel anda, bukan kata laluan biasa.

Pemboleh ubah yang turut ditetapkan dalam persekitaran sebenar mengatasi fail, dan `--config <laluan>` membaca fail lain. Jika anda tinggalkan kedua-dua `ISS_NOTIFIER_LATITUDE` dan `ISS_NOTIFIER_LONGITUDE`, program meneka kedudukan anda daripada alamat IP awam anda (lihat [Konfigurasi](Configuration-ms)). Semua tetapan disenaraikan di situ.

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
