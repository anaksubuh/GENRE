import telebot
import os

API_KEY = ('6215631300:AAH0rPZsMxTT_fnEva2sjGeVqugTdQwk_t8')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['ping'])
def greet(message):
    print(message.chat.id)
    bot.reply_to(message, f"Hey! , Thankyou for try your verification\nYour code is :\n{message.chat.id}")


bot.polling()