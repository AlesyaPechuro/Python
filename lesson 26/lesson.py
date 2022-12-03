import sqlite3

# создаем бд, если такой нет то создается автоматически
conn = sqlite3.connect('name.db')
# создаем объект курсор который позволяет взаимодействовать и добавлять записи в бд
cursor = conn.cursor()
# создаем таблицу с названием таб1, поле айди для связи между таблицами и двумя текстовыми колонками
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS 
    tab_1(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        col_1 TEXT, 
        col_2 TEXT
    )''')
# вставляем значения в таблицу
cursor.execute('''
    INSERT INTO tab_1(col_1, col_2)
    VALUES('hello', 'world')''')
# сохраняем изменения
conn.commit()

# создаем еще одну таблицу
cursor.execute('''
    CREATE TABLE IF NOT EXISTS 
    tab_2(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        col_1 TEXT, 
        col_2 TEXT
    )''')

# пример заполнения таблицы
var1 = 'red'
var2 = 'black'

cursor.execute('''
    INSERT INTO tab_2(col_1, col_2)
    VALUES(?,?)
    ''', (var1, var2))

# через генератор
command = '''
    INSERT INTO tab_2(col_1, col_2)
    VALUES(?,?)
    '''

data_list = [('yellow', 'white') for x in range(10)]  # список из 10 значений

for tuple_ in data_list:
    cursor.execute(command, tuple_)  # передаем команду и кортеж

conn.commit()  # сохраняем изменения

# достаем все значения из таблицы
cursor.execute('''SELECT * FROM tab_2''')
print(cursor.fetchall())


# задание: создайте 10 различных записей в таблицу 1
for i in range(10):
    col_1_inp = input('введите значение для колонки col_1: ')
    col_2_inp = input('введите значение для колонки col_2: ')
    cursor.execute('''
    INSERT INTO tab_1(col_1, col_2)
    VALUES(?,?)
    ''', (col_1_inp, col_2_inp))

conn.commit()


# выберет все значения, где имя колонки Hello
cursor.execute('''SELECT * FROM tab_1 WHERE col_1 = 'hello' ''')
print(cursor.fetchall())

# выберет все значения отсортировав по колонке 2
cursor.execute('''SELECT * FROM tab_1 ORDERED BY col_2 ''')

# выберет данные только по указанной колонке
cursor.execute('''SELECT col_2 FROM tab_1 ''')
cursor.execute('''SELECT id, col_2 FROM tab_1 ORDERED BY col_2 ''')

# выберет данные, где в колонке есть слово world, но мы не помним первую и последнюю букву
cursor.execute('''SELECT col_2 FROM tab_1 WHERE col_2 LIKE '%orl%' ''')
s = cursor.fetchall()
print(s)

# удаление
cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
cursor.execute('''DELETE FROM tab_1 WHERE col_1 = 'red' ''')

# обновление
t = 3
cursor.execute('''UPDATE tab_1 SET col_1='world' WHERE id=?''', (t,))
conn.commit()