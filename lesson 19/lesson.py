from datetime import datetime


def count_the_time(func):  # параметр func - функция кот мы будем оборачивать
    def wrapper(*args, **kwargs):  # создаем вложенную функцию-обертку
        start = datetime.now()  # отмечаем старт отсчета
        result = func(*args, **kwargs)  # вызываем функцию
        print(datetime.now() - start)  # отмечаем время работы
        return result  # выводим результат переданной функции

    return wrapper  # выводим результат обертки


@count_the_time  # вызов декоратора (оборачиваем функцию)
def create_list_gen(k):
    list_ = [i for i in range(k) if i % 2 == 0]
    return list_


create_list_gen(10)


# задание 1 написать декоратор который будет считать сколько раз была вызвана декорируемая ф-ция
def count_decorator(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        print(f'{func.__name__} была вызвана {wrapper.count} раз')
        return result

    wrapper.count = 0
    return wrapper
