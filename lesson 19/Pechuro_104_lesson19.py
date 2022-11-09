# ДЗ. напишите декоратор который при каждом вызове декорируемой функции выводит её имя (вместе с аргументамим),
# а затем - какое значение она возвращает. после выводится результат её выполнения
import logging

logging.basicConfig(level=logging.DEBUG, filename="homework.log",
                    format="%(asctime)s %(levelname)s %(funcName)s || %(message)s")  # настраиваем журнал-отладки


def debug(func):  # декоратор
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'была вызвана функция: {func.__name__} с аргументами: {args}. её результат = {res}')
        return res

    return wrapper


@debug
def example(x, y):
    logging.info(f"The values of x and y are {x} and {y}.")  # записываем в журнал какие были даны значения
    try:
        x / y
        return x / y   # ругается на это, он без этого нет результата в декораторе
        logging.info(f"x/y successful with result: {x / y}.")  # если всё хорошо то записывается это сообщение в журнал
    except ZeroDivisionError:
        logging.exception("ZeroDivisionError")   # если срабатывает ошибка то записывается это сообщение в журнал


example(4, 5)
example(7, 0)


# Задача:
# 1. Дан список [ [1,2,3], [4, 5, 6], [7, 8, 9] ]
# 2. Напишите функцию, которая возвращает новый список, состоящий из значений кратных 3.
# 3. Напишите декоратор, который будет возвращать количество значений, не кратных 3 из вашей функции.
def decor(func):
    def wrapper(arg):
        res = func(arg)
        print(f'была вызвана функция: {func.__name__} с аргументами: {arg}. её результат = {res}')
        list_count = [s for i in arg for s in i if s % 3 != 0]  # делаем новый список со значениями не кратными 3
        print(f'количество значений не кратных 3 равно {len(list_count)}')  # выводим их количество
        return res

    return wrapper


@decor
def list_of_multiples_of_3(list_):
    new_list = [s for i in list_ for s in i if s % 3 == 0]   # делаем список со занчениями кратными 3
    return new_list


task = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_of_multiples_of_3(task)
