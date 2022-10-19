# задача 1 в качестве аргумента принимается рост и вес. расчитывается индекс массы тела
def index():
    height = bool(input('введите свой рост в метрах: '))
    weight = bool(input('введите свой вес в килограммах : '))
    bmi = weight / height ** 2  # расчет индекса
    if bmi < 16:
        print('у вас выраженный дефицит массы тела')
    elif 16 <= bmi < 18.5:
        print('у вас недостаточная масса тела')
    elif 18.5 <= bmi < 25:
        print('у вас норма')
    elif 25 <= bmi < 30:
        print('у вас избытчная масса тела')
    elif 30 <= bmi < 35:
        print('у вас ожирение первой степени')
    elif 35 <= bmi < 40:
        print('у вас ожирение второй степени')
    elif 40 <= bmi:
        print('у вас ожирение третьей степени')
    else:
        print('вы ввели что-то неверно')


index()


# задача 2 определяется вид фигуры по кол-ву указанных сторон от 3 до 10
def figure():
    side = int(input('введите количество сторон: '))
    if side == 3:
        print('треугольник')
    elif side == 4:
        print('прямоугольник/квадрат/ромб/параллелограмм')
    elif side == 5:
        print('пятиугольник или пентагон')
    elif side == 6:
        print('шестиугольник или гексагон')
    elif side == 7:
        print('семиугольник или гептагон')
    elif side == 8:
        print('восьмиугольник или октагон')
    elif side == 9:
        print('девятиугольник')
    elif side == 10:
        print('десятиугольник или декагон')
    else:
        print('нет такой фигуры')


figure()


# задача 3 ф-ция принимает на вход дату и выводит следующую за ней дату
def data():
    date = int(input('введите день: '))
    month = str(input('введите месяц: '))
    year = int(input('введите год: '))
    all_month = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
                 'ноября', 'декабря']
    month_with_30_days = ['апреля', 'июня', 'сентября', 'ноября']
    month_with_31_days = ['января', 'марта', 'мая', 'июля', 'августа', 'октября']
    new_month = ''
    if date == 31 and month == 'декабря':  # условие для 31 декабря
        print('1 января', year + 1)
    if month == 'февраля':  # условие для февраля
        if date == 28 and year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  # если год високосный
            print('29 февраля', year)
        else:
            print('1 марта', year)
    if date == 30 and month in month_with_30_days or date == 31 and month in month_with_31_days:  # для последнего дня
        for index, value in enumerate(all_month):
            if value == month:
                new_month = all_month[index + 1]
        print('1', new_month, year)
    else:
        print(date + 1, month, year)


data()


# задача 4 интернет-магазин по доставке. первый заказ 10,95 а все последующие по 2,95
def delivery(oder):
    count = 0  # переменная для подсчета суммы заказа
    if oder == 1:
        print('сумма вашей доставки составляет 10,95$')
    else:
        count = 10.95 + (2.95 * (oder - 1))
        print(f'сумма вашей доставки составляет {count}$')


delivery(int(input('введите количество позиций в заказе: ')))


# задача 5 указываются числитель и знаменатель. надо максимально сократить дробь и вывести на экран
def fraction():
    numerator = int(input('введите числитель: '))
    denominator = int(input('введите знаменатель : '))
    spis_numerator = []  # список для добавления чисел на которые делится числитель
    spis_denominator = []  # список для добавления чисел на которые делится знаменатель
    for q in range(numerator, 1, -1):  # цикл в последовательности от числителя до 1
        if numerator % q == 0:  # если числитель делится на число без остатка
            spis_numerator.append(q)  # то это число добавлется в список
    for x in range(denominator, 1, -1):  # аналогично для знаменателя
        if denominator % x == 0:
            spis_denominator.append(x)
    for d in spis_numerator:  # затем проходимся циклом по списку чисел на которые делится числитель
        if d in spis_denominator:  # если это число так же присутствует и в списке на который делится знаменатель
            new_numerator = numerator / d  # то сокращаем дробь на это число
            new_denominator = denominator / d
            print(new_numerator, '/', new_denominator)


