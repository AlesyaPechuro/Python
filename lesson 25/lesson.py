class Something:

    # переопределяем метод __new__ в кот обязательно делаем ссылку на текущий класс и прием неогранич кол-ва аргументов
    def __new__(cls, *args, **kwargs):
        # выводим сообщение о том что наш метод нью сработал
        # print(f'сработал __new__ для класса: {cls.__name__}')
        print(f'__new__ сработал, переданы аргументы: {args, kwargs}')

        # добавляем новый атрибут, для этого мы переопределяем метод родителя (object)
        instance = super().__new__(cls)

        # добавляем к экземпляру новый атрибут
        instance.new_attribute = 'добавлено'

        return instance

    def __init__(self, name, age):
        self.name = name
        self.age = age


example = Something('Alesya', 25)


# практика
class FileObject:

    def __init__(self, filename):  # создать класс на открытие файла из директории
        self.file = open(filename, 'r+', encoding='utf-8')

    def read_file(self):  # прочитать строки
        print(self.file.readlines())

    def __del__(self):  # метод на закрытие файла и его удаление
        print('__del__ сработал')
        self.file.close()
        del self.file


new_obj = FileObject('example.txt')
new_obj.read_file()


class Word(str):
    # класс для слов, определяющий сравнение по длине слов

    def __new__(cls, word):
        # мы должны использовать нью тк тип str неизменяемый и мы должны инициализировать его при создании
        if ' ' in word:  # если введенное слово содержит пробел - обрезаем символы до него
            word = word[:word.index(' ')]  # теперь ворд - все символы до первого пробела
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)


exam = Word('один два')
print(exam > 'два')
print(exam < 'два')
print(exam == 'два')
print(exam != 'два')
