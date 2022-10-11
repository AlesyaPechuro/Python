text1 = 'Fault, this, which pursue laborious pleasure exercise know complete how fault loves those from extremely - ' \
        'account right praising some toil occur, procure master who one builder will do avoids will dislikes are some' \
        ' but this obtain teachings of or teachings a occur circumstances trivial man all know there exercise except'

text2 = 'Открывший предаваться восхваляющих стремящегося потому избегал а счастливой - если иной стал раскрою людей ' \
        'раз обстоятельства несло счастливой всю истину избегал немалое предаваться пользы истину только наслаждению ' \
        'что: или поняли того отвергает было счастливой возжаждал наслаждение которое счастливой приносило избегал ' \
        'тех никаких и стремящегося отвергает стремящегося которого истину страдания лишь никого '

text1_ = list(text1)  # текст 1 приводим к списку
text1_set = set(text1_)  # делаем из текста множество чтобы убрать все повторы
text1__ = list(text1_set)  # делаем обратно список
text1__.sort()  # сортируем по алфавиту
for i in text1__:  # задаем цикл
    if 66 <= ord(i) <= 74 or 98 <= ord(i) <= 106:  # если переменная в пределах символов B и J
        print(i, end=' ')  # выводим ее

probel1 = 0  # задаем переменную для подсчета количества пробелов
for c in text1_:  # идем циклом по тексту
    if c == ' ':  # если переменная равно пробелу
        probel1 += 1  # то +1 к переменной
print(f'количество пробелов в английском тексте равно {probel1}')



# аналогичное проделываем с русским текстом
text2_ = list(text2)  # приводим к списку
text2_set = set(text2_)  # делаем множество чтобы убрать все повторы
text2__ = list(text2_set)  # делаем обратно списокм
text2__.sort()  # сортируем по алфавиту
for x in text2__:  # задаем цикл
    if 1043 <= ord(x) <= 1061 or 1075 <= ord(x) <= 1093:  # если переемнная в пределах от г до х
        print(x, end=' ')  # выводим ее

probel2 = 0
for z in text2_:
    if z == ' ':
        probel2 += 1
print(f'количество пробелов в русском тексте равно {probel2}')