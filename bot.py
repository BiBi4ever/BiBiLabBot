import telebot
from PIL import Image
from urllib.request import urlopen
import os

from dictionary_for_files import storageKey   #словарь 
from Dicts import keyboard, keyboard1, keyboard2, keyboard3, callback_query_handler, callback_query_handler1, callback_query_handler2

token = os.environ.get('token')

#картинка
url = "https://sun9-40.userapi.com/impg/mG_WTIdgArErQb4YbU7CEIDz873dDvJoH0VW-w/arHUSXBmA5Y.jpg?size=527x505&quality=96&proxy=1&sign=3103cde7044a879a6d8e76a5b8ab2d62&type=album"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
         bot.send_message(message, f'Bonjour, {message.from_user.first_name}!\U0001F44B\nЯ бот, облегчающий работу в лаборатории. \n\nУ меня есть база протоколов, которые могут пригодиться в твоих исследованиях. \n\nЧтобы начать поиск протокола, нажми /protocols.\n\nЧтобы увидеть список доступных действий, нажми /help.')
                               
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, ' С моей помощью ты можешь увидеть протоколы для '
                                      'работы с нуклеиновыми кислотами, обратной транскрипции и '
                                      'ПЦР.\n\n' 
                     'Чтобы найти нужный протокол, нажми /protocols. Выбирай поиск с кнопками или воспользуйся поиском по ключу и введи ключевое слово.')
    
#Ключ или кнопки
@bot.message_handler(commands=['protocols'])
def callback_handler(message):    
    bot.send_message(message.chat.id, 'Можешь выбрать нужный вариант', reply_markup=keyboard)
    
    @bot.callback_query_handler(func=lambda call1: call1.data in [value for value in callback_query_handler.values()])
    def query_handler(call1):
        if call1.data == 'key':
            send = bot.edit_message_text(chat_id=call1.message.chat.id, message_id=call1.message.message_id, text='Введи слово')
            bot.register_next_step_handler(send,keys)
            #Переписывает предыдущее сообщение, кнопки пропадают, код переходит на функцию поиска по ключам,которая ниже
        elif call1.data == 'button':
            bot.edit_message_text(chat_id=call1.message.chat.id, message_id=call1.message.message_id, text='Можешь выбрать нужный вариант', reply_markup=keyboard1)
            #Переписывает предыдущее сообщение и добавляет новую клавиатуру для выбора дальше по кнопкам
            
    @bot.callback_query_handler(func=lambda call2: call2.data in [value for value in callback_query_handler1.values()])
    def query_handler1(call2):
        if call2.data == 'acid':
            bot.edit_message_text(chat_id=call2.message.chat.id, message_id=call2.message.message_id, text='Можешь выбрать нужный вариант', reply_markup=keyboard2)
            #Переписывает предыдущее сообщение и добавляет новую клавиатуру для выбора дальше по кнопкам
                  
        elif call2.data == 'PCR':
            bot.edit_message_text(chat_id=call2.message.chat.id, message_id=call2.message.message_id, text='Можешь выбрать нужный вариант', reply_markup=keyboard3) 
            #Переписывает предыдущее сообщение и добавляет новую клавиатуру для выбора дальше по кнопкам 
    
        elif call2.data == 'back':
            bot.edit_message_text(chat_id=call2.message.chat.id, message_id=call2.message.message_id, text='Можешь выбрать нужный вариант', reply_markup=keyboard)
        
    @bot.callback_query_handler(func=lambda call3: call3.data in [value for value in callback_query_handler2.values()] )
    def query_handler2(call3):
        if call3.data == 'back1':
            bot.edit_message_text(chat_id=call3.message.chat.id, message_id=call3.message.message_id, text='Можешь выбрать нужный вариант', reply_markup=keyboard1)
        elif call3.data == 'back2':
            bot.edit_message_text(chat_id=call3.message.chat.id, message_id=call3.message.message_id, text='Можешь выбрать нужный вариант', reply_markup=keyboard1)

#Ответ на приветствие
@bot.message_handler(content_types=['text'])
def send_first_message(message):
    greet = ['hello','hi','привет', 'здравствуй']
    if any(greetings in message.text.lower() for greetings in greet):
        bot.send_message(message.from_user.id, 'Рад тебя видеть! Я скучал')               
#бот кидает мемосную картиночку, если пользователь вводит неправильный запрос
    else:
        img = Image.open(urlopen(url))
        bot.send_photo(message.chat.id, img)
        img.close()
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит. Если тебе нужна помощь, нажми /help')
         
         
def keys(message):
    dickt = storageKey 
    found_links=[]
    for i in dickt:
        if message.text.lower() in i:
            found_links.append(storageKey[i])
    if len(found_links) <= 0:
        send_me = bot.send_message(message.from_user.id,
                                 'Совпадений не найдено. Попробуй ввести другое слово, например: ДНК \n Или нажми /protocols, чтобы начать поиск')
        bot.register_next_step_handler(send_me, keys)
        return
    send_me = bot.send_message(message.from_user.id, "\n\n".join(found_links) + '\n\n Чтобы начать новый поиск, нажми /protocols')
    
bot.polling(True)
