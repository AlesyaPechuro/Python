import sqlite3


# Создать 2 таблицы. Одна хранит текстовые данные, вторая - числовые (каждая по 1 колонке). Есть список из чисел и слов.
# Если элемент списка слово - записать в соответствующую таблицу, затем посчитать длину слова и записать во 2 таблицу.
# Если элемент списка число: если четное - записать в таблицу чисел, нечетное - слово "нечетное" в 1 таблицу.
# Если число записей во 2 таблице > 5 - удалить 1 запись в 1 таблице, если < 5 - обновить запись в 1 таблице на "hello"
conn = sqlite3.connect('homework.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS
                table_str(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                col_1 TEXT)''')  # 1 таблица, которая хранит текст

cursor.execute('''CREATE TABLE IF NOT EXISTS
                table_int(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                col_1 INTEGER)''')  # 2 таблица, которая хранит числа

list_ = [1, 5, 8, 'I', 'Love', 'Python', 10]
for i in list_:  # проходимся циклом по списку
    if type(i) == str:  # если элемент - строка
        cursor.execute('''INSERT INTO table_str(col_1) VALUES (?)''', (i,))  # записываем в текстовую таблицу
        length = len(i)  # находим длинну слова
        cursor.execute('''INSERT INTO table_int(col_1) VALUES (?)''', (length,))  # и записываем её в числовую таблицу
    else:  # иначе элемент - число
        if i % 2 == 0:  # если четное
            cursor.execute('''INSERT INTO table_int(col_1) VALUES (?)''', (i,))  # то добавляем в числовую таблицу
        else:  # иначе нечетное
            cursor.execute('''INSERT INTO table_str(col_1) VALUES ('нечетное')''')  # добавляем слово в текстовую табл.
conn.commit()  # сохраняем

cursor.execute('''SELECT * FROM table_int''')  # формируем список из кортежей значений из числовой таблицы
count_tab = cursor.fetchall()
print(count_tab)

if len(count_tab) > 5:  # если кортежей больше 5
    cursor.execute('''DELETE FROM table_str WHERE id=1''')  # удаляем 1 строку
elif len(count_tab) < 5:  # если кортежей меньше 5
    cursor.execute('''UPDATE table_str SET col_1='hello' WHERE id=1''')  # обновляем 1 строку
conn.commit()  # сохраняем

cursor.execute('''SELECT * FROM table_str''')
print(cursor.fetchall())
cursor.execute('''SELECT * FROM table_int''')
print(cursor.fetchall())
