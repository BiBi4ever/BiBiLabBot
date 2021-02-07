import telebot
from PIL import Image
from urllib.request import urlopen
import os

token = os.environ.get('TOKEN')

#картинка
url = "https://sun9-40.userapi.com/impg/mG_WTIdgArErQb4YbU7CEIDz873dDvJoH0VW-w/arHUSXBmA5Y.jpg?size=527x505&quality=96&proxy=1&sign=3103cde7044a879a6d8e76a5b8ab2d62&type=album"

bot = telebot.TeleBot(token)
keyboard1 = telebot.types.ReplyKeyboardMarkup(False,True)
keyboard1.row('Рассчитать концентрацию', 'Сохранить протокол', 'Предобратотать данные','Показать результаты')

@bot.message_handler(commands=['start'])
def send_welcome(message):
         bot.reply_to(message, f'Приятно познакомиться, {message.from_user.first_name}. Я бот, облегчающий работу в лаборатории. Чтобы начать, напиши \'Hello\' или \'Привет\'.')

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /help', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_first_message(message):
    greet = ['hello','hi','привет']
    task = ['рассчитать концентрацию', 'сохранить протокол', 'предобратотать данные','показать результаты']
    if any(greetings in message.text.lower() for greetings in greet):
        bot.send_message(message.from_user.id, 'Hello you! Со мной ты можешь быстро рассчитать необходимые концентрации, предобработать данные, оценить их качество и сделать многое другое! Напиши \'/help\', чтобы увидеть все возможные функции.')
    elif any(word in message.text.lower() for word in task):
        bot.send_message(message.from_user.id, 'упс, пока что функция в разработке')
#бот кидает мемосную картиночку
    else:
        img = Image.open(urlopen(url))
        bot.send_photo(message.chat.id, img)
        img.close()
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит. Напиши \'Hello\' чтобы начать')

bot.polling(True)
