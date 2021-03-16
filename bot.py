import telebot
from PIL import Image
from urllib.request import urlopen
import os

from dictionary_for_files import storageKey   #словарь 

import telebot
from PIL import Image
import os

token = os.environ.get('token')

#картинка
url = "https://sun9-40.userapi.com/impg/mG_WTIdgArErQb4YbU7CEIDz873dDvJoH0VW-w/arHUSXBmA5Y.jpg?size=527x505&quality=96&proxy=1&sign=3103cde7044a879a6d8e76a5b8ab2d62&type=album"

bot = telebot.TeleBot(token)


# Команда для работы с протоколами, если пользователь выбирает поиск по ключу (вызов key), он вводит слова для протокола сам, если выбирает кнопку (вызов button) - тыкает на варианты
@bot.message_handler(commands=['protocols'])
def exchange_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup().row(
        telebot.types.InlineKeyboardButton('Поиск по ключу', callback_data='key'),
        telebot.types.InlineKeyboardButton('Поиск с кнопками',callback_data='button'))
    bot.send_message(message.chat.id, 'Выберите нужный вариант:', reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call1: call1.data in ['key', 'button'] )
    def query_handler(call1):
        if call1.data == 'key':
            send = bot.edit_message_text(chat_id=call1.message.chat.id, text='Введи ключевое слово')
            bot.register_next_step_handler(send,keys)
         
        elif call1.data == 'button':
            keyboard1 = telebot.types.InlineKeyboardMarkup()
            keyboard1.row(
                telebot.types.InlineKeyboardButton('Работа с нуклеиновыми кислотами', callback_data='acid'),
                telebot.types.InlineKeyboardButton('Работа с ПЦР', callback_data='PCR'))
            bot.send_message(call1.message.chat.id, 'Выберите нужный вариант:', reply_markup=keyboard1)
            
    @bot.callback_query_handler(func=lambda call2: call2.data in ['acid', 'PCR'] )
    def query_handler2(call2):
        if call2.data == 'acid':
            keyboard2 = telebot.types.InlineKeyboardMarkup(row_width=2)
            keyboard2.add(
                    telebot.types.InlineKeyboardButton('Выделение ДНК по Хомчински', url='https://drive.google.com/file/d/1DmogZzc5-vEgDxxqiCB4sC3wHOb9KYHc/view?usp=sharing'),
                    telebot.types.InlineKeyboardButton('Выделение ДНК на магнитах', url='https://drive.google.com/file/d/1C_TYw363bHUPfdFXumlmeqA1TEDP3YEd/view?usp=sharing'),
                    telebot.types.InlineKeyboardButton('Выделение РНК ', url='https://drive.google.com/file/d/1mzLZRFX3hDsQpm18QD_op8mg89E29Z-P/view'),
                    telebot.types.InlineKeyboardButton('Обратная транскрипция', url='https://drive.google.com/file/d/1uZr7I87Ow6VqzTTBqg_0OzuriqUm-Ip-/view'))
            bot.send_message(call2.message.chat.id, 'Выберите нужный вариант:', reply_markup=keyboard2)
                  
        elif call2.data == 'PCR':
            keyboard2 = telebot.types.InlineKeyboardMarkup(row_width=2)
            keyboard2.add(
                telebot.types.InlineKeyboardButton('Обычная ПЦР', url='https://s.tcdn.co/ec5/c1b/ec5c1b75-12ea-45bd-aa7b-33491089b8e5/1.png'),
                telebot.types.InlineKeyboardButton('Реал тайм ПЦР с зондами', url='https://s.tcdn.co/ec5/c1b/ec5c1b75-12ea-45bd-aa7b-33491089b8e5/8.png'),
                telebot.types.InlineKeyboardButton('Реал тайм ПЦР на sybr green', url='https://s.tcdn.co/ec5/c1b/ec5c1b75-12ea-45bd-aa7b-33491089b8e5/11.png'))
            bot.send_message(call2.message.chat.id, 'Выберите нужный вариант:', reply_markup=keyboard2) 
                 
def keys(message):
    list = [storageKey]
    found_links = []
    for i in list:
        if message.text.lower() in i:
            found_links.append(storageKey[i])
    if len(found_links) > 0:
        bot.send_message(message.from_user.id, "\n\n".join(found_links) + '\n\n\U0001F50E Чтобы начать новый поиск, нажми /protocols')
    else:
        send_me = bot.send_message(message.from_user.id,
                                 'Совпадений не найдено. Попробуй ввести другое слово, например: ДНК')
        bot.register_next_step_handler(send_me, keys)
        return
bot.polling(True)
