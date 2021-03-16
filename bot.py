import telebot
from PIL import Image
from urllib.request import urlopen
import os

from dictionary_for_files import storageKey   #словарь 

token = os.environ.get('token')

#картинка
url = "https://sun9-40.userapi.com/impg/mG_WTIdgArErQb4YbU7CEIDz873dDvJoH0VW-w/arHUSXBmA5Y.jpg?size=527x505&quality=96&proxy=1&sign=3103cde7044a879a6d8e76a5b8ab2d62&type=album"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
         bot.reply_to(message, f'Hello you, {message.from_user.first_name}!\U0001F44B\nЯ бот, облегчающий работу в лаборатории. Чтобы начать поиск протокола, нажми /protocols.\n\nЧтобы увидеть список доступных действий, нажми /help.')
                               #ПРОШУ ОСТАВИТЬ ПРИВЕТСВИЕ, ЧТОБЫ НЕ БЫЛО СЛИШКОМ СУХО 
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, ' С моей помощью ты можешь увидеть протоколы для '
                                      'работы с нуклеиновыми кислотами, обратной транскрипции и '
                                      'ПЦР.\n\n' 
                     'Чтобы найти нужный протокол, нажми /protocols. Выбирай поиск с кнопками или воспользуйся поиском по ключу - введи ключевое слово.'
)
# Команда для работы с протоколами, если пользователь выбирает поиск по ключу (вызов key), он вводит слова для протокола сам, если выбирает кнопку (вызов button) - тыкает на варианты
@bot.message_handler(commands=['protocols'])
def exchange_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Поиск по ключу', callback_data='key'),
        telebot.types.InlineKeyboardButton('Поиск с кнопками',callback_data='button'))
    bot.send_message(message.chat.id, 'Выберите нужный вариант:', reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call1: call1.data in ['key', 'button'] )
    def query_handler(call1):
        if call1.data == 'key':
            # поиск по ключу, см. функцию ниже:
            bot.send_messege(chat_id=call1.message.chat.id, text='Введи ключевое слово')
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
            bot.edit_message_reply_markup(call2.message.chat.id, call2.message.message_id)
                  
        elif call2.data == 'PCR':
            keyboard2 = telebot.types.InlineKeyboardMarkup(row_width=2)
            keyboard2.add(
                telebot.types.InlineKeyboardButton('Обычная ПЦР', url='https://s.tcdn.co/ec5/c1b/ec5c1b75-12ea-45bd-aa7b-33491089b8e5/1.png'),
                telebot.types.InlineKeyboardButton('Реал тайм ПЦР с зондами', url='https://s.tcdn.co/ec5/c1b/ec5c1b75-12ea-45bd-aa7b-33491089b8e5/8.png'),
                telebot.types.InlineKeyboardButton('Реал тайм ПЦР на sybr green', url='https://s.tcdn.co/ec5/c1b/ec5c1b75-12ea-45bd-aa7b-33491089b8e5/11.png'))
            bot.send_message(call2.message.chat.id, 'Выберите нужный вариант:', reply_markup=keyboard2) 
bot.polling(True)
