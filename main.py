import random

import telebot
import re
from telebot import types


bot = telebot.TeleBot('')

@bot.message_handler(content_types=['text'])

@bot.message_handler(func = lambda message: True)
def answer_to_user(message):
    print('%s (%s): %s' %(message.chat.first_name, message.chat.username, message.text))
    msg = None

    user_message = message.text.lower()

    if BOT_NAME:
        regex = re.compile(BOT_NAME.lower())
        print(regex.search(user_message))
        if regex.search(user_message) == None:
            return

        regex = re.compile('%s[^a-z]'%(BOT_NAME.lower()))
        user_message = regex.sub("", user_message)

    user_message = user_message.lstrip()
    user_message = user_message.rstrip()

    print(user_message)
    #print("Сообщение выведено успешно")

# Обработка сообщений и команд

    if message.text == "/start":
        bot.send_message(message.from_user.id, "Я бот")


    else:
        jopa = message.text
        #with open("pizdagovno.txt", "r", encoding='utf-8') as f:
        #    tb = f.readline()
        #    tb = int(tb)
        #    print(tb)
        #    tb += 1
        with open("pizdagovno.txt", "a+", encoding='utf-8') as f:
            f.write(jopa + "\n")
            count = 0
            with open('pizdagovno.txt', 'rb') as f:
                for line in f:
                    count += 1

            print(count)

        with open("pizdagovno.txt", "r",  encoding='utf-8') as f:
            hhh=random.randint(1, 3)
            if hhh==2:
                dg = (random.randint(1, count-4))
                text = f.readlines()
                print(text[dg])
                bot.send_message(message.chat.id, (text[dg]))
            else:
                print("Не удалось")





BOT_NAME = ''
bot.polling(none_stop=True, interval=0)
