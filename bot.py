import telebot
from PIL import Image
from urllib.request import urlopen
import os

from dictionary_for_files import storageKey   #словарь 
from Dicts import callback_data_keyboard, callback_data_keyboard1, callback_data_keyboard2, callback_data_keyboard3

token = os.environ.get('token')

#картинка
url = "https://sun9-40.userapi.com/impg/mG_WTIdgArErQb4YbU7CEIDz873dDvJoH0VW-w/arHUSXBmA5Y.jpg?size=527x505&quality=96&proxy=1&sign=3103cde7044a879a6d8e76a5b8ab2d62&type=album"

bot = telebot.TeleBot(token)


keyboard = telebot.types.InlineKeyboardMarkup().add(
        telebot.types.InlineKeyboardButton(bottom_titles[0],callback_data=callback_data_keyboard[bottom_titles[0]]),
        telebot.types.InlineKeyboardButton(bottom_titles[1],callback_data=callback_data_keyboard[bottom_titles[1]]))

keyboard1 = telebot.types.InlineKeyboardMarkup().add(
            telebot.types.InlineKeyboardButton(bottom_titles1[0],callback_data=callback_data_keyboard1[bottom_titles1[0]]),
            telebot.types.InlineKeyboardButton(bottom_titles1[1],callback_data=callback_data_keyboard1[bottom_titles1[1]]),
            telebot.types.InlineKeyboardButton(bottom_titles1[2],callback_data=callback_data_keyboard1[bottom_titles1[2]]))

keyboard2 = telebot.types.InlineKeyboardMarkup().add(
            telebot.types.InlineKeyboardButton(bottom_titles2[0],callback_data=callback_data_keyboard2[bottom_titles2[0]]),
            telebot.types.InlineKeyboardButton(bottom_titles2[1],callback_data=callback_data_keyboard2[bottom_titles2[1]]),
            telebot.types.InlineKeyboardButton(bottom_titles2[2],callback_data=callback_data_keyboard2[bottom_titles2[2]]),
            telebot.types.InlineKeyboardButton(bottom_titles2[3],callback_data=callback_data_keyboard2[bottom_titles2[3]]),
            telebot.types.InlineKeyboardButton(bottom_titles2[4],callback_data=callback_data_keyboard2[bottom_titles2[4]]))

keyboard3 = telebot.types.InlineKeyboardMarkup().add(
            telebot.types.InlineKeyboardButton(bottom_titles3[0],callback_data=callback_data_keyboard3[bottom_titles3[0]]),
            telebot.types.InlineKeyboardButton(bottom_titles3[1],callback_data=callback_data_keyboard3[bottom_titles3[1]]),
            telebot.types.InlineKeyboardButton(bottom_titles3[2],callback_data=callback_data_keyboard3[bottom_titles3[2]]),
            telebot.types.InlineKeyboardButton(bottom_titles3[3],callback_data=callback_data_keyboard3[bottom_titles3[3]]))

bottom_titles=[key for key in callback_data_keyboard]
bottom_titles1=[key for key in callback_data_keyboard1]
bottom_titles2=[key for key in callback_data_keyboard2]
bottom_titles3=[key for key in callback_data_keyboard3]

#Ключ или кнопки
@bot.message_handler(commands=['protocols'])
def callback_handler(message):    
    bot.send_message(message.chat.id, 'Выберите нужный вариант:', reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call1: call1.data==callback_query_handler)
    def query_handler(call1):
        query = update.callback_query
        data = query.data
        
        if call1.data == 'key':
            send = bot.edit_message_text(chat_id=call1.message.chat.id, message_id=call1.message.message_id, text='Введи слово')
            bot.register_next_step_handler(send,keys)
            #Переписывает предыдущее сообщение, кнопки пропадают, код переходит на функцию поиска по ключам,которая ниже
         
        elif call1.data == 'button':
            query.edit_message_text(text='Выберите нужный вариант', reply_markup=keyboard1)
            #Переписывает предыдущее сообщение и добавляет новую клавиатуру для выбора дальше по кнопкам
            
    @bot.callback_query_handler(func=lambda call2: call2.data==callback_query_handler1)
    def query_handler2(call2):
        query = update.callback_query
        data = query.data
        
        if call2.data == 'acid':
            query.edit_message_text('Выберите нужный вариант', reply_markup=keyboard2)
            #Переписывает предыдущее сообщение и добавляет новую клавиатуру для выбора дальше по кнопкам
                  
        elif call2.data == 'PCR':
            query.edit_message_text('Выберите нужный вариант', reply_markup=keyboard3) 
            #Переписывает предыдущее сообщение и добавляет новую клавиатуру для выбора дальше по кнопкам     
                
                
def keys(message):
    dickt = storageKey 
    found_links=[]
    for i in dickt:
        if message.text.lower() in i:
            found_links.append(storageKey[i])
    if len(found_links) <= 0:
        send_me = bot.send_message(message.from_user.id,
                                 'Совпадений не найдено. Попробуйте ввести другое слово, например: ДНК \n Или нажмите /protocols, чтобы начать поиск')
        bot.register_next_step_handler(send_me, keys)
        return
    send_me = bot.send_message(message.from_user.id, "\n\n".join(found_links) + '\n\n\U0001F50E Чтобы начать новый поиск, нажмите /protocols')

bot.polling(True)
