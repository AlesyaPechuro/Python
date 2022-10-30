import csv

# работа с csv-файлом
exampleFile = open('example.csv', encoding='utf-8')  # открываем его
exampleReader = csv.reader(exampleFile, delimiter=';')  # читаем файл

for row in exampleReader:  # задаем цикл
    string = 'строка #' + str(exampleReader.line_num) + ' '  # чтобы выводилась строка №
    for value in row:
        string = string + value + ' '
    print(string)
exampleFile.close()

# запись в csv-файл
exampleFile2 = open('output.csv', 'w', encoding='utf-8', newline='')  # открываем файл, т.к его нет, то он создасться
exampleWriter = csv.writer(exampleFile2, delimiter=';')  # записыватель
exampleData = [['05.04.2015 13:34', 'Яблоки', '73'], ['05.04.2015 3:41', 'Вишни', '85']]  # указываем что записываем
for row in exampleData:
    exampleWriter.writerow(row)
exampleFile2.close()
