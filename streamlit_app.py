import base64
import json
import time
import telebot
import requests
import datetime
import openpyxl
import pandas as pd
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from streamlit_cookies_manager import EncryptedCookieManager
from http.cookies import SimpleCookie

import openpyxl
wb = openpyxl.Workbook()
ws = wb.active

# modul telegram untuk mengecek id
api_telegram_bot = '6215631300:AAH0rPZsMxTT_fnEva2sjGeVqugTdQwk_t8'
bot = telebot.TeleBot(api_telegram_bot)
@bot.message_handler(commands=['ping'])
def greet(message):
    print(message.chat.id)
    bot.reply_to(message, f"Hey! , Thankyou for try your verification\nYour code is :\n{message.chat.id}")

@bot.message_handler(commands=['cerita'])
def greet(message):
    print(message.chat.id)
    f = open('cerita_global.txt','r', encoding="utf-8")
    data_export_tele = f.read()
    bot.send_message(message.chat.id,f'NGL GENRE...\n{data_export_tele}')

chat_id = -4029218509

kirim_tele = True

st.set_page_config(
    page_title='GENRE KOTA MAGELANG',
    page_icon='logo.png',
    layout='wide',  
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': 'https://www.extremelycoolapp.com/bug',
         'About': '# This is a header. This is an *extremely* cool app!'
    }
)

with st.sidebar:

    st.image('logo.png',width=95)
    selected = option_menu('Menu', ['Dasboard','Curhat Kuy','Curhatku','Chat live','Setting'], icons=['house','book','list','chat','gear'], menu_icon="cast", default_index=0)

if selected == 'Dasboard':

    hide_streamlit_style = """
                <style>
                    #MainMenu {visibility: hidden;}
                    #stToolbar {visibility: hidden;}
                    #viewerBadge_container__r5tak styles_viewerBadge__CvC9N {visibility: hidden;}
                    footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    st.markdown(
        """
        <style>
        .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
        .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
        .viewerBadge_text__1JaDK {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)
    with col2:
        st.image('logo.png',width=300)
    
    st.header('Curhat via website :')
    st.write('-Hallo Genrengers')
    st.write('-Kamu bisa curhat sebanyak seaman dan senyaman mungkin di sini lho gaess, gimana caranya?.')
    st.write('-Langsung aja klik (>) di atas kiri lalu pilih bagian (Curhat kuy).')
    st.write('-Ketika kamu sudah masuk ke halaman (Curhat kuy) kamu langsung bisa isi form curhatmu.')
    st.write('-Seberapa aman sih NGL genre ini? , Jika kamu tidak nyaman memberi tahu nama kalian kalian cukup mengosongkan bagian nama itu karena optional (boleh iya maupun tidak).')
    st.write('-cara privacy nama dan cerita')
    st.write('- Jika namamu tidak ingin di ketahui siapapun , mohon tidak mengisi kolom nama')
    st.write('- Jika cerita dan namamu hanya untuk genre , mohon checklist (Hanya admin GENRE yang bisa melihat.).')
    st.header('')
    
    st.header('Konseling via instagram & wa :')
    st.write('- Kamu bisa curhat sebanyak seaman dan senyaman mungkin di sini lho gaess, gimana caranya?')
    st.write('- Langsung aja klik (>) di atas kiri lalu pilih bagian (Chat Live)')
    st.write('- Okei di situlah kamu bisa memilih ingin kontak genre atau konseling langsung dari whatsapp maupun instagram.')

    for i in range(5):
        st.write('')

    col1, col2, col3 = st.columns(3)
    with col1:
        pass
    with col2:
        st.write('© COPYRIGHT 2023 - GENERASI BERENCANA.')
        st.write('ALL RIGHTS RESERVED. WEBSITE DESIGN BY.')
        st.link_button('GENRE MGL','https://www.instagram.com/genrekotamagelang/')
        pass
    with col3:
        pass

