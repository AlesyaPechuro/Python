from bs4 import BeautifulSoup
import requests

website = requests.get('https://cars.av.by/filter?brands[0][brand]=8&brands[0][model]=5865&brands[0][generation]=4441')
soup = BeautifulSoup(website.text, 'lxml')
car = soup.find_all('div', class_='listing-item__wrap')
print(car)
for i in car:
    ssilka = car.find('a', class_='listing-item__link')
    info = car.find('div', class_='listing-item__params')
    price = car.find('div', class_='listing-item__prices')

print(ssilka)