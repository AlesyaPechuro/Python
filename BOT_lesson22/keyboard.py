from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

start = types.ReplyKeyboardMarkup(resize_keyboard=True)  # основа для кнопок

info = types.KeyboardButton('Информация')  # кнопка информации
stats = types.KeyboardButton('Статистика')  # кнопка статистики
razrab = types.KeyboardButton('Разработчик')
user = types.KeyboardButton('Покажи пользователя')
photo = types.KeyboardButton('Отправить фото')

start.add(stats, info, razrab, user, photo)  # добавляем кнопки в основу бота

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

"""-------------------------------Создаем Inline- кнопки для показания пользователя----------------------------------"""

show_user = InlineKeyboardMarkup()
show_user.add(InlineKeyboardButton('Хочу увидеть свой ID', callback_data='user_id'))
show_user.add(InlineKeyboardButton('Вернуться обратно', callback_data='back'))

"""-------------------------------Создаем Inline- кнопки для показания галереи фото----------------------------------"""

show_photo = InlineKeyboardMarkup()
show_photo.add(InlineKeyboardButton('Посмотреть галерею', callback_data='gallery'))
show_photo.add(InlineKeyboardButton('Вернуться обратно', callback_data='back'))
