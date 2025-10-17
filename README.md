Aplikasi DISPENDA LAYANAN TERPADU ini akan memiliki fitur dasar:
- **Login sederhana** untuk pengguna (misalnya, admin atau petugas).
- **Dashboard** untuk melihat ringkasan pendapatan daerah.
- **Form untuk mengelola wajib pajak** (tambah, edit, hapus).
- **Form untuk mencatat pembayaran pajak** dan menghasilkan laporan sederhana.
- **Koordinasi sederhana** melalui halaman perencanaan (e.g., input target pendapatan).

### Persiapan
1. **Instalasi Dependensi:**
   - Pastikan Anda memiliki Python terinstal (versi 3.6+).
   - Instal Flask dan SQLite (umumnya sudah ada di Python, tapi jika tidak):
     ```
     pip install flask
     ```
   - Bootstrap akan di-include langsung di HTML, jadi tidak perlu instalasi tambahan.

2. **Cara Menjalankan Aplikasi:**
   - Simpan semua file di folder **dispenda_app**.
   - Buka terminal/cmd, navigasi ke folder **dispenda_app**, lalu jalankan:
     ```
     python app.py
     ```
   - Aplikasi akan berjalan di server lokal (http://127.0.0.1:5000/). Akses melalui browser di komputer yang sama.

### Kode Aplikasi
Berikut adalah kode lengkap untuk **app.py** (backend). Saya juga sertakan contoh file frontend di dalamnya (menggunakan template Flask).

#### File: app.py (Backend dengan Python Flask)
```python
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session
from flask import jsonify  # Untuk API sederhana jika diperlukan
import os



### Catatan Penting
- **Keamanan:** Password disimpan plain text di contoh ini. Di produksi, gunakan hashing (dengan library `werkzeug.security`).
- **Ekstensi:** Aplikasi ini sederhana; Anda bisa tambahkan fitur lanjutan seperti export laporan PDF atau integrasi email.
- **Offline Capability:** Karena menggunakan SQLite dan server lokal, aplikasi bisa dijalankan di komputer tanpa internet. Pastikan Bootstrap di-load dari CDN, tapi jika offline mutlak, unduh file Bootstrap dan simpan di folder **static/**.
- **Pengujian:** Setelah menjalankan **app.py**, buat user pertama melalui database secara manual (e.g., gunakan SQLite browser untuk insert ke tabel users).

Aplikasi ini siap digunakan! Jika Anda perlu modifikasi atau penambahan fitur, beri tahu saya. email : endrielhanan@gmail.com, satriaadhipradana2701@gmail.com

<img width="513" height="455" alt="00000" src="https://github.com/user-attachments/assets/1a2a1fcf-ba2b-4512-8665-0352a744a477" />

<img width="569" height="341" alt="0000" src="https://github.com/user-attachments/assets/28b507f5-82d0-4fce-bc78-056d0011c99e" />
