import requests
import argparse
import lxml.html


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('product_id', type=str, help='Input product id')
    parser.add_argument('-p', '--price', action="store_true")
    parser.add_argument('-s', '--specifications', action="store_true")
    parser.add_argument('-r', '--related', default=0, type=int)
    parser.add_argument('-c', '--currency', default='uah', const='uah', nargs='?', choices=['uah', 'usd', 'eur'])
    return parser.parse_args()


args = get_arguments()


metrex_site_url = 'https://metrex.kiev.ua'
currency_url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'


def get_search_url(any_product_id):
    return metrex_site_url + '/site_search?search_term=' + any_product_id  # .format


search_url = get_search_url(args.product_id)


def get_search_html(any_search_url):
    search_response = requests.get(any_search_url)
    return lxml.html.fromstring(search_response.text)


search_html = get_search_html(search_url)


def get_product_url(any_search_html):
    return ''.join(any_search_html.xpath('//div[@class="cs-product-gallery__title"]/a/@href'))


product_url = get_product_url(search_html)


def get_product_html(any_product_url):
    product_response = requests.get(any_product_url)
    return lxml.html.fromstring(product_response.text)


product_html = get_product_html(product_url)


def get_product_title(any_product_html):
    return ''.join(any_product_html.xpath('//h1/span/text()'))


product_title = get_product_title(product_html)


def get_price(any_product_html):
    return float(''.join(any_product_html.xpath('//p/span[@data-qaid="product_price"]/text()')).replace(',', '.'))


product_price = get_price(product_html)


def currency_converter(any_currency):
    currency_response = requests.get(currency_url).json()
    for currency in currency_response:
        if currency["cc"] == any_currency:
            return product_price / currency['rate']


def get_product_specifications(any_product_html):
    unedited_specifications = any_product_html.xpath('//tr/td/text()')

    val = "\n"
    while val in unedited_specifications:
        unedited_specifications.remove("\n")

    edited_specifications = []
    for item in unedited_specifications:
        edited_specifications.append(item.replace('\n', '').replace('   ', '').replace('  ', ''))  # найти более удобный метод строки

    return ''.join(['    ' + edited_specifications[i] + ': ' + edited_specifications[i + 1] + '\n' for i in range(0, len(edited_specifications), 2)])


product_specifications = get_product_specifications(product_html)


def get_related_products_url(any_product_html):
    return metrex_site_url + ''.join(product_html.xpath('//div[@data-qaid="related_products_block"]/@data-lazydiv-url'))


related_products_url = get_related_products_url(product_html)


def get_product_id(any_product_html):
    return ''.join(any_product_html.xpath('//span[@data-qaid="product_code"]/text()'))


product_check = product_html.xpath('//h1/span[contains(text(),"0 наименований")]/text()')
if product_check:
    print("Товара с таким артикулом не сущетвует!")
else:
    print(f"Наименование: {product_title}")

    if args.price:
        if args.currency == 'uah':
            print(f"Цена: {round(product_price, 2)} {args.currency.upper()}")
        else:
            rate = currency_converter(args.currency.upper())
            print(f"Цена: {round(rate, 2)} {args.currency.upper()}")

    if args.specifications:
        print(f"Характеристики:\n{product_specifications}")

    if args.related:
        related_product_html = get_product_html(related_products_url)
        related_urls = related_product_html.xpath('//a[@class="cs-carousel__title"]/@href')

        related_products_urls = []
        for url in related_urls:
            related_product_url = 'https://metrex.kiev.ua' + url
            related_products_urls.append(related_product_url)

        if args.related > len(related_products_urls):
            print(f"Подобных товаров меньше, чем {args.related}. Чтобы посмотреть подобные товары, введите число от 1 до {len(new_list)} включительно.")
        else:
            print(f"Сопутствующие товары:")

            selected_products = related_products_urls[:args.related]

            related_products_list = []
            for product in selected_products:
                related_product_html = get_product_html(''.join(product))
                related_product_title = get_product_title(related_product_html)
                related_product_id = get_product_id(related_product_html)
                related_product_price = get_price(related_product_html)

                related_products_list.append(f'  - Название: {related_product_title}')
                related_products_list.append(f'    Код товара: {related_product_id}')

                if args.currency == 'uah':
                    related_products_list.append(f'    Цена: {round(related_product_price, 2)} {args.currency.upper()}')
                else:
                    rate = currency_converter(args.currency.upper())
                    related_products_list.append(f'    Цена: {round(rate, 2)} {args.currency.upper()}')

        print(*related_products_list, sep='\n')


# cd /Users/dmytrocash/Desktop/code/playground

# https://metrex.kiev.ua/site_search?search_term=10602
# https://metrex.kiev.ua/ua/p1489767212-samorez-dlya-profnastila.html

# python3 metrex-parser.py 10602 -p -s -r=2
# python3 metrex-parser.py 10602 -p -s -r=4 -c=uah
# python3 metrex-parser.py 10602 -p -s -r=7 -c=usd
# python3 metrex-parser.py 10602 -p -s -r=10 -c=eur

# - def product_info():
# все данные о запрашиваемом товаре (ничего не возвращает)
# - def if_product_exists(root)
# return True or False
# - def tsar_function(product_id):
# отвечает за сбор всех данных
# return Product()
# - class Product():
# title =
# price =
# id =
# specifications =
# related_products = [Product]
# - class Currency():
