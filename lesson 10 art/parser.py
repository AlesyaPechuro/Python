from bs4 import BeautifulSoup
import requests
import pandas as pd
import json


def parser():
    global data  # делаем переменную глобальной чтобы использовать в других функциях
    data = []  # делаем пустой список в который будем обавлять информацию
    # в качестве ссылки передаем страницу с уже заданным фильтром на бмв е60 что дало нам 4 страницы с машинами.
    # для этого задаем цикл чтобы зайти на каждую страницу
    for p in range(1, 5):
        website = requests.get(
            f'https://cars.av.by/filter?brands[0][brand]=8&brands[0][model]=5865&brands[0][generation]=12687&page={p}&sort=4')
        soup = BeautifulSoup(website.text, 'lxml')

        cars = soup.find_all('div', class_='listing-item')  # находим блок с объявлением
        for car in cars:  # заходим в каждый и ищем нужную нам информацию
            link = 'https://cars.av.by' + car.find('a', class_='listing-item__link').get('href')  # находим ссылку

            price_byn = car.find('div', class_='listing-item__price').text  # цена в бун
            new_price_byn = ''.join([b for b in price_byn if b.isdigit()])  # чтобы убрать скрытые символы

            price_usd = car.find('div', class_='listing-item__priceusd').text  # цена в долларах
            new_price_usd = ''.join([u for u in price_usd if u.isdigit()])

            info = car.find('div', class_='listing-item__params').text.replace('\xa0', '')  # информация
            new_info = info.replace('\u2009', '')  # также убираем скрытые символы

            data.append([new_price_usd + '$', new_price_byn + 'p.', new_info, link])  # добавляем в список
        print(data)


def writer_to_csv():  # записываем в табличный вариант
    header = ['ценв в usd', 'цена в byn', 'год выпуска/объем/тип двигателя/пробег', 'ссылка на авто']
    df = pd.DataFrame(data, columns=header)
    df.to_csv('C:\\Users\\by01.admin\\PycharmProjects\\lessons\\lesson 10 art\\parser.csv', sep=';', encoding='utf-8')


def writer_to_json():
    with open('parser.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)


parser()
writer_to_csv()
writer_to_json()
