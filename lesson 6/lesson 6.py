# задание 1 выводим квадрат чисел от 1 до 10
a = 0
while a <= 10:
    a += 1
    print(f'квадрат числа {a} равен', a ** 2)

# задача 2 найти произведение четных чисел от 0 до 125
sifra = 1
result = 1
while sifra != 125:
    sifra += 1
    if sifra % 2 == 0:
        result *= sifra
print(result)

# задание 3 вывести числа в порядке убывания от 1 до 15
b = 16
while b > 1:
    b -= 1
    print(b)

# задание 5 вывести последовательность в массив и указать его длинну
g = 0
arr = []
while g < 98:
    g += 7
    arr.append(g)
print(arr)
print(len(arr))