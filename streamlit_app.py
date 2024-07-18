import base64
import json
import time
import telebot
import datetime
import openpyxl
import pandas as pd
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page

import openpyxl
wb = openpyxl.Workbook()
ws = wb.active

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

# Fungsi untuk menyembunyikan elemen tertentu menggunakan CSS
def hide_streamlit_elements():
    hide_elements = """
        <style>
        /* Sembunyikan tombol perbesar gambar */
        [title="View fullscreen"] {
            display: none;
        }
        /* Sembunyikan simbol link pada header */
        .stMarkdown .css-10trblm a {
            display: none;
        }
        </style>
    """
    st.markdown(hide_elements, unsafe_allow_html=True)

# Fungsi untuk menampilkan gambar tanpa tombol perbesar
def display_image(image_path, width=None):
    img = Image.open(image_path)
    st.image(img, use_column_width=(width is None), width=width)

# Fungsi untuk menampilkan header tanpa simbol link
def display_header(header_text):
    st.markdown(f"<h1 style='display: inline-block;'>{header_text}</h1>", unsafe_allow_html=True)

# Memanggil fungsi untuk menyembunyikan elemen
hide_streamlit_elements()

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

with st.sidebar:
    display_image('logo.png', width=95)
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
        display_image('logo.png', width=300)
    
    display_header('Curhat via website :')
    st.write('-Hallo Genrengers')
    st.write('-Kamu bisa curhat sebanyak seaman dan senyaman mungkin di sini lho gaess, gimana caranya?.')
    st.write('-Langsung aja klik (>) di atas kiri lalu pilih bagian (Curhat kuy).')
    st.write('-Ketika kamu sudah masuk ke halaman (Curhat kuy) kamu langsung bisa isi form curhatmu.')
    st.write('-Seberapa aman sih NGL genre ini? , Jika kamu tidak nyaman memberi tahu nama kalian kalian cukup mengosongkan bagian nama itu karena optional (boleh iya maupun tidak).')
    st.write('-cara privacy nama dan cerita')
    st.write('- Jika namamu tidak ingin di ketahui siapapun , mohon tidak mengisi kolom nama')
    st.write('- Jika cerita dan namamu hanya untuk genre , mohon checklist (Hanya admin GENRE yang bisa melihat.).')
    st.header('')
    
    display_header('Konseling via instagram & wa :')
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
        display_image('logo.png', width=300)

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
    with col2:
        display_image('logo.png', width=300)

    st.write('![Foo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTznmKnFZt18pGNNGzRurUSVV1R4JZZf1Cz8g&usqp=CAU)')

    a = open(f'history.json')
    data = json.load(a)

    f = open('cerita_publick.txt','r', encoding="utf-8")
    genre_mgl = f.read().split('\n')
    for i in genre_mgl:
        st.write(i)

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

    col1, col2, col3 = st.columns(3)
    with col2:
        display_image('logo.png', width=300)

    st.subheader('Hello genrengers')

    st.write('hubungi kami via whatsapp')

    st.write('[![Foo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTznmKnFZt18pGNNGzRurUSVV1R4JZZf1Cz8g&usqp=CAU)](https://wa.me/+6285925728687)')

    st.write('[![Foo](https://cdn-icons-png.flaticon.com/512/174/174855.png)](https://www.instagram.com/genrekotamagelang/)')

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
        display_image('logo.png', width=300)

    st.write('h')
