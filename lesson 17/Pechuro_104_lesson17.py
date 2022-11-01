# дз два метода в классе - один принимает в себя либо строку либо число.
# если строка: если произведение гласных и согласных <= длине слова, то выводить все гласные. иначе согласные.
# если число: произведение суммы четных цифр на длину числа. длину строки и числа искать во втором методе
class Dz:
    data = input('введите строку или число: ')

    def string_or_number(self):  # первый метод
        if self.data.isdigit():  # если ввели число
            sum_ = sum([int(i) for i in str(self.data) if int(i) % 2 == 0])  # находим сумму четных цифр
            return sum_ * self.length()
        elif self.data.isalpha():  # если ввели строку
            vowels = []  # гласные
            consonants = []  # согласные
            for h in self.data:  # проходимся циклом по строке
                if h in 'eyuioa' or h in 'аоуэыяюеи':  # находим гласные
                    vowels.append(h)  # и добавляем их в список
                else:
                    consonants.append(h)  # иначе добавляем в список для согласных
            if len(vowels) * len(consonants) <= self.length():  # если произведение гласных и согласных <= длины строки
                return vowels  # возвращает список гласных
            else:
                return consonants  # иначе возвращаем список согласных
        else:
            print('ввели неверные данные')

    def length(self):  # второй метод
        return len(self.data)  # находим длину строки или числа


chek = Dz()
print(chek.string_or_number())


class Car:  # создаем класс

    # статические поля (переменные класса)
    default_color = 'grey'
    default_weight = 5000

    def turn_on(self):
        pass

    def ride(self):
        pass


car_object = Car()  # создаем объект класса
print(dir(Car))


# задание 1 создаем класс и пишем 3 функции. две переменные статические и две динамические.
# первая функция: создайте переменную и выведите её. вторая функция: верните сумму 2-ух глобал. переменных.
# третья: верните результут возведения первой динам. пер во вторую динам. пер. создайте объект класса.
# напечатайте обе функции. напечатайте переменную а
class Example:
    price = 45  # создали 2 статические переменные
    weight = 500

    def __init__(self, length, number):  # создаем функцию с 2 динамическими переменными
        self.length = length
        self.number = number
        print(length, number)

    def func(self):  # функция создает переменную и выводит её
        self.a = 5
        print(self.a)

    def sum_(self):  # функция возвращает сумму двух переменных
        return self.price + self.weight

    def square(self):  # функция возвращает возведение в степень
        return self.length ** self.number


object_ = Example(4, 9)  # создаем объект класса и передаем динамические переменные

print(Example.price)
print(object_.sum_(), object_.square(), sep='\n')
Example.func()


# задание 2 калькулятор. функции для математических операций и функция для ввода данных
class Calculator:
    def __init__(self):
        self.number1 = int(input('введите первое число: '))
        self.number2 = int(input('введите второе число: '))

    def sum_(self):
        return self.number1 + self.number2

    def difference(self):
        return self.number1 - self.number2

    def product_of_numbers(self):
        return self.number1 * self.number2

    def division(self):
        if self.number2 == 0:
            print('деление на ноль!')
        else:
            return self.number1 / self.number2


cal = Calculator()
print(cal.sum_(), cal.difference(), cal.product_of_numbers(), cal.division())
