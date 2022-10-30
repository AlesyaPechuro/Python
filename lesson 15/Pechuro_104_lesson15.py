import json


# задание 1 пользователь вводит название и стоимость покупки за день пока не напишет стоп. запистаь в json
def daily_shopping():
    dict_ = {}  # создаем пустой словарь
    while True:  # задаем цикл
        name_shop = input('введите название своей покупки (или stop для прекращения): ')
        if name_shop == 'stop':  # если стоп то цикл завершится
            break

        cost_shop = int(input('введите стоимость своей покупки: '))
        dict_.setdefault(name_shop, cost_shop)  # добавляем в словарь ключ - название, значение - цена

        with open('data.json', 'w', encoding='utf-8') as file:  # записываем в json
            json.dump(dict_, file, ensure_ascii=False)


daily_shopping()


# задание 2 прочитать файл из пред задания и вывести стоимость всех покупок за день
def sum_of_daily_shopping():
    with open('data.json', encoding='utf-8') as file_:
        data = json.load(file_)
        print(f'стоимость всех покупок за день составила {sum(data.values())}')


sum_of_daily_shopping()
