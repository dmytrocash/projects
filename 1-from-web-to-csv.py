import requests # нужна для работы с html запросами
from bs4 import BeautifulSoup as bs # нужна для извлечения данных из файлов HTML и XML
import csv
from bottle import route, run

# №1. АВТОРИЗАЦИЯ НА САЙТЕ

session = requests.Session()

auth_url = "http://snt.od.ua/"

real_header = {
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

data ={
 "user": "pechk.in.ua",
 "pass": "Pechkin2081",
 "login_submit": "Вход"
}

responce = session.post(auth_url, data=data, headers=real_header).text
# print(responce)

# №2. ИЗВЛЕЧЕНИЕ ДАННЫХ С САЙТА

url = "http://snt.od.ua/ru/vnov.html?resPerPage=all"
my_request = session.get(url) # после авторизации меняем request на session
# print(my_request.text)

# <div class="top top_test"><p>040-01-57 Чашка цилиндр 330мл Черная</p>
soup = bs(my_request.text, "html.parser")
product_names = soup.find_all("div", class_="top top_test")
product_prices = soup.find_all("div", class_="bot bot_test")

name_result = []
for name in product_names:
    name_result.append(name.p.text)

price_result = []
for price in product_prices:
    if price.p is not None:
        price_result.append(price.p.text)
    else:
        price_result.append("None")

common_list = [list(x) for x in zip(name_result, price_result)]
# print(common_list)

# №3. СОХРАНЕНИЕ ДАННЫХ В ФАЙЛ
with open('products.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['Наименование товара', 'Оптовая цена'])
    for item in common_list:
        writer.writerow(item)

# №4. ВЫВЕСТИ ДАННЫЕ ИЗ ФАЙЛА CSV НА САЙТ
