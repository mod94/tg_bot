#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmpp
from jaber_bot import JabberBot
from message_text import *
from comand_parser import *
import os

config = { #имя пользователя и пароль для подключения
'jid': 'job-rdp-shop@xmpp.jp',
'pass': 'M0de$t201809@'
}
def message_handler(conn, mess): #вызывается при входящем сообщении,
	text = mess.getBody() #получаем текст сообщения, отправителя
	user = mess.getFrom() #получаем  отправителя
	reply = start_menu(user,text) #парсим текст на наличие команд
	conn.send(xmpp.Message(mess.getFrom(), reply)) # отправляем

bot = JabberBot(config['jid'], config['pass'])#создаем экземпляр бота
bot.register_handler('message', message_handler)#создаем поток приема сообщений
bot.start()#запускаем