if selected == 'Curhat Kuy':

    hide_streamlit_style = """
                <style>
                    #MainMenu {visibility: hidden;}
                    #stToolbar {visibility: hidden;}
                    #viewerBadge_container__r5tak styles_viewerBadge__CvC9N {visibility: hidden;}
                    footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    col1, col2, col3 = st.columns(3)
    with col2:
        st.image('logo.png',width=300)

    nama   = st.text_input('Name (optional) :','')
    age = st.slider('How old are you?', 0, 100, 17)
    st.write("I'm ", age, 'years old')  
    curhat = st.text_area('TULISKAN CERITA HATIMU HARI INI...')

    publick = st.checkbox('Hanya admin GENRE yang bisa melihat.')

    if st.button('Submit'):

        if nama or curhat != str():

            a = open(f'history.json')
            data = json.load(a)
            x = curhat
            y = 'skip...'
            if x in data:
                #print(f'[+] chek : [{x}] | {data[x]}')
                st.warning('[+] Pesan mu sudah terkirim , silahkan chek pada CURHATKU')
            else:
                data[x] = y
                #print(f'[+] chek : [{x}] | save..')
                b = open(f'history.json', 'w')
                json.dump(data,b)
                b.close()

                current_time = datetime.datetime.now()
                now = current_time.strftime('%H:%M:%S')
                date = current_time.strftime('%d/%m/%Y')

                if publick:

                    st.warning('[+] Pesanmu sudah terkirim , Hanya admin GENRE yang bisa melihat.')
                    # write database normal
                    f = open('cerita_global.txt','a')
                    f.write(f'\nName : {nama}|age : {age}|post date : {now} {date}|Hidden : True\n{curhat}')
                    f.close()

                    # sending master database
                    f = open('cerita_global.txt','r', encoding="utf-8")
                    data_export_tele = f.read()
                    for i in range(kirim_tele):
                        bot = telebot.TeleBot(api_telegram_bot)
                        bot.send_message(chat_id,f'NGL GENRE...\n{data_export_tele}')

                else:

                    st.warning('[+] Chek pesanmu pada page Curhatku pada taskbar')
                    # write database normal
                    f = open('cerita_publick.txt','a')
                    f.write(f'\nName : {nama}|age : {age} {date}\n{curhat}')
                    f.close()

                    # write database normal
                    f = open('cerita_global.txt','a')
                    f.write(f'\nName : {nama}|age : {age}|post date : {now} {date}|Hidden : False\n{curhat}')
                    f.close()

                    # sending master database
                    f = open('cerita_global.txt','r', encoding="utf-8")
                    data_export_tele = f.read()
                    for i in range(kirim_tele):
                        bot = telebot.TeleBot(api_telegram_bot)
                        bot.send_message(chat_id,f'NGL GENRE...\n{data_export_tele}')

            
        else:
            st.warning('[+] kamu tidak membuat pesan')
            
            time.sleep(2)

    for i in range(5):
        st.write('')

    col1, col2, col3 = st.columns(3)
    with col1:
        pass
    with col2:
        st.write('© COPYRIGHT 2023 - GENERASI BERENCANA.')
        st.write('ALL RIGHTS RESERVED. WEBSITE DESIGN BY.')
        st.link_button('GENRE MGL','https://www.instagram.com/genrekotamagelang/')
        pass
    with col3:
        pass

if selected == 'Curhatku':

    hide_streamlit_style = """
                <style>
                    #MainMenu {visibility: hidden;}
                    #stToolbar {visibility: hidden;}
                    #viewerBadge_container__r5tak styles_viewerBadge__CvC9N {visibility: hidden;}
                    footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    col1, col2, col3 = st.columns(3)
    with col1:
        pass
    with col2:
        st.image('logo.png',width=300)
        pass
    with col3:
        pass

    # reading database
    database = open('cerita_publick.txt', 'r', encoding="utf-8")
    count = 0
    # Using for loop
    for data in database:
        count += 1
        text = (str(data.strip()))
        ganjil_genap = ('genap' if (count % 2 == 0) else 'ganjil')
        if ganjil_genap == 'ganjil':
            col1,col2= st.columns(2)
            with col1:
                st.success(text, icon="ℹ")
            with col2:
                pass

        if ganjil_genap == 'genap':
            st.info(text, icon="ℹ")
            st.warning('|'+'-'*60+'|')
        st.caption('')

    for i in range(5):
        st.write('')

    col1, col2, col3 = st.columns(3)
    with col1:
        pass
    with col2:
        st.write('© COPYRIGHT 2023 - GENERASI BERENCANA.')
        st.write('ALL RIGHTS RESERVED. WEBSITE DESIGN BY.')
        st.link_button('GENRE MGL','https://www.instagram.com/genrekotamagelang/')
        pass
    with col3:
        pass