fraction()


# задача 6 подается список из 10 элементов
def ex_(list_):
    list_.reverse()
    print(f'1. список в перевернутом виде {list_}')
    list_s = []  # пустой список для создания нового из слов
    list_i = []  # пустой список для создания нового из чисел
    for g in list_:  # проходимся циклом по списку
        if type(g) == str:  # если элемент является строкой
            list_s.append(g)  # то добавляем его с список для строк
        else:
            list_i.append(g)  # иначе добавляем в список для чисел
    list_s.sort(reverse=True)
    list_i.sort(reverse=True)
    print(f'2. список в порядке убывания {list_s} {list_i}')
    list_s.sort()
    list_i.sort()
    print(f'3. список в порядке возрастания {list_s} {list_i}')
    print(f'4. срез списка от 2 до 7 элемента {list_[2:7]}')
    del list_[5]
    print(f'5. список c удаленным 5 элементом {list_}')
    list_ = set(list_)
    list_ = list(list_)
    print(f'6. список без дубликатов {list_}')
    print(f'7. список без чисел {list_s}')


ex_(['hi', 'hello', 456, 'world', 852, 'hi', 666, 999, 'buy', 5])


#  задача 7 фун-ция подсчитывает кол-во эл в списке значения кот >= заданному мин порогу и < макс порога
def countrange(number, min_, max_):
    count = 0
    for j in number:
        if min_ <= j < max_:
            count += 1
    print(count)


countrange([7, 11, 4, 6, 9, 22, 100], 5, 50)
countrange([7.8, 11, 27.6, 55, 14], 7, 30)


# задача  8 подается список. возвращается кол-во всех подсписков внутри этого списка
def sublist(list__):
    count_list = 0  # переменная для подсчета кол-ва списков
    for t in list__:  # проходимся циклом по списку
        if type(t) == list:  # если переменная ялвяется подсписком
            count_list += 1  # то подсчитываем количество
            print('[', count_list, ']', end='')
            sublist(t)


sublist([1, 2, 3, [4, 5, 6, [7, 8, 9, 10], [8, 7, 8]]])


# задача 9 анаграммы, т.е слов образованные путем взаимной перестановки букв
def anagrams():
    word1 = str(input('введите первое слово: '))
    word2 = str(input('введите второе слово: '))
    if sorted(list(word1)) == sorted(list(word2)):  # сортируем буквы в обоих словах
        print(f'слова {word1} и {word2} являются анаграммами')  # делаем сравнение строк
    else:
        print(f'слова {word1} и {word2} не являются анаграммами')


anagrams()


# задача 10 телефон
def mobile(text):
    dict_ = {1: ['.', ',', '?', '!', ':'],
             2: ['A', 'B', 'C'],
             3: ['D', 'E', 'F'],
             4: ['G', 'H', 'I'],
             5: ['J', 'K', 'L'],
             6: ['M', 'N', 'O'],
             7: ['P', 'Q', 'R', 'S'],
             8: ['T', 'U', 'V'],
             9: ['W', 'X', 'Y', 'Z'],
             0: ' '}
    for p in text.upper():  # идем сначала циклом по передоваемому тексту который сделали заглавными буквами
        for key, value in dict_.items():  # одновременно проходимся циклом по словарю
            for w in value:  # и проходимся циклом по значениям
                if p == w:  # если буква из текста совпадает с буквой из значения
                    print(str(key) * (value.index(w) + 1), end='')
                    # то выводит ключ в котором находится это значение умнож. на его индекс + 1 (т.к. начинается с 0)
                else:
                    continue  # если попадется то чего нет в словаре то просто его пропускает


mobile('Hello, world!')


# задача 11 выравнивание списка
def flattering(data_):
    if data_ == []:
        return data_
    if type(data_[0]) == list:
        return flattering(data_[0]) + flattering(data_[1:])
    return data_[:1] + flattering(data_[1:])


print(flattering([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))
