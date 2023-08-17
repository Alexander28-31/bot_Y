import os

import telebot
from dotenv import load_dotenv
from telebot import types
from information import *
load_dotenv()

token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def start_message(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb2 = types.InlineKeyboardMarkup()
    btn1 = types.KeyboardButton(text=' Последнее селфи Александра ')
    btn2 = types.KeyboardButton(text=' Фото из старшей школы ')
    kb.add(btn1, btn2)
    btn3 = types.KeyboardButton(text='Мои увлечения')
    kb.add(btn3)
    bot.send_message(message.chat.id,
                     f'Привет {message.from_user.first_name}: я Телеграм Бот, который поможет вам узнать об Александре✌',
                     reply_markup=kb)
    bot.send_message(message.chat.id, f'{message.from_user.first_name}:  тут ты сможешь посмотреть его фотографии')
    bot.send_message(message.chat.id, ' Для просмотра информации о Александре, достаточно написать в чат /about')
    bot.send_message(message.chat.id, ' Для прослушивания ответа на вопрос /voice')
    bot.send_message(message.chat.id,
                     ' Для просмотра доступных команд, нужно написать /help или написать / в строке вода текста')
    bot.send_message(message.chat.id, ' Для вовзрата в начальное меню, нужно написать /exit')
    btn4 = types.InlineKeyboardButton('Перейти в git Александра', GIT_HUB)
    kb2.add(btn4)
    bot.send_message(message.chat.id,
                     f'Для просмотра репозитория, тебе {message.from_user.first_name},нужно перейти по ссылке',
                     reply_markup=kb2)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, HELP_MESSAGE)


@bot.message_handler(commands=['exit'])
def exit_start_message(message):
    start_message(message)


@bot.message_handler(commands=['about'])
def abount_me_message(message):
    bot.send_message(message.chat.id, ABOUT_ME)


@bot.message_handler(commands=['voice'])
def questions_message(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text=' Что такое GPT')
    btn2 = types.KeyboardButton(text=' Разница между SQL и NoSQL')
    btn3 = types.KeyboardButton(text=' История первой любви')
    kb.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, ' Для прослушивания ответов, выберите нужный вопрос', reply_markup=kb)


@bot.message_handler(func=lambda message: True)
def unkown_message(message):
    if message.text.startswith('/') and message.text not in COMMANDS:
        help_message(message)
    elif message.text in MENU:
        get_text_messages(message)
    else:
        bot.send_message(message.chat.id, f'{message.from_user.first_name}, я вас не понимаю. '
                                          'Используйте команду /help  для использования доступных команд.')


@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    if message.text == 'Последнее селфи Александра':
        with open('media/photo/1.jfif', 'rb') as photo:
            bot.send_photo(message.chat.id, photo=photo, caption='Фотографии несколько лет')
    elif message.text == 'Фото из старшей школы':
        with open('media/photo/2.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo=photo, caption='Фота  не, но есть фото  Панды)')
    elif message.text == 'Мои увлечения':
        with open('media/text/text.txt', 'rb') as text:
            bot.send_document(message.chat.id, document=text, caption='Мои увлечения')
    elif message.text == 'Что такое GPT':
        with open('media/audio/GPT.m4a', 'rb') as audio:
            bot.send_audio(message.chat.id, audio=audio, caption='Прослушать: что такое GPT')
    elif message.text == 'Разница между SQL и NoSQL':
        with open('media/audio/SQL_NoSQL.m4a', 'rb') as audio:
            bot.send_audio(message.chat.id, audio=audio, caption='Прослушать: разница между SQL и NoSQL')
    elif message.text == 'История первой любви':
        with open('media/audio/Love.m4a', 'rb') as audio:
            bot.send_audio(message.chat.id, audio=audio, caption='Прослушать: история первой любви')


if __name__ == '__main__':
    bot.polling(none_stop=True)
