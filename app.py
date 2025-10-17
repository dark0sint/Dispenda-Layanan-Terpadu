import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session
from flask import jsonify  # Untuk API sederhana jika diperlukan
import os

app = Flask(__name__)
app.secret_key = 'rahasia_dispenda'  # Untuk session login

# Konfigurasi database SQLite
DATABASE = 'database.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row  # Untuk mengakses kolom seperti dictionary
    return db

# Inisialisasi database (buat tabel jika belum ada)
def init_db():
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL  -- Gunakan hashing di produksi
            )
        ''')
        db.execute('''
            CREATE TABLE IF NOT EXISTS wajib_pajak (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama TEXT NOT NULL,
                alamat TEXT,
                jumlah_pajak REAL,
                status_pembayaran TEXT  -- e.g., 'Lunas' atau 'Belum'
            )
        ''')
        db.execute('''
            CREATE TABLE IF NOT EXISTS pendapatan (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tanggal TEXT,
                jumlah REAL,
                keterangan TEXT
            )
        ''')
        db.commit()

init_db()  # Jalankan inisialisasi saat aplikasi dimulai

# Route untuk halaman login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        user = db.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        if user:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Login gagal')
    return render_template('login.html')

# Route untuk logout
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

# Route untuk dashboard (ringkasan pendapatan)
@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    db = get_db()
    pendapatan = db.execute('SELECT SUM(jumlah) as total FROM pendapatan').fetchone()
    return render_template('dashboard.html', total_pendapatan=pendapatan['total'] or 0)

# Route untuk mengelola wajib pajak (CRUD sederhana)
@app.route('/wajib_pajak', methods=['GET', 'POST'])
def wajib_pajak():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    db = get_db()
    if request.method == 'POST':
        nama = request.form['nama']
        alamat = request.form['alamat']
        jumlah_pajak = request.form['jumlah_pajak']
        status = request.form['status']
        db.execute('INSERT INTO wajib_pajak (nama, alamat, jumlah_pajak, status_pembayaran) VALUES (?, ?, ?, ?)',
                   (nama, alamat, jumlah_pajak, status))
        db.commit()
        return redirect(url_for('wajib_pajak'))
    data = db.execute('SELECT * FROM wajib_pajak').fetchall()
    return render_template('wajib_pajak.html', data=data)

# Route untuk mencatat pembayaran (bagian pemungutan pendapatan)
@app.route('/catat_pembayaran', methods=['GET', 'POST'])
def catat_pembayaran():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    db = get_db()
    if request.method == 'POST':
        tanggal = request.form['tanggal']
        jumlah = request.form['jumlah']
        keterangan = request.form['keterangan']
        db.execute('INSERT INTO pendapatan (tanggal, jumlah, keterangan) VALUES (?, ?, ?)',
                   (tanggal, jumlah, keterangan))
        db.commit()
        return redirect(url_for('catat_pembayaran'))
    return render_template('catat_pembayaran.html')

# Route utama (home atau redirect ke login)
@app.route('/')
def index():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)  # Jalankan di localhost:5000
