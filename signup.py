import sqlite3
import hashlib

def create_connection():
    conn = sqlite3.connect('data.db')
    return conn

# Fungsi untuk memeriksa apakah username sudah terdaftar
def is_username_taken(username):
    conn = create_connection()
    cursor = conn.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user is not None

# Fungsi untuk menampilkan halaman registrasi
def show_registration_page(st):
    st.subheader("Registrasi Pengguna Baru")
    new_user = st.text_input("Nama Pengguna")
    new_password = st.text_input("Kata Sandi", type='password')
    kode_otp = st.text_input("OTP")

    if st.button("Daftar"):
        if kode_otp != 2801:
            st.warning('Anda tidak mendapatkan izin regrsit oleh admin , mohon hubungi admin...', icon="⚠️")
        else:
            if not new_user or not new_password:
                st.error("Nama pengguna dan kata sandi tidak boleh kosong.")
            elif is_username_taken(new_user):
                st.error("Nama pengguna sudah ada. Silakan pilih nama pengguna yang lain.")
            else:
                add_user(new_user, new_password)
                st.success("Akun berhasil dibuat. Silakan masuk.")


# Fungsi untuk menambahkan pengguna baru
def add_user(username, password):
    conn = create_connection()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
    conn.commit()
    conn.close()
