import math
import random

a = 6
b = 2

c = a * b  # умножение
d = a / b  # деление
f = a ** b  # возведение в степень
g = a // b  # целочисленное деление
e = a % b  # остаток от деления
print(c, d, f, g, e)

# задание 1
num1 = int(input("ведите первое число: "))
num2 = int(input("ведите второе число: "))
num3 = int(input("ведите третье число: "))
print(num1 + num2 + num3,
      num1 - num2 - num3,
      num1 / num2 / num3,
      num1 ** num2 ** num3)

# задание 2
var1 = 17 / 2 * 3 + 2
var2 = 2 + 17 / 2 * 3
var3 = 19 % 4 + 15 / 2 * 3
var4 = (15 + 6) - 10 * 4
var5 = 17 / 2 % 2 * 3 ** 3
print(var1, var2, var3, var4, var5)

# задание 3
money = 11
cost = 1.5
bread = 3
print(money - cost * bread)

# задание 4 высчитываем среднее кол-во человек
people = 17
print((30 + 33 + 24 + 28 + 31 + 33 + 38 + 29 + 22 + 31 + 28 + 15 + 32 + 29 + 21 + 41 + 49) / people)

# задание 5 программа по преобразованию градусов в радианы
var = int(input("введите градусы: "))
print(math.radians(var))

# задание 6 находим дискриминант
a, b, c = int(input("введите значение а: ")), int(input("введите значение b: ")), int(input("введите значение c: "))
print("дискриминант равен: ", b ** 2 - 4 * a * c)

# задание 7 вычислить сумму цифр случайного трёхзначного числа
num = random.randint(100, 999)
num1 = num // 100
num2 = num / 10 % 10
num3 = num % 10
print(num1 + num2 + num3)

# задание 8 найти площадь и периметр прямоугольного треугольника
storona1 = int(input('введите значение 1 катета: '))
storona2 = int(input('введите значение 2 катета: '))
storona3 = int(input('введите значение гипотенузы: '))
perimetr = storona1 + storona2 + storona3
square = (storona1 + storona2) / 2
print('площадь прямоугольного треугольника = ', square,
      'периметр прямоугольника =', perimetr)
