# задание 6 таблица умножения от 1 до 9

for i in range(1, 10):
    print('таблица умножения для', i)
    for l in range(1, 11):
        print('на', l, 'равно', i * l)

# дз
# задание 1 перемножить все нечетные значения в диапазоне от 1 до 100
pr = 1
for h in range(1, 101):
    if h % 2 == 1:
        pr *= h
print(pr)

# задание 2 записать в массив все числа в диапазоне от 1 до 500 кратные 5
mas = []
for x in range(1, 501):
    if x % 5 == 0:
        mas.append(x)
print(mas)

# задание 3 вывести на экран все четные значения от 1 до 497
for f in range(1, 497):
    if f % 2 == 0:
        print(f)

# задание 4 дан массив. если число встречается более 2 раз то добавить его в нов массив
arr = [3, 7, 10, 3, 5, 10, 7, 11, 14, 15, 20]
arr2 = []
for v in arr:
    if arr.count(v) >= 2:
        arr2.append(v)
print(arr2)
