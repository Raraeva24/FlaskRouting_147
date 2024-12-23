# Mengimpor modul-modul yang diperlukan dari Flask
from flask import Flask, redirect, url_for, request, render_template  # render_template digunakan untuk merender file HTML

# Membuat instance aplikasi Flask
app = Flask(__name__)

# Rute untuk halaman utama (home)
@app.route('/')  # Rute ini akan menangani permintaan ke root ('/')
def home():
    # Menampilkan file index.html yang ada di folder templates
    return render_template('index.html')  # Flask akan mencari index.html di folder templates

# Rute untuk halaman sukses setelah login
@app.route('/success/<name>')  # Menggunakan parameter <name> yang akan diterima dari URL
def success(name):
    # Menampilkan pesan selamat datang dengan nama pengguna yang diambil dari URL
    return f'Welcome {name}!'  # Menggunakan f-string untuk menyisipkan nama ke dalam string

# Rute untuk halaman login
@app.route('/login', methods=['POST', 'GET'])  # Rute ini menangani metode POST dan GET
def login():
    # Jika request menggunakan metode POST (setelah mengirimkan form)
    if request.method == 'POST':
        # Mengambil nama pengguna yang dimasukkan ke dalam form
        user = request.form['nm']  # 'nm' adalah nama input dalam form HTML
        # Setelah login, mengarahkan pengguna ke halaman success dengan nama yang dimasukkan
        return redirect(url_for('success', name=user))  # Mengarahkan ke halaman 'success' dengan nama pengguna
    else:
        # Jika request menggunakan metode GET (misalnya saat pertama kali membuka halaman login)
        # Mengarahkan kembali ke halaman utama (home)
        return redirect(url_for('home'))  # Mengarahkan ke halaman utama jika metode GET

# Menjalankan aplikasi Flask jika file ini dijalankan langsung
if __name__ == '__main__':
    app.run(debug=True)  # Menjalankan aplikasi Flask dengan mode debug aktif (untuk pengembangan)