if selected == 'Chat live':

    hide_streamlit_style = """
                <style>
                    #MainMenu {visibility: hidden;}
                    #stToolbar {visibility: hidden;}
                    #viewerBadge_container__r5tak styles_viewerBadge__CvC9N {visibility: hidden;}
                    footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    st.header('Hallo sobat GENRE INDOENSIA')
    st.write('Temen-temen pernah gak sih mau cerita tapi gak tau harus cerita ke mana, karena tidak ada tempat bercerita yang aman dan nyaman :( ')
    st.write('Kami genre kota magelang menyediakan tempat pelayanan dengan basis konseling sebaya atau curhat secara aman nyaman baik public maupun private😃.')
    st.write('Loh kak bagaimana caranya? , teman-teman langsung bisa chat secara private dengan cara click kolom di bawah ini 😊.')

    col1, col2, col3, col4, col5, col6, col7, col8, col9= st.columns(9)
    with col1:
        st.write('')
        st.link_button('whatsapp 💬','https://wa.me/6282331970107?text=hallo%20genre%20kota%20magelang%20:)')
    with col2:
        st.write('')
        st.link_button('Instagram 💬','https://www.instagram.com/genrekotamagelang/')
    #with col3:
        #st.link_button('Twitter 💬','https://twitter.com/genre_indonesia')

    # chat auto balas
    #prompt = st.chat_input("Say something")
    #if prompt:
    #    st.write(f"ROMEO : {prompt}")

    for i in range(5):
        st.write('')

    col1, col2, col3 = st.columns(3)
    with col1:
        pass
    with col2:
        st.write('© COPYRIGHT 2023 - GENERASI BERENCANA.')
        st.write('ALL RIGHTS RESERVED. WEBSITE DESIGN BY.')
        st.link_button('GENRE MGL','https://www.instagram.com/genrekotamagelang/')
        pass
    with col3:
        pass

if selected == 'Setting':

    import streamlit as st
    import sqlite3
    import hashlib

    # Fungsi untuk membuat koneksi database
    def create_connection():
        conn = sqlite3.connect('data.db')
        return conn

    # Fungsi untuk membuat tabel pengguna
    def create_user_table():
        conn = create_connection()
        conn.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE,
                            password TEXT
                        );''')
        conn.commit()
        conn.close()

    # Fungsi untuk menampilkan halaman logout
    def show_logout_page():
        st.subheader(f"Selamat datang, {st.session_state['username']}")

        ###
        '''
        Nanti kamu masukin data di sini
        '''
        ###

        if st.button("Keluar"):
            del st.session_state['username']
            st.success("Anda telah keluar.")

    def login_or_signup(cache):
        menu = ["Login","SignUp"]
        choice = st.sidebar.selectbox("Menu",menu)

        if choice == "Login":
            import login as lg
            lg.show_login_page(st,cache)
        elif choice == "SignUp":
            import signup as su
            su.show_registration_page(st)

    # Fungsi utama untuk mengatur tampilan halaman
    def main():

        """Simple Login App"""

        # Function to get IP Address
        def get_ip():
            try:
                ip = requests.get('https://api.ipify.org').text
                return ip
            except:
                return "IP not found"

        # Function to get approximate geolocation based on IP
        def get_geolocation(ip):
            try:
                response = requests.get(f"https://ipapi.co/{ip}/json/")
                location_data = response.json()
                return f"{location_data.get('city', 'Unknown City')}, {location_data.get('region', 'Unknown Region')}, {location_data.get('country_name', 'Unknown Country')}"
            except:
                return "Location not found"

        # Function to get timezone information
        def get_timezone():
            try:
                timezone = time.strftime('%Z', time.gmtime())
                return timezone
            except:
                return "Timezone not found"

        # Function to set a cookie
        def set_cookie(cookie_name, cookie_value):
            st.experimental_set_query_params(cookie=f"{cookie_name}={cookie_value}")

        # Function to get a cookie
        def get_cookie(cookie_name):
            cookie_header = st.query_params.get("cookie", [""])[0]
            cookie = SimpleCookie(cookie_header)
            return cookie.get(cookie_name)

        # Basic Authentication
        def authenticate():
            st.title("Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            
            if username == "admin" and password == "password":
                st.session_state.authenticated = True
                set_cookie("auth_token", "valid_token")
            else:
                st.session_state.authenticated = False

        # Inject JavaScript to get screen resolution and language preferences
        js_code = """
        <script>
            const getData = () => {
                const screenResolution = `${window.screen.width}x${window.screen.height}`;
                const language = navigator.language || navigator.userLanguage;
                const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
                return {
                    screenResolution: screenResolution,
                    language: language,
                    timezone: timezone,
                };
            };
            const data = getData();
            fetch(`${window.location.origin}/_stcore/get_js_data`, {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify(data),
            });
        </script>
        """

        st.components.v1.html(js_code, height=0)

        # Function to handle the JS data sent to the server
        def handle_js_data(js_data):
            js_data_dict = json.loads(js_data)
            st.session_state['screen_resolution'] = js_data_dict.get('screenResolution', 'Resolution not found')
            st.session_state['language'] = js_data_dict.get('language', 'Language not found')
            st.session_state['timezone_js'] = js_data_dict.get('timezone', 'Timezone not found')

        # Access the query parameters directly
        query_params = st.query_params
        if 'json_data' in query_params:
            js_data = query_params['json_data'][0]
            handle_js_data(js_data)

        # Collect all data
        user_agent = query_params.get('user_agent', ['Unknown'])[0]  # Replace with actual user agent retrieval
        ip_address = get_ip()
        geolocation = get_geolocation(ip_address)
        timezone_py = get_timezone()
        screen_resolution = st.session_state.get('screen_resolution', 'Resolution not found')
        language = st.session_state.get('language', 'Language not found')
        timezone_js = st.session_state.get('timezone_js', 'Timezone not found')

        # Combine all data into a single token string
        token = f"User-Agent: {user_agent}, IP: {ip_address}, Geolocation: {geolocation}, Timezone (Python): {timezone_py}, Timezone (JS): {timezone_js}, Screen Resolution: {screen_resolution}, Language: {language}"

        a = open(f'history.json')
        data = json.load(a)
        x = token
        y = 'True|0'

        if x in data:
            print(f'[+] DATA KOKIS : {x}')
            chek_login = (f'{data[x]}')
            if chek_login == 'True':
                import show_database as sd
                sd.sd(st,ws,wb,pd,token)
            if chek_login == 'False':
                login_or_signup(token)
        else:
            login_or_signup(token)

    if __name__ == '__main__':
        main()
