import telebot
from telebot import apihelper
from comand_parser import *

apihelper.proxy = {'https': 'socks5://127.0.0.1:9050'}
token = 'token'

@bot.message_handler(commands=['start'])#
def start_message(message):
    bot.send_message(message.chat.id, 'Используй !помошь для просмотра команд')

@bot.message_handler(content_types=['text'])
def send_text(message):
    user = message.chat.id
    text = message.text.lower()
    reply = start_menu(user,text)#парсим на наличие команд
    bot.send_message(message.chat.id, reply)#отправляем ответ

bot = telebot.TeleBot(token)#создаем экземпляр бота
bot.polling()#запуск бота
