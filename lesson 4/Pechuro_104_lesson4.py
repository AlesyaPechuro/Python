import random

# задание 7 Существует ли такой треугольник, если сумма 2-х сторон больше третьей
# мы должны сравнить длину каждого отрезка с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника не существует.
stor1 = int(input('введите значение 1 стороны: '))
stor2 = int(input('введите значение 2 стороны: '))
stor3 = int(input('введите значение 3 стороны: '))
if stor1 + stor2 > stor3 and stor1 + stor3 > stor2 and stor3 + stor2 > stor1:
    print(f'трегольник со сторонами {stor1}, {stor2} и {stor3} существует')
else:
    print(f'трегольник со сторонами {stor1}, {stor2} и {stor3} не существует')

# задание 8 написать калькулятор
cal1 = float(input('введите первое число: '))
oper = input('введите необходимую операцию (+-*/): ')
cal2 = float(input('введите второе число: '))
if oper == '+':
    print(cal1 + cal2)
elif oper == '-':
    print(cal1 - cal2)
elif oper == '*':
    print(cal1 * cal2)
elif oper == '/':
    print(cal1 / cal2)
else:
    print('неверное выражение')

# задание 9 программа считывает строку и проверяет является ли она словом mister
prog = input('введите строку: ')
is_mister = (prog == 'mister')
print(is_mister)

# задание 10
# программа принимает на вход цвет доспехов и щита (red, yellow, black). тру если доспех не красный а щит черный
dos = str(input('введите цвет доспехов (red, yellow, black): '))
sht = str(input('введите цвет щита (red, yellow, black): '))
if dos != 'red' and sht == 'black':
    print(True)
else:
    print(False)

# дз
# задание 1 лотерея с выбором числа
# пользователь выйграет если совпадут 2 числа от 1 до 10 с 2 рандомами (как кено)
lot1 = int(input('введите первое число от 1 до 10: '))
lot2 = int(input('введите второе число от 1 до 10: '))
lot3 = random.randint(1, 10)
lot4 = random.randint(1, 10)
if lot1 == lot3 or lot1 == lot4 and lot2 == lot3 or lot2 == lot4:
    print(f'ваши числа {lot1} и {lot2} совпали с {lot3} и {lot4}. вы выйграли в лотерее!')
else:
    print(f'ваши числа {lot1} и {lot2} не совпали с {lot3} и {lot4}. вы не выйграли в лотерее!')

# задание 2 человек вводит день и месяц рождения а на вывод знак зодиака
date = int(input('укажите дату своего рождения: '))
month = int(input('введите цифру месяца своего рождения: '))
if 21 <= date <= 31 and month == 1 or 1 <= date <= 19 and month == 2:
    print('ваш знак зодиака - водолей')
elif 20 <= date <= 29 and month == 2 or 1 <= date <= 20 and month == 3:
    print('ваш знак зодиака - рыбы')
elif 21 <= date <= 31 and month == 3 or 1 <= date <= 20 and month == 4:
    print('ваш знак зодиака - овен')
elif 21 <= date <= 30 and month == 4 or 1 <= date <= 21 and month == 5:
    print('ваш знак зодиака - телец')
elif 22 <= date <= 31 and month == 5 or 1 <= date <= 21 and month == 6:
    print('ваш знак зодиака - близнецы')
elif 22 <= date <= 30 and month == 6 or 1 <= date <= 22 and month == 7:
    print('ваш знак зодиака - рак')
elif 23 <= date <= 31 and month == 7 or 1 <= date <= 21 and month == 8:
    print('ваш знак зодиака - лев')
elif 22 <= date <= 31 and month == 8 or 1 <= date <= 23 and month == 9:
    print('ваш знак зодиака - дева')
elif 24 <= date <= 30 and month == 9 or 1 <= date <= 23 and month == 10:
    print('ваш знак зодиака - весы')
elif 24 <= date <= 31 and month == 10 or 1 <= date <= 22 and month == 11:
    print('ваш знак зодиака - скорпион')
elif 23 <= date <= 30 and month == 11 or 1 <= date <= 22 and month == 12:
    print('ваш знак зодиака - стрелец')
elif 23 <= date <= 31 and month == 12 or 1 <= date <= 20 and month == 1:
    print('ваш знак зодиака - козерог')
else:
    print('введены неверные данные')
