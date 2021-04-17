import telebot
from PIL import Image
from urllib.request import urlopen
import os
import ast
import json
from googleapiclient.http import MediaIoBaseDownload,MediaFileUpload
import io
from google_drive import authorization
from Dicts import keyboard_for_buttons, keyboard_for_buttons1, keyboard_for_buttons2, keyboard_for_buttons3, callback_query_handler, callback_query_handler1, callback_query_handler2, callback_data_keyboard_Acid, callback_data_keyboard_PCR


#картинка
url = "https://sun9-40.userapi.com/impg/mG_WTIdgArErQb4YbU7CEIDz873dDvJoH0VW-w/arHUSXBmA5Y.jpg?size=527x505&quality=96&proxy=1&sign=3103cde7044a879a6d8e76a5b8ab2d62&type=album"

token = os.environ.get('token')
ID = json.loads(os.environ.get('key'))
service = authorization(ID) 
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
         bot.send_message(message.chat.id, f'Bonjour, {message.from_user.first_name}!\U0001F44B\n\nЯ бот, облегчающий работу в лаборатории. \n\nУ меня есть база протоколов, которые могут пригодиться в твоих исследованиях. \n\nЧтобы начать поиск протокола, нажми /protocols.\n\nЧтобы увидеть список доступных действий, нажми /help.')  

                  
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'С моей помощью ты можешь увидеть протоколы для работы с нуклеиновыми кислотами(НК), обратной транскрипции и ПЦР.\n\n' 
                     'Чтобы найти нужный протокол, нажми /protocols и выбери поиск с кнопками или поиск по ключевому слову')
    
#Ключ или кнопки
@bot.message_handler(commands=['protocols'])
def callback_handler(message):    
    bot.send_message(message.chat.id, 'Можешь выбрать нужный вариант', reply_markup=keyboard_for_buttons)
    
    @bot.callback_query_handler(func=lambda call1: call1.data in [value for value in callback_query_handler.values()])
    def query_handler(call1):
        if call1.data == 'key':
            send = bot.edit_message_text(chat_id=call1.message.chat.id, message_id=call1.message.message_id, text='Не вводи /protocols, /help или /start. Я не смогу обработать эти запросы, пока идет поиск по ключу. \n\nВведи слово:')
            bot.register_next_step_handler(send, keys)
            #Переписывает предыдущее сообщение, кнопки пропадают, код переходит на функцию поиска по ключам,которая ниже
        elif call1.data == 'button':
            bot.edit_message_text(chat_id=call1.message.chat.id, message_id=call1.message.message_id, text='Можешь выбрать нужный вариант', reply_markup=keyboard_for_buttons1)
            bot.answer_callback_query(call1.id)
            #Переписывает предыдущее сообщение и добавляет новую клавиатуру для выбора дальше по кнопкам
            
    @bot.callback_query_handler(func=lambda call2: call2.data in [value for value in callback_query_handler1.values()])
    def query_handler1(call2):
        if call2.data == 'acid':
            bot.edit_message_text(chat_id=call2.message.chat.id, message_id=call2.message.message_id, text='Можешь выбрать нужный вариант', reply_markup=keyboard_for_buttons2)
            
                  
        elif call2.data == 'PCR':
            bot.edit_message_text(chat_id=call2.message.chat.id, message_id=call2.message.message_id, text='Можешь выбрать нужный вариант', reply_markup=keyboard_for_buttons3) 
            
    
        elif call2.data == 'back':
            bot.edit_message_text(chat_id=call2.message.chat.id, message_id=call2.message.message_id, text='Можешь выбрать нужный вариант', reply_markup=keyboard_for_buttons)
            bot.answer_callback_query(call2.id)
                  
    @bot.callback_query_handler(func=lambda call3: call3.data in [value for value in callback_query_handler2.values()] )
    def query_handler2(call3):
        if call3.data == 'back1':
            bot.edit_message_text(chat_id=call3.message.chat.id, message_id=call3.message.message_id, text='Можешь выбрать нужный вариант', reply_markup=keyboard_for_buttons1)
            bot.answer_callback_query(call3.id)
                        

#Ответ на приветствие
@bot.message_handler(content_types=['text'])
def send_first_message(message):
    greet = ['hello','hi','привет', 'здравствуй']
    if any(greetings in message.text.lower() for greetings in greet):
        bot.send_message(message.chat.id, 'Рад тебя видеть! Я скучал')
#бот кидает мемосную картиночку, если пользователь вводит неправильный запрос
    else:
        img = Image.open(urlopen(url))
        bot.send_photo(message.chat.id, img)
        img.close()
        bot.send_message(message.chat.id, 'Не понимаю, что это значит. Если тебе нужна помощь, нажми /help')
       
def download_and_send (name, id, message_chat_id):
         filename = name
         request = service.files().get_media(fileId=id)
         fh = io.FileIO(filename, 'wb')
         downloader = MediaIoBaseDownload(fh, request)
         done = False
         while done is False:
                  status, done = downloader.next_chunk()
         with open(filename, 'rb') as f:
              bot.send_document(message_chat_id, f)
              f.close()
         

def keys(message):
         
         results = service.files().list(fields="files(name, id)", q =("name contains '%s'" % message.text.lower()) ).execute()
        
         if  results.get('files'):
                  for file in results.get('files'):
                           download_and_send(file.get('name'), file.get('id'), message_chat_id=message.chat.id)
                  bot.send_message(message.from_user.id, '\n\n Если хочешь начать новый поиск, нажми /protocols')
         else:
                  bot.send_message(message.from_user.id,'Совпадений не найдено. Нажми поиск по ключу и попробуй ввести другое слово', reply_markup=keyboard_for_buttons)
    
bot.polling(none_stop=True)
