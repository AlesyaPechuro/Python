import random

# задание 1 выводит четное или нечетное заданное число
num = int(input('введите целое число'))
if num % 2 == 0:  # если число четное
    print("число четное")
else:
    print('число нечетное ')

# задание 2 указывает название пальца руки по его номеру
finger = int(input('введите порядковый номер пальца руки: '))
if finger == 1:
    print('это большой палец')
elif finger == 2:
    print('это указательный палец')
elif finger == 3:
    print('это средний палец')
elif finger == 4:
    print('это безымянный палец')
elif finger == 5:
    print('это мизинец')
else:
    print('такого пальца нет')

# задание 3 указывает к какой поре года относится месяц по его номеру
month = int(input("введите порядковый номер месяца:"))
if month == 12 or month <= 2:
    print('зима')
elif 3 <= month <= 5:
    print('весна')
elif month >= 6 and month <= 8:
    print('лето')
elif month >= 9 and month <= 11:
    print('осень')
else:
    print('нет такого месяца')

# задание 4 выводит какое число больше из трех заданных
numbers1 = int(input(" введите 1 число :"))
numbers2 = int(input(" введите 2 число :"))
numbers3 = int(input(" введите 3 число :"))
if numbers1 > numbers2 and numbers1 > numbers3:
    print(f'число {numbers1} является наибольшим из трёх заданных')
elif numbers2 > numbers3 and numbers2 > numbers1:
    print(f'число {numbers2} является наибольшим из трёх заданных')
else:
    print(f'число {numbers3} является наибольшим из трёх заданных')

# задание 5 игра камень-ножницы-бумага
people = int(input('введите: 1-камень, 2-ножницы или 3-бумага: '))
comp = random.randint(1, 3)
if people == comp:
    print(f'{people} равен {comp}, а значит - ничья')
elif people > comp:
    print(f'{people} сильнее {comp}, а значит - вы выйграли')
else:
    print(f'{people} слабее {comp}, а значит - вы проиграли')

# задание 6 сравнение 2 переменных
per1 = int(input('введите 1 переменную: '))
per2 = int(input('введите 2 переменную: '))
per = per1 > per2
if per:
    print(True)
else:
    print(False)