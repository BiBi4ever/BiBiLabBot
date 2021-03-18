import telebot

callback_query_handler={'Поиск по ключу':'key',
                        'Поиск с кнопками':'button'}

callback_query_handler1={'Работа с нуклеиновыми кислотами':'acid',
                        'Работа с ПЦР':'PCR',
                        'Назад':'back'}
                         
callback_query_handler2={'Назад':'back1'}

callback_data_keyboard_Acid={'Выделение ДНК по Хомчински':'',
                        'Выделение ДНК на магнитах':'',
                        'Выделение РНК':'',
                        'Обратная транскрипция':''}

callback_data_keyboard_PCR={'Обычная ПЦР':'',
                        'Реал тайм ПЦР с зондами': '',
                        'Реал тайм ПЦР на sybr green':''}

List_keyboards_with_url = [keyboard_for_buttons2, keyboard_for_buttons3] 

for i in callback_query_handler:
    button = telebot.types.InlineKeyboardButton([i],callback_data=callback_query_handler[i])
    keyboard_for_buttons = telebot.types.InlineKeyboardMarkup().add(button)

for i in callback_query_handler1:
    button1 = telebot.types.InlineKeyboardButton([i],callback_data=callback_query_handler1[i])
    keyboard_for_buttons1 = telebot.types.InlineKeyboardMarkup().add(button1)

for i in callback_data_keyboard_Acid:
    button2 = telebot.types.InlineKeyboardButton([i], url=callback_data_keyboard_Acid[i])
    keyboard_for_buttons2 = telebot.types.InlineKeyboardMarkup().add(button2)

for i in callback_data_keyboard_PCR:
    button3 = telebot.types.InlineKeyboardButton([i], url=callback_data_keyboard_PCR[i])
    keyboard_for_buttons3 = telebot.types.InlineKeyboardMarkup().add(button3)
    
for i in range(len(List_keyboards_with_url)):
    button_back = telebot.types.InlineKeyboardButton([key for key in callback_query_handler2][0], callback_data=[values for values in callback_query_handler2.values()][0])
    i = telebot.types.InlineKeyboardMarkup().add(button_back)
