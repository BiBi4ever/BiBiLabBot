import telebot

callback_query_handler={'Поиск по ключу':'key',
                        'Поиск с кнопками':'button'}

callback_query_handler1={'Работа с НК':'acid',
                        'ПЦР':'PCR',
                        'Назад':'back'}
                         
callback_query_handler2={'Назад':'back1'}

callback_data_keyboard_Acid={'Выделение ДНК \nпо Хомчински':'DNA_KCHOMCHINSKY',
                        'Выделение ДНК \nна магнитах':'DNA_MAGNET',
                        'Выделение РНК':'RNA',
                        'Обратная \nтранскрипция':'REVERSE_TRANSCRIPTION'}

callback_data_keyboard_PCR={'Обычная ПЦР':'PCR_REARE',
                        'Реал тайм \n ПЦР зонд': 'PCR_WITH_ZOND',
                        'Реал тайм \n ПЦР sybr':'PCR_SYBRE'}

keyboard_for_buttons = telebot.types.InlineKeyboardMarkup().add(
        telebot.types.InlineKeyboardButton([key for key in callback_query_handler][0],callback_data=[values for values in callback_query_handler.values()][0]),
        telebot.types.InlineKeyboardButton([key for key in callback_query_handler][1],callback_data=[values for values in callback_query_handler.values()][1]))

keyboard_for_buttons1 = telebot.types.InlineKeyboardMarkup(row_width=2).add(
            telebot.types.InlineKeyboardButton([key for key in callback_query_handler1][0],callback_data=[values for values in callback_query_handler1.values()][0]),
            telebot.types.InlineKeyboardButton([key for key in callback_query_handler1][1],callback_data=[values for values in callback_query_handler1.values()][1]),
            telebot.types.InlineKeyboardButton([key for key in callback_query_handler1][2],callback_data=[values for values in callback_query_handler1.values()][2]))

keyboard_for_buttons2 = telebot.types.InlineKeyboardMarkup(row_width=2).add(
            telebot.types.InlineKeyboardButton([key for key in callback_data_keyboard_Acid][0], callback_data=[values for values in callback_data_keyboard_Acid.values()][0]),
            telebot.types.InlineKeyboardButton([key for key in callback_data_keyboard_Acid][1], callback_data=[values for values in callback_data_keyboard_Acid.values()][1]),
            telebot.types.InlineKeyboardButton([key for key in callback_data_keyboard_Acid][2], callback_data=[values for values in callback_data_keyboard_Acid.values()][2]),
            telebot.types.InlineKeyboardButton([key for key in callback_data_keyboard_Acid][3], callback_data=[values for values in callback_data_keyboard_Acid.values()][3]),
            telebot.types.InlineKeyboardButton([key for key in callback_query_handler2][0], callback_data=[values for values in callback_query_handler2.values()][0]))

keyboard_for_buttons3 = telebot.types.InlineKeyboardMarkup(row_width=2).add(
            telebot.types.InlineKeyboardButton([key for key in callback_data_keyboard_PCR][0],callback_data=[values for values in callback_data_keyboard_PCR.values()][0]),
            telebot.types.InlineKeyboardButton([key for key in callback_data_keyboard_PCR][1], callback_data=[values for values in callback_data_keyboard_PCR.values()][1]),
            telebot.types.InlineKeyboardButton([key for key in callback_data_keyboard_PCR][2], callback_data=[values for values in callback_data_keyboard_PCR.values()][2]),
            telebot.types.InlineKeyboardButton([key for key in callback_query_handler2][0],callback_data=[values for values in callback_query_handler2.values()][0]))

