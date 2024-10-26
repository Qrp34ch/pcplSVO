import telebot
import random
from telebot import types
import datetime

# Загружаем список праздников
f = open('facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
# Загружаем список цитат
f = open('thinks.txt', 'r', encoding='UTF-8')
thinks  = f.read().split('\n')
f.close()
# Создаем экземпляр бота
bot = telebot.TeleBot('7727784858:AAEjg_LbdEZYd-Dd3o-hjVF9LTfc9sX_TcI')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем три кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("ура")
        item2=types.KeyboardButton("сосмыслом")
        item3=types.KeyboardButton("пока")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(m.chat.id, 'Привет, ' + m.chat.first_name + '!\nЕсли ищешь повод для тусовки, напиши "ура"\nХочешь цитату Стетхема? Напиши "сосмыслом"\nХочешь уйти? Напиши "пока"',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему сегодняшний праздник
    if message.text.strip() == 'ура' :
            print(message.chat.first_name + ' поинтересовался праздником')
            current_time = datetime.datetime.now()
            dat = str(current_time.day) + '.' + str(current_time.month)
            dat1 = str(current_time.day + 1) + '.' + str(current_time.month)
            dat2 = '1.' + str(current_time.month + 1)
            answer = 'Праздники сегодня ('+ dat +'):' + '\n'
            sd = 4315
            sd1 = 4315
            for datee in facts:
                if datee.find(dat) != -1:
                        fd = facts.index(datee)
                        break

            for datee in facts:
                if datee.find(dat1) != -1:
                        sd = facts.index(datee)
                        break
            for datee in facts:
                if datee.find(dat2) != -1:
                        sd1 = facts.index(datee)
                        break
            if sd > sd1:
                   sd = sd1
            for i in range (fd + 1, sd):
                        answer += facts[i] + '\n'

    # Если юзер прислал дату, выдаем ему праздник
#     elif message.text.strip() == 'ура0_0' :
#             bot.send_message(message.chat.id, 'Напиши дату, я скажу, какие в этот день праздники')
#             def handle_text(message1):
#             answer = 'с днем дня'
    # Если юзер прислал 2, выдаем умную мысль
    elif message.text.strip() == 'сосмыслом':
            answer = random.choice(thinks)
            print(message.chat.first_name + ' поинтересовался цитатами')
    elif message.text.strip() == 'пока' or message.text.strip() == 'Пока':
            answer = 'Пока, ' + message.chat.first_name + '! До скорой встречи!'
            print(message.chat.first_name + ' ушел в поисках счастья')
    else:
            answer = 'Я не умею отвечать на другие темы, воспользуйся кнопками, пожалуйста'
            print(message.chat.first_name + ': ' + message.text)
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)
    # bot.send_message(message.chat.id, 'АХАХАХАХАХ: ' + message.text + ': в траве сидел чигоснче')
# Запускаем бота
bot.polling(none_stop=True, interval=0)
