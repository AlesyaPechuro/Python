# пример создания итератора из списка
elems = [1, 2, 3]
iter_list = iter(elems)
print(next(iter_list))  # >>> 1
print(next(iter_list))  # >>> 2
print(next(iter_list))  # >>> 3
print(next(iter_list))  # >>> StopIteration

# Файл как итератор
f = open('example.txt', 'r', encoding='UTF-8')
print(type(f))  # получаем тип нашей переменной
print('__next__' in f.__dir__())  # убеждаемся в том, что __next__ есть у нашего объекта
print(f.__next__())
print(f.__next__())
print(f.__next__())


class Xrange:
    def __init__(self, start=0.0, stop=0.0, step=0.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        """
        Каждый раз, когда мы будем вызывать метод __iter__
        у нас self.value будет инициализироваться на начало арифметической прогрессии
        """
        self.value = self.start - self.step
        return self  # возвращается сам экземпляр класса

    def __next__(self):
        """
        По сути, определив метод __next__, мы указали способ образования
        новых значений.
        """
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


"""
Попробуем проверить
"""

example = Xrange(3, 6, 1)
for elem in example:
    print(elem)


# генератор
def example(x):
    n1, n2 = 0, 1  # задаем стартовые значения
    for _ in range(x):  # проходим по прогрессии от 0 до x
        yield n1  # запоминаем значение n1
        n1, n2 = n2, n1 + n2  # меняем местами значения переменных


# получаем все значения по заданному аргументу
for _ in example(8):
    print(_)
