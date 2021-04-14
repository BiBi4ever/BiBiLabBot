import telebot

callback_query_handler={'Поиск по ключу':'key',
                        'Поиск с кнопками':'button'}

callback_query_handler1={'Работа с НК':'acid',
                        'ПЦР':'PCR',
                        'Назад':'back'}
                         
callback_query_handler2={'Назад':'back1'}

callback_data_keyboard_Acid={'Выделение ДНК по Хомчински':'1DmogZzc5-vEgDxxqiCB4sC3wHOb9KYHc',
                        'Выделение ДНК на магнитах':'1C_TYw363bHUPfdFXumlmeqA1TEDP3YEd',
                        'Выделение РНК':'1Cmvh8kn6BgqiMDcdN1xEF93JXsmyvHfw',
                        'Обратная транскрипция':'1uZr7I87Ow6VqzTTBqg_0OzuriqUm-Ip-'}

callback_data_keyboard_PCR={'Обычная ПЦР':'1Lr0dWQySLjaqHYoc9xG424zUlHTa_sUV',
                        'Real time ПЦР c зондами': '1O3Qe9OsAX-k3dT9-kvAfawOYsidYkbxR',
                        'Real time ПЦР sybr':'1WOv4aIC3BG8X05pUSdYPLm1u12MxJAHz'}

keyboard_for_buttons = telebot.types.InlineKeyboardMarkup().add(
        telebot.types.InlineKeyboardButton([key for key in callback_query_handler][0],callback_data=[values for values in callback_query_handler.values()][0]),
        telebot.types.InlineKeyboardButton([key for key in callback_query_handler][1],callback_data=[values for values in callback_query_handler.values()][1]))

keyboard_for_buttons1 = telebot.types.InlineKeyboardMarkup(row_width=2).add(
            telebot.types.InlineKeyboardButton([key for key in callback_query_handler1][0],callback_data=[values for values in callback_query_handler1.values()][0]),
            telebot.types.InlineKeyboardButton([key for key in callback_query_handler1][1],callback_data=[values for values in callback_query_handler1.values()][1]),
            telebot.types.InlineKeyboardButton([key for key in callback_query_handler1][2],callback_data=[values for values in callback_query_handler1.values()][2]))

keyboard_for_buttons2 = telebot.types.InlineKeyboardMarkup(row_width=1).add(
            telebot.types.InlineKeyboardButton([key for key in callback_data_keyboard_Acid][0], callback_data=[values for values in callback_data_keyboard_Acid.values()][0]),
            telebot.types.InlineKeyboardButton([key for key in callback_data_keyboard_Acid][1], callback_data=[values for values in callback_data_keyboard_Acid.values()][1]),
            telebot.types.InlineKeyboardButton([key for key in callback_data_keyboard_Acid][2], callback_data=[values for values in callback_data_keyboard_Acid.values()][2]),
            telebot.types.InlineKeyboardButton([key for key in callback_data_keyboard_Acid][3], callback_data=[values for values in callback_data_keyboard_Acid.values()][3]),
            telebot.types.InlineKeyboardButton([key for key in callback_query_handler2][0], callback_data=[values for values in callback_query_handler2.values()][0]))

keyboard_for_buttons3 = telebot.types.InlineKeyboardMarkup(row_width=1).add(
            telebot.types.InlineKeyboardButton([key for key in callback_data_keyboard_PCR][0],callback_data=[values for values in callback_data_keyboard_PCR.values()][0]),
            telebot.types.InlineKeyboardButton([key for key in callback_data_keyboard_PCR][1], callback_data=[values for values in callback_data_keyboard_PCR.values()][1]),
            telebot.types.InlineKeyboardButton([key for key in callback_data_keyboard_PCR][2], callback_data=[values for values in callback_data_keyboard_PCR.values()][2]),
            telebot.types.InlineKeyboardButton([key for key in callback_query_handler2][0],callback_data=[values for values in callback_query_handler2.values()][0]))

