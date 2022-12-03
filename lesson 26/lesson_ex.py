import sqlite3
import random

conn = sqlite3.connect('lesson.db')
cursor = conn.cursor()

# Задание 1 создать базу. Создать таблицу с 3 полями: 2 текстовых и 1 целое число с клавиатуры,
# а слова статически. Выведите каждую запись в отдельную сроку
cursor.execute('''CREATE TABLE IF NOT EXISTS
                table1(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                col_1 TEXT,
                col_2 TEXT,
                col_3 INTEGER)''')  # создали базу с 3 колонками

text1 = 'hello'  # добавляем текст для первой колонки
text2 = 'hi'  # добавляем текст для второй колонки
text3 = input('введите число: ')  # для третьей колонки вводится число с клавиатуры

cursor.execute('''INSERT INTO table1(col_1, col_2, col_3)
                VALUES(?,?,?)''', (text1, text2, text3))  # добавляем записи в колонки
conn.commit()  # сохраняем

cursor.execute('''SELECT * FROM table1''')  # делаем выборку всех записей из таблицы
print(cursor.fetchall())  # выводим выборку


# Задание 2 создать базу. Поля: id, 2 целочисленных поля. Поля заполняются рандомно от 0 до 9. посчитать ср.арифмет.
# Если > кол-ва записей в бд, то удалить 4 запись
cursor.execute('''CREATE TABLE IF NOT EXISTS
                table2(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                col_1 INTEGER,
                col_2 INTEGER)''')  # создаем таблицу

cursor.execute('''INSERT INTO table2(col_1, col_2)
                    VALUES(?,?)''', (random.randint(0, 9), random.randint(0, 9)))  # заполняем колонки рандомно
conn.commit()  # сохраняем

cursor.execute('''SELECT col_1, col_2 FROM table2''')  # выбираем значение 2 колонок
colum = cursor.fetchall()  # задаем их в переменную
print(colum)
sum_ = 0  # задаем переменную для подсчета суммы
for i in colum:  # заходим циклом в список кортежей
    for f in i:  # проходимся по каждому элементу кортежа
        sum_ += f  # и суммируем их
avg = sum_ / (len(colum) * 2)  # находим среднее арифметическое двух колонок
print(avg)
if avg > len(colum):  # если оно больше чем кол-во строк в таблице
    cursor.execute('''DELETE FROM table2 WHERE id=4''')  # то удаляем 4 строку
conn.commit()  # сохраняем

# Задание 3 создать базу. Поля: id, 2 целочисленных поля. Поля заполняются рандомно от 0 до 9. Выбрать случайную запись.
# Если каждое число в ней четное, то удалить запись, если нечетное, то обновить данные на (2, 2)
cursor.execute('''CREATE TABLE IF NOT EXISTS
                table3(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                col_1 INTEGER,
                col_2 INTEGER)''')  # создаем таблицу

x = random.randint(0, 9)
y = random.randint(0, 9)
cursor.execute('''INSERT INTO table3(col_1, col_2)
                    VALUES(?,?)''', (x, y))  # заполняем колонки рандомно
# conn.commit()  # сохраняем

cursor.execute('''SELECT id FROM table3''')  # выбираем значение по айди
s = cursor.fetchall()  # записываем в переменную
r_id = random.choice(s)  # выбираем рандомно айди
cursor.execute('''SELECT col_1, col_2 FROM table3 WHERE id=?''', (r_id,))  # выбираем значение с рандомной строки
h = cursor.fetchall()
print(h)
even = []  # создаем список для четных
not_even = []  # создаем список для нечетных
for g in h:  # заходим циклом в список кортежей
    for i in g:  # берем каждый элемент кортежа
        if i % 2 == 0:  # если он четный
            even.append(i)  # то добавляем в список для четных
        else:
            not_even.append(i)  # иначе добавляем в список для нечетных
if len(even) == 2:  # если в списке четных два числа (то-есть оба оказались четными)
    cursor.execute('''DELETE FROM table3 WHERE id=?''', (r_id,))  # удаляем эту строку
    conn.commit()
elif len(not_even) == 2:  # если оба оказались нечетными
    cursor.execute('''UPDATE table3 SET col_1=2, col_2=2 WHERE id=?''', (r_id,))  # то обновляем эту строку
    conn.commit()
else:
    print('одно число четное а второе нечетное')  # иначе
cursor.execute('''SELECT * FROM table3 ''')
h = cursor.fetchall()
print(h)

# Задание 4. Создайте метод класса для работы с бд. Если передан 1 аргумент - то вставить запись с числом 3, если 2 -
# проверить является ли 2 числом. Если да, то удалить 1 запись. Если переданы 2 неизвестных, а 3 число - то обновить
# запись 3 на число 77
cursor.execute('''CREATE TABLE IF NOT EXISTS
                table4(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                col_1 INTEGER)''')
conn.commit()  # сохраняем изменения
cursor.execute('''SELECT * FROM table4''')
s = cursor.fetchall()  # формируем список со значениями


class Bd:  # объявляем класс
    def fill(self, a=None, b=None, c=None):  # создаем метод для объектов класса принимающий три значения
        if a is not None and b is None and c is None:  # если передаем одно значение выполняем следующий блок кода
            cursor.execute('''INSERT INTO table4(col_1) VALUES(3)''')  # добавляем запись со значением 3
            conn.commit()  # сохраняем изменения
        elif a is not None and type(b) == int and c is None:  # если передаем два значения и второе является числом
            cursor.execute('''DELETE FROM table4 WHERE id=1''')  # удаляем из таблицы первую запись
            conn.commit()  # сохраняем изменения
        elif a is not None and b is not None and type(c) == int:  # если передаем три значения и третье является числом
            cursor.execute('''UPDATE table4 SET col_1=77 WHERE id=3''')  # меняем значение в третьей записи
            conn.commit()  # сохраняем изменения


new_bd = Bd()  # создаем объект класса
new_bd.fill(a='1', b=5, c=10)  # вызываем метод экземпляра класса и передаем три значения
cursor.execute('''SELECT * FROM table4''')  # получаем информацию из таблицы
v = cursor.fetchall()  # формируем список с информацией из таблицы
print(v)  # вывод информации


# Задание 5. 3 колонки(id, text, text). заполнить данными (3 записи). Удалить 2 запись. Обновить 3 колонку
cursor.execute('''CREATE TABLE IF NOT EXISTS
                table5(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                col_1 TEXT,
                col_2 TEXT)''')
for _ in range(3):
    col_1 = input('введите слово 1: ')
    col_2 = input('введите слово 2: ')
    cursor.execute('''INSERT INTO table5(col_1, col_2)
                    VALUES(?,?)''', (col_1, col_2))
    conn.commit()
cursor.execute('''SELECT * FROM table5''')
z = cursor.fetchall()
print(z)
cursor.execute('''DELETE FROM table5 WHERE id=2''')
cursor.execute('''UPDATE table5 SET col_1='hello', col_2='world' WHERE id=3''')
conn.commit()
cursor.execute('''SELECT * FROM table5''')
z = cursor.fetchall()
print(z)
