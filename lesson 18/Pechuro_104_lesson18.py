import string


# ДЗ
class Tomato:  # класс томаты содердащий словарь со стадиями созревания
    states = {0: 'первые листики',
              1: 'рост',
              2: 'цветение',
              3: 'формирование плодов',
              4: 'вызревание плодов'}

    def __init__(self, index):  # передается номер куста который начинает с 0 стадии роста
        self._index = index
        self._state = 0

    def grow(self):  # переводит томат на следующую стадию
        while self._state < 4:
            self._state += 1
            print(f'томат № {self._index} на стадии - {Tomato.states[self._state]}')

    def is_ripe(self):  # проверяет созрел ли томат
        if self._state == 4:
            print(f'томат № {self._index} - созрел')
        else:
            print(f'томат № {self._index} - не созрел')


class TomatoBush:  # создает список объектов класса (т.е количество томатных кустов)
    def __init__(self, amount):
        self.tomatoes = [Tomato(index) for index in range(1, amount + 1)]

    def grow_all(self):  # переводит все кусты на следующий этап
        for tomatoes in self.tomatoes:
            tomatoes.grow()

    def all_are_ripe(self):  # проверяет созрели ли все кусты
        ripe_tomato = []  # для этого создаем пустой список
        for tomato in self.tomatoes:  # проверяем каждй куст из списка кустов
            if tomato.is_ripe():  # если куст созрел
                ripe_tomato.append(tomato)  # то добавялем его в список созревших кустов
        if all(ripe_tomato):  # если все кусты в списке будут созревшие
            return True  # выводим тру
        else:
            return False
        # можно было
        # return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):  # чистим список томатов после сбора урожая
        self.tomatoes.clear()


class Gardener:  # создаем садовника (plant - объект класса томатобуш)
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):  # садовник работает
        print(f'садовник {self.name} работает')
        self._plant.grow_all()

    def harvest(self):  # сбор урожая
        if self._plant.all_are_ripe():
            print('Все созрело - собираем урожай')
            self._plant.give_away_all()
        else:
            print('томатам надо ещё подрости')

    @staticmethod
    def knowledge_base():  # выводит справку по сбору урожая
        print('томат проходит жизненный путь в 4 этапа. на последнем этапе его собирают')


Gardener.knowledge_base()
bush = TomatoBush(2)
ricardo = Gardener('Ricardo', bush)
ricardo.work()
ricardo.harvest()


# # пример
# class Phone:
#
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#
#     def check_sim(self, mobile_operator):  # обычный метод. первый параметр - self
#         if self.model == 'I785' and mobile_operator == "MTS":
#             print('Your mobile operator is MTS')
#
#     @staticmethod  # статический метод возвращает хэш по номеру модели
#     def model_hash(model):
#         if model == 'I785':
#             return 34565
#         elif model == 'K498':
#             return 45567
#         else:
#             return None
#
#     @classmethod  # метод класса
#     def toy_phone(cls, color):
#         toy_phone = cls(color, 'ToyPhone', None)
#         return toy_phone
#
#
# Phone.model_hash('I785')
# my_phone = Phone('red', 'I785')
# my_phone.check_sim('MTS')


# задание 1
class Human:
    default_name = 'No name'  # статические поля
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name  # динамические публичные поля
        self.age = age
        self.__money = 0  # приватные поля
        self.__house = None

    def info(self):
        print(f'Имя - {self.name}')
        print(f'Возраст - {self.age}')
        print(f'Дом - {self.__house}')
        print(f'Денег - {self.__money}')

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)

    def earn_money(self, money):  # метод увеличивающий баланс денег
        self.__money += money
        print(f'баланс составляет - {self.__money}')

    def buy_house(self, house, discont):  # покупка дома
        price = house.final_price(discont)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print('Недостаточно денег!')

    def __make_deal(self, house, price):  # совершение сделки
        self.__money -= price
        self.__house = house


# Human.default_info()
# Anna = Human('Anna', 30)
# Anna.info()
# Anna.earn_money(60000)
# Anna.earn_money(1000)
# Anna.info()


# задание 2
class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discont):  # цена с учетом скидки
        final_price = self._price - (self._price * discont / 100)
        print(f'конечная стоимость = {final_price}')


class SmallHouse(House):
    area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.area, price)


small_house = SmallHouse(85000)
kate = Human('Kate', 25)
kate.earn_money(100000)
kate.buy_house(small_house, 5)
kate.info()


# задание 3
class Alphabet:
    def __init__(self, language, letters):  # язык и список букв
        self.lang = language
        self.letters = list(letters)

    def print(self):  # выводит буквы алфавита
        print(self.letters)

    def letters_num(self):  # вернет количество букв в алфавите
        return len(self.letters)


class EngAlphabet(Alphabet):
    def __init__(self):  # возвраащет обозначение английского языка и его алфавит
        super().__init__('En', string.ascii_uppercase)

    __letters_num = 26  # количетво букв в английском алфавите

    def is_en_letter(self, letter):  # проверяет есть ли такая буква в алфавите
        if letter in self.letters:
            print('такая буква есть в алфавите')
        else:
            print('такой буквы нет')

    def letters_num(self):  # переопределяет родительский метод
        return self.__letters_num

    @staticmethod  # статический метод который выводит английский текст
    def example():
        print('London is the capital of Great Britain')


english = EngAlphabet()  # создаем объект класса
english.print()  # печатаем буквы алфавита
print(english.letters_num())  # вводим количество букв в алфавите
print(english.is_en_letter('F'))  # проверяем относится ли буква к данному алфавиту
print(english.is_en_letter('Щ'))
print(english.example())  # печатаем английский текст
