from unittest import result
import requests # нужна для работы с html запросами
from bs4 import BeautifulSoup as bs # нужна для извлечения данных из файлов HTML и XML
import csv
# import fake_useragent # имитация реального User-Agent браузера

# №1. АВТОРИЗАЦИЯ НА САЙТЕ

session = requests.Session()

auth_url = "http://snt.od.ua/"
#user = fake_useragent.UserAgent().random

real_header = {
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}
# fake_header = {
#     "user-agent": user
# }

data ={
 "user": "pechk.in.ua",
 "pass": "Pechkin2081",
 "login_submit": "Вход"
}

responce = session.post(auth_url, data=data, headers=real_header).text
# print(responce)

# №2. ИЗВЛЕЧЕНИЕ ДАННЫХ С САЙТА И СОХРАНЕНИЕ В ФАЙЛ

url = "http://snt.od.ua/ru/vnov.html?resPerPage=all"
my_request = session.get(url) # после авторизации меняем request на session
# print(my_request.text)

# <div class="top top_test"><p>040-01-57 Чашка цилиндр 330мл Черная</p>
soup = bs(my_request.text, "html.parser")
product_names = soup.find_all("div", class_="top top_test")
product_prices = soup.find_all("div", class_="bot bot_test")

for name in product_names:
	print(name.p.text)
for price in product_prices:
	print(price.p.text)
# AttributeError: 'NoneType' object has no attribute 'text'
# if:
# else:
		
# №3. СОХРАНЕНИЕ ДАННЫХ В ФАЙЛ

def save_file(items, path):
    with open(path, 'w',  encoding='utf8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['Имя', 'Базовая цена'])
        for item in items:
            writer.writerow([item['title'], item['cost']])





# while True:

# url = "http://snt.od.ua/ru/glavnaja/stranica-1.html"
# response = requests.get(url) # отправляем HTTP запрос и получаем результат
# soup = bs(response.text, "lxml") # созадаём переменную с классом beutifulsoup. 
# # в качестве параметров она принимает переменную с кодом response и библиотекой для парсинга lxml

# all_products = soup.find_all("p", class_="balance") # 1й аргумент - тег, 2й - класс. 
# # нижний слеш указываем, т.к. class - это ключевое зарезервированное слово
# print(all_products)
# #for item in all_products_available:


# print(response.text)

# new_products = soup.find_all("balance", class_="")
# for name in new_products:
#     print(name.a['title'])


# <p class="overflow text-muted add-top-sm cut-bottom">
# vacancies_info = soup.find_all('p', class_='overflow text-muted add-top-sm cut-bottom')
# for name in vacancies_names:
#     print('https://www.work.ua'+name.a['href'])
# for info in vacancies_info:
#     print(info.text)
