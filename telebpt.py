import telebot

import base64
import json
import time
import telebot
import datetime
import openpyxl
import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_autorefresh import st_autorefresh
from streamlit_extras.switch_page_button import switch_page

# modul telegram untuk mengecek id
api_telegram_bot = '6215631300:AAH0rPZsMxTT_fnEva2sjGeVqugTdQwk_t8'
bot = telebot.TeleBot(api_telegram_bot)

chat_id = -4029218509
#bot.send_message(chat_id,f"Bot telegram for genre is ready or nhoting problem for now :)")

@bot.message_handler(commands=['ping'])
def greet(message):
    print(message.chat.id)
    bot.reply_to(message, f"Hey! , Thankyou for try your verification\nYour code is :\n{message.chat.id}")

#bot.send_message(1366551188,f"Bot telegram for genre is ready or nhoting problem for now :)")
@bot.message_handler(commands=['p'])
def welcome(pm):
    f = open('polling.txt','w')
    f.write('False')
    f.close()
    #print(pm.chat.id)
    keluh_kesah_user = bot.send_message(pm.chat.id, "Hallo sahabat genre , ada apa?")
    bot.register_next_step_handler(keluh_kesah_user, admin_bales1) #Next message will call the name_handler function

def admin_bales1(pm):
    keluh_kesah_user = pm.text
    
    st.write(keluh_kesah_user)
    admin_bales = st.chat_input("Say something")
    st.write(admin_bales)

    sent_msg = bot.send_message(pm.chat.id, f"{admin_bales}")
    bot.register_next_step_handler(sent_msg, admin_bales2) #Next message will call the age_handler function

def admin_bales2(pm):
    keluh_kesah_user = pm.text

    st.write(keluh_kesah_user)
    admin_bales = st.chat_input("Say something")
    st.write(admin_bales)

    sent_msg = bot.send_message(pm.chat.id, f"{admin_bales}")
    bot.register_next_step_handler(sent_msg, admin_bales1) #Next message will call the age_handler function

f = open('polling.txt','r')
f = f.read()
if f == True:
    bot.polling()

#bot.polling()