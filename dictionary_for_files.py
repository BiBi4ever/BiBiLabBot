storage = {
'dna extraction XOM':'https://drive.google.com/file/d/1DmogZzc5-vEgDxxqiCB4sC3wHOb9KYHc/view?usp=sharing',
'dna extraction MAG':'https://drive.google.com/file/d/1C_TYw363bHUPfdFXumlmeqA1TEDP3YEd/view?usp=sharing'
}


''' сам костыль
def protocol_responce(message):
    for i in storage.keys():
        if message.text.lower() == i:
            bot.send_message(message.from_user.id, storage[i])
'''