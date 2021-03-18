import telebot

callback_query_handler={'Поиск по ключу':'key',
                        'Поиск с кнопками':'button'}

callback_query_handler1={'Работа с нуклеиновыми кислотами':'acid',
                        'Работа с ПЦР':'PCR',
                        'Назад':'back'}
                         
callback_query_handler2={'Назад':'back1'}

callback_data_keyboard_Acid={'Выделение ДНК по Хомчински':'https://drive.google.com/file/d/1DmogZzc5-vEgDxxqiCB4sC3wHOb9KYHc/view?usp=sharing',
                        'Выделение ДНК на магнитах':'https://drive.google.com/file/d/1C_TYw363bHUPfdFXumlmeqA1TEDP3YEd/view?usp=sharing',
                        'Выделение РНК':'https://drive.google.com/file/d/1mzLZRFX3hDsQpm18QD_op8mg89E29Z-P/view',
                        'Обратная транскрипция':'https://drive.google.com/file/d/1uZr7I87Ow6VqzTTBqg_0OzuriqUm-Ip-/view'}

callback_data_keyboard_PCR={'Обычная ПЦР':'https://s.tcdn.co/ec5/c1b/ec5c1b75-12ea-45bd-aa7b-33491089b8e5/1.png',
                        'Реал тайм ПЦР с зондами': 'https://s.tcdn.co/ec5/c1b/ec5c1b75-12ea-45bd-aa7b-33491089b8e5/8.png',
                        'Реал тайм ПЦР на sybr green':'https://s.tcdn.co/ec5/c1b/ec5c1b75-12ea-45bd-aa7b-33491089b8e5/11.png'}

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

List_keyboards_with_url = [keyboard_for_buttons2, keyboard_for_buttons3] 
    
for i in range(len(List_keyboards_with_url)):
    button_back = telebot.types.InlineKeyboardButton([key for key in callback_query_handler2][0], callback_data=[values for values in callback_query_handler2.values()][0])
    i = telebot.types.InlineKeyboardMarkup().add(button_back)
