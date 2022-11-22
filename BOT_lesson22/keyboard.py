from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

start = types.ReplyKeyboardMarkup(resize_keyboard=True)  # основа для кнопок

info = types.KeyboardButton('Информация')  # кнопка информации
stats = types.KeyboardButton('Статистика')  # кнопка статистики
razrab = types.KeyboardButton('Разработчик')

start.add(stats, info, razrab)  # добавляем кнопки в основу бота

"""--------------------------------------Создаем Inline- кнопки для Статистики--------------------------------------"""

stats = InlineKeyboardMarkup()  # создаем основу для инлайн кнопки
stats.add(InlineKeyboardButton('Да', callback_data='join'))  # создаем кнопку и калбэк к ней
stats.add(InlineKeyboardButton('Нет', callback_data='cancel'))

"""--------------------------------------Создаем Inline- кнопки для Разработчика-------------------------------------"""

creator = InlineKeyboardMarkup()
creator.add(InlineKeyboardButton('Да', callback_data='link'))
creator.add(InlineKeyboardButton('Нет', callback_data='cancel'))

"""--------------------------------------Создаем Inline- кнопки для Литературы---------------------------------------"""

infolink = InlineKeyboardMarkup()
infolink.add(InlineKeyboardButton('Документация по Aiogram', url='https://docs.aiogram.dev/en/latest/'))
infolink.add(InlineKeyboardButton('Дополнительно про разработку бота', url='https://habr.com/ru/post/442800/'))