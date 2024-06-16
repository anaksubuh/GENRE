import hashlib
import sqlite3
import json

def create_connection():
    conn = sqlite3.connect('data.db')
    return conn

# Fungsi untuk memeriksa kredensial pengguna
def login_user(username, password):
    conn = create_connection()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, hashed_password))
    user = cursor.fetchone()
    conn.close()
    return user

# Fungsi untuk menampilkan halaman login
def show_login_page(st,cache):
    st.subheader("Masuk")
    username = st.text_input("Nama Pengguna")
    password = st.text_input("Kata Sandi", type='password')

    if st.button("Masuk"):
        user = login_user(username, password)
        if user:
            st.session_state['username'] = username
            st.success(f"Selamat datang, {username}!")

            # save cache login
            a = open(f'history.json')
            data = json.load(a)
            x = cache
            y = 'True'
            data[x] = y
            b = open(f'history.json', 'w')
            json.dump(data,b)
            b.close()

            import openpyxl
            wb = openpyxl.Workbook()
            ws = wb.active
            import pandas as pd

            import show_database as sd
            sd.sd(st,ws,wb,pd,cache)

        else:
            st.error("Nama pengguna atau kata sandi salah.")