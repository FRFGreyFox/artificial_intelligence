
'''
@bot.message_handler(content_types=['text'])
def get_text_messanger(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, 'Привет, чем могу тебе помочь?')
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши Привет')
    else:
        bot.end_message(message.from_user.id, 'Я тебя не понимю напиши /help')
'''

import telebot
from telebot import types
bot = telebot.TeleBot('1932954196:AAFo5tVnaOTSPiInoDAsIbIVYLYNfjh1f2k')

name = ''
surname = ''
age = 0

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Привет, а как тебя зовут?")
        bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')


def get_name(message): #получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id,'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')



        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')  # кнопка «Да»
        keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_no)
        question = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_worker(call):
            if call.data == "yes":  # call.data это callback_data, которую мы указали при объявлении кнопки
                # код сохранения данных, или их обработки
                bot.send_message(call.message.chat.id, 'Запомню, пообщаемся? Напиши "Давай общаться"')
            elif call.data == "no":
                bot.send_message(call.message.chat.id, 'Прости, я буду и дальше стараться, попробуем еще раз? /reg ?')

def a_tebya(message):
    if message.text == "Давай общаться":
        bot.send_message(message.from_user.id, "Давай " + name)
    else:
        bot.send_message(message.from_user.id, "Может все таки пообщаемся?")


bot.polling(none_stop=True, interval=0)


''' для стикеров
stickers = ['CAACAgIAAxkBAAED5AtiBiVqFTecIAL-4NRr1oTZPm8jvQAC4xMAAhDpkEvE2ddihWmL4yME',
                'CAACAgIAAxkBAAED5AliBiU7-mqMe8dsGt4IZ3drFRa5OgACZAUAAj-VzAoEyzewVHTnAAEjBA']
                # message.sticker.file_id
                bot.send_sticker(message.from_user.id, random.choice(stickers))'''