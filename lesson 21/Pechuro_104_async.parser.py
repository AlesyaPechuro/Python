from bs4 import BeautifulSoup
import json
import asyncio
import aiohttp

data = []


async def get_page_data(session, page):  # ф-ция по сбору данных
    url = f'https://cars.av.by/filter?brands[0][brand]=8&brands[0][model]=5865&brands[0][generation]=12687&page={page}&sort=4'

    async with session.get(url=url) as response:
        response_text = await response.text()

        soup = BeautifulSoup(response_text, 'lxml')

        cars = soup.find_all('div', class_='listing-item')  # находим блок с объявлением
        for car in cars:  # заходим в каждый и ищем нужную нам информацию
            link = 'https://cars.av.by' + car.find('a', class_='listing-item__link').get('href')  # находим ссылку

            price_byn = car.find('div', class_='listing-item__price').text.encode('ascii', errors='ignore').decode(
                'UTF-8')   # чтобы убрать скрытые символы

            price_usd = car.find('div', class_='listing-item__priceusd').text.encode('ascii', errors='ignore').decode(
                'UTF-8')

            info = car.find('div', class_='listing-item__params').text.encode('ascii', errors='ignore').decode(
                'UTF-8')

            data.append([price_usd, price_byn + 'p.', info, link])  # добавляем в список
        print(data)


async def gather_data():  # ф-ция для формирования необходимого списка задач

    async with aiohttp.ClientSession() as session:  # Создаем клиент-сессию для повторного исп. соединения
        tasks = []

        for page in range(1, 5):  # задаем цикл по страницам которых 4
            task = asyncio.create_task(get_page_data(session, page))
            # создаем задачу с параметрами - объект сессии и текущую страницу из цикла
            tasks.append(task)  # пополняем список задач

        await asyncio.gather(*tasks)
        # запускает на выполнение awaitable объекты, кот перечислены в последовательности с *


def main():
    asyncio.run(gather_data())
    with open('async_parser.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)


if __name__ == "__main__":
    main()
