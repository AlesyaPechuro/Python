# задание 1 дан произвольный список .записать в обратном порядке

# вариант 1
spisok = [1, 2, 3, 4, 5]
spisok.reverse()
print(spisok)

# вариант 2]
spisok2 = [7, 8, 9, 10, 11]
print(spisok2[::-1])


# задание 2 есть список. найти значение 20 и если оно есть - заменить на 200. только первое вхождение
list = [10, 20, 30, 40, 20]  # задаем список
c = list.index(20)  # вводим переменную которая дает индекс числа 20 в списке
if 20 in list:  # если 20 есть в списке
    list[c] = 200  # меняем на 200 по индексу
print(list)


# задание 3 список из 7 цифр. если четных больше - найти сумму всех.иначе произведение 1 3 и 6
spis = [1, 5, 8, 9, 10, 16, 22]  # задаем список
chet = 0  # переменная для подсчета количества четных
nechet = 0  # переменная для подсчета количества нечетных
for i in spis:  # задаем цикл по списку
    if i % 2 == 0:  # если чсло из списка четное
        chet += 1  # то количество четных увеличивается
    else:
        nechet += 1  # иначе увеличивается количество нечетных
if chet > nechet:  # если четных больше чем нечетных
    print(f'четных больше! сумма всех чисел списка равна', sum(spis))
else:
    print(f'нечетных больше! произведение 1, 3 и 6 элемента равно', spis[1] * spis[3] * spis[6])


# задание 4 найти совпадающие элементы двух списков и их записать в новый список
# вариант 1
a = [5, [1, 2], 2, 'r', 4, 'ee']
b = [4, 'we', 'ee', 3, [1, 2]]
c = []  # задаем пустой список для добавления
for i in a:  # идем циклом по списку а
    if i in b:  # и проверяем есть ли такая переменная и в списке b
        c.append(i)  # если находим совпадение то добавляем в новый список
print(c)
# вариант 2
for i in a:
    if b.count(i) > 0:
        c.append(i)
# вариант 3
c = [i for i in a if i in b]  # добавляет i если она есть в списке а и списке б

# задание 5
h = [4, 6, 'py', 'tell', 78]
v = [44, 'hello', 56, 'exept', 3]
print(h + v)  # сложение 2 списков вариант 1
h.extend(v)  # сложение 2 списков вариант 2
print(h)
h.insert(3, 6)  # добавляем 6 на 3 позицию
print(len(h))  # считаем количество элементов в списке
for i in h:  # запускаем цикл по списку
    if isinstance(i, str):  # если цикл доходит до переменой с типом str
        h.remove(i)  # то эта переменная удаляется
print(h)


# дз
# Все числа этого списка проверить на чётность.
# Если число чётное, то посчитать сумму его цифр.
# Если нечётное, то заменить его на 1 в списке.
# Все слова: посчитать количество гласных и согласных.
# Вывести все на экран.

listik = [15, 48, 'hello', 6, 19, 'world']
print(f'исходный список {listik}')  # для нагляднсти выведем исходный список
glas = 0  # переменная для подчета гласных
soglas = 0  # переменная для подсчета согласных
for i in listik:  # задаем цикл для элементов из списка
    if isinstance(i, int):  # если элемент является числом
        if i % 2 == 0:  # и если это число четное
            print(f'число {i} - четное. сумма его цифр равна', i // 10 + i % 10)  # выводим сумму его цифр
        else:  # иначе, то есть число нечетное
            listik[listik.index(i)] = 1  # заменим его на 1
            print(f'число {i} - нечетное. заменим его на 1')
    elif isinstance(i, str):  # если элемент является строкой
        i = ''.join(i)  # разбиваю строку на отдельные буквы.
                        # можно было просто for x in list(i) то есть привести к типу данных список
        for x in i:  # прохожу циклом по каждой букве
            if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'y':  # если присутствуют гласные
                glas += 1  # добавляем +1 к счетчику гласных
            else:  # иначе - согласные
                soglas += 1  # добавляем +1 к счетчику согласных
print(f'новый список {listik}')
print(f'согласных букв в словах из списка - {glas}')
print(f'гласных букв в словах из списка - {soglas}')