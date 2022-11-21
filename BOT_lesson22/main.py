from aiogram import Bot, types
from aiogram.utils import executor
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

import config
import keyboard

import logging

storage = MemoryStorage()
bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)  # инициализируем бота
dp = Dispatcher(bot, storage=storage)  # инициализируем диспетчер к нашему боту и хранилище состояний в оп

logging.basicConfig(
    # указываем название с логами
    filename='log.txt',
    # указываем уровень логирования
    level=logging.INFO,
    # указываем формат сохранения логов
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s '
           u'[%(asctime)s] %(message)s')

"""---------------------------------------------- настройка FMS -----------------------------------------------------"""


class Me_info(StatesGroup):
    Q1 = State()  # задаем состояние 1
    Q2 = State()  # задаем состояние 2


# прописываем хендлер на команду me, при этом изначальное состояние не задаем
@dp.message_handler(Command('me'), state=None)  # создаем команду /me для админа
async def enter_me_info(message: types.Message):
    if message.chat.id == config.admin:  # сверяем id с id администратора
        await message.answer("Начинаем настройку \n"  # бот отправит сообщение
                             "1. Укажите ссылку на Ваш профиль")
        # после чего мы изменяем состояние Q1
        await Me_info.Q1.set()  # бот начинает ждать наш ответ, задав состояние Q1


# задаем хендлер для состояния Q1
# обратите внимание, что к состоянию мы обращаемся через атрибут класса
@dp.message_handler(state=Me_info.Q1)
# нашей функции мы указываем, что хотим получить сообщение и состояние
async def answer_for_state_Q1(message: types.Message, state: FSMContext):
    answer = message.text  # сохраняем текст полученного сообщения
    # в данном месте прописываем для нашего состояния обновление данных
    # в пространство имен для текущего состояния
    # мы добавляем ключ answer1 со значением answer, далее мы в этом убедимся
    await state.update_data(answer1=answer)
    await message.answer("Ваша ссылка сохранена \n"
                         "2. Введите текст")
    await Me_info.Q2.set()  # и задаем состояние Q2


# бот будет отлавливать пользователей, которые перейдут в состояние Q2
@dp.message_handler(state=Me_info.Q2)
async def answer_for_state_Q2(message: types.Message, state: FSMContext):
    answer = message.text  # записываем ответ
    await state.update_data(answer2=answer)  # Снова в пространство имен добавляем answer2 со текстом пользователя
    await message.answer("Текст сохранен")  # говорим боту отправить сообщение
    # в переменную data получаем словарь, хранящийся в нашем хранилище состояний для текущего состояния
    data = await state.get_data()
    answer1 = data.get("answer1")  # достаем значение по ключу answer1
    answer2 = data.get("answer2")  # достаем значение по ключу answer2

    with open("link.txt", 'w', encoding="UTF-8") as link_txt:  # открываем файл на режим записи в кодировке UTF-8
        link_txt.write(str(answer1))  # записываем строкой ссылку в наш файл

    with open("text.txt", "w", encoding="UTF-8") as text_txt:  # открываем файл в режиме записи в той же кодировке
        text_txt.write(str(answer2))  # записываем в файл текст, который передал пользователь

    await message.answer(f"Ваша ссылка на профиль: {answer1} \n"  # говорим боту отправить сообщение
                         f"Ваш текст: {answer2}")

    await state.finish()  # закрываем текущее состояние


""" --------------------------------------- обработка команды /start -----------------------------------------------"""


@dp.message_handler(Command('start'), state=None)  # задаем название команды старт
async def welcome(message):
    joinedFile = open('user.txt', 'r')  # создаем файл в который будем записывать id пользователя
    joinedUsers = set()  # создается множество
    for line in joinedFile:  # цикл в котором проверяем имеется ли такой id в файле user
        joinedUsers.add(line.strip())  # метод стрип удаляет пробелы в начале и в конце

    if not str(message.chat.id) in joinedUsers:  # делаем запись в файл user нового id
        joinedFile = open('user.txt', 'a')
        joinedFile.write(str(message.chat.id) + '\n')
        joinedUsers.add(message.chat.id)

    await bot.send_message(message.chat.id, f'ПРИВЕТ, *{message.from_user.first_name}, * БОТ РАБОТАЕТ',
                           reply_markup=keyboard.start, parse_mode='Markdown')
    # после проверки и записи выводим сообщение с именем пользователя и отображением кнопки


"""--------------------------------------- БЛОК КОДА ДЛЯ РАБОТЫ С РАССЫЛКОЙ-----------------------------------------"""


@dp.message_handler(commands=['rassilka'])  # делаем рассылку бота с фотографией
async def rassilka(message: types.Message):
    if message.chat.id == config.admin:  # сможет делать только админ
        await bot.send_message(message.chat.id, f'*Рассылка началась*'
                                                f'\nБот оповестит когда рассылку закончит', parse_mode='Markdown')
        receive_users, block_users = 0, 0  # кол-во получивших фото и кто его заблокировал
        joinedFile = open('user.txt', 'r')
        joinedUsers = set()
        for line in joinedFile:
            joinedUsers.add(line.strip())
        joinedFile.close()
        for user in joinedUsers:
            try:
                await bot.send_photo(user, open('photo.png', 'rb'))
                receive_users += 1
            except:
                block_users += 1
            await asyncio.sleep(0.4)  # делаем слип тк есть ограничение у самой телеги
        await bot.send_message(message.chat.id, f'*Рассылка была завершена*\n'
                                                f'получили сообщение: *{receive_users}*\n'
                                                f'заблокировали бота: *{block_users}*', parse_mode='Markdown')


"""-------------------------------------- ИНФОРМАЦИЯ/СТАТИСТИКА/РАЗРАБОТЧИК ----------------------------------------"""


@dp.message_handler(content_types=['text'])  # указываем боту реагировать на текстовые сообщения
async def get_message(message):
    if message.text == 'Информация':  # если введено слово Информация, то выводит строку
        await bot.send_message(message.chat.id, text='Информация\nБот создан для обучения', parse_mode='Markdown')

    if message.text == 'Статистика':
        await bot.send_message(message.chat.id, text='Хочешь посмотреть статистику бота?', reply_markup=keyboard.stats,
                               parse_mode='Markdown')

    if message.text == 'Разработчик':
        link1 = open('link.txt', encoding='utf-8')  # вытаскиваем с файла инфу, помещаем в переменную и выводим её
        link = link1.read()
        text1 = open('text.txt', encoding='utf-8')
        text = text1.read()
        await bot.send_message(message.chat.id, text=f'Создатель: {link}\n{text}', parse_mode='HTML')


"""------------------------------------------------ КОД ДЛЯ КОЛБЭКА ------------------------------------------------"""


@dp.callback_query_handler(text_contains='join')  # мы прописывали в кнопках на статистику колбэк join и тут ловим его
async def join(call: types.CallbackQuery):
    if call.message.chat.id == config.admin:  # если на кнопку статистика жмет админ
        d = sum(1 for line in open('user.txt'))  # находит сколько пользователей заходило
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'Вот статистика бота: *{d}* человек', parse_mode='Markdown')
        # в этом чате заменяет это сообщение на текст

    else:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text='У тебя нет админки\n Куда ты полез!', parse_mode='Markdown')


@dp.callback_query_handler(text_contains='cancel')
async def cancel(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='Ты вернулся в главное меню. Жми опять кнопки', parse_mode='Markdown')


if __name__ == '__main__':  # создаем точку входа
    print('Бот запущен!')
    executor.start_polling(dp, skip_updates=True)  # запускаем бота
