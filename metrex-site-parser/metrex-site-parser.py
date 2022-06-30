import requests
import argparse
import lxml.html


metrex_site_url = 'https://metrex.kiev.ua'
currency_url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'


class Product:
    def __init__(self, product_title, product_price=None, product_id=None, product_specifications=None):  # ?? related
        self.title = product_title
        self.price = product_price
        self.id = product_id
        self.specifications = product_specifications
        self.related = [Product()]


# class Currency:


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('product_id', type=str, help='Input product id')
    parser.add_argument('-p', '--price', action="store_true")
    parser.add_argument('-s', '--specifications', action="store_true")
    parser.add_argument('-r', '--related', default=0, type=int)
    parser.add_argument('-c', '--currency', default='uah', const='uah', nargs='?', choices=['uah', 'usd', 'eur'])
    return parser.parse_args()


def get_search_url(product_id):
    return "{}/site_search?search_term={}".format(metrex_site_url, product_id)


def get_search_html(search_url):
    search_response = requests.get(search_url)
    return lxml.html.fromstring(search_response.text)


def get_product_url(search_html):
    return ''.join(search_html.xpath('//div[@class="cs-product-gallery__title"]/a/@href'))


def get_product_html(product_url):
    product_response = requests.get(product_url)
    return lxml.html.fromstring(product_response.text)


def get_product_title(product_html):
    return ''.join(product_html.xpath('//h1/span/text()'))


def get_price(product_html):
    return float(''.join(product_html.xpath('//p/span[@data-qaid="product_price"]/text()')).replace(',', '.'))


def currency_converter(currency_code, product_price):
    currency_response = requests.get(currency_url).json()
    for item in currency_response:
        if item["cc"] == currency_code:
            return product_price / item['rate']


def get_product_specifications(product_html):
    unedited_specifications = product_html.xpath('//tr/td/text()')

    val = "\n"
    while val in unedited_specifications:
        unedited_specifications.remove("\n")

    edited_specifications = []
    for item in unedited_specifications:
        edited_specifications.append(item.replace('\n', '').replace('   ', '').replace('  ', ''))

    return ''.join(['    ' + edited_specifications[i] + ': ' + edited_specifications[i + 1] + '\n' for i in range(0, len(edited_specifications), 2)])


def get_related_products_url(product_html):
    return metrex_site_url + ''.join(product_html.xpath('//div[@data-qaid="related_products_block"]/@data-lazydiv-url'))


def get_product_id(product_html):
    return ''.join(product_html.xpath('//span[@data-qaid="product_code"]/text()'))


def if_product_exists(search_html):
    if search_html.xpath('//h1/span[contains(text(),"0 наименований")]/text()'):
        return False
    else:
        return True


def get_info():
    # отвечает за сбор всех данных товара
    search_url = get_search_url(args.product_id)
    search_html = get_search_html(search_url)
    product_url = get_product_url(search_html)
    product_html = get_product_html(product_url)
    product_title = get_product_title(product_html)
    product_id = get_product_id(product_html)
    product_price = get_price(product_html)
    product_specifications = get_product_specifications(product_html)
    related_products_url = get_related_products_url(product_html)  # ?? not used
    product = Product(product_title, product_price, product_id, product_specifications)  # ?? related
    related_product_html = get_product_html(related_products_url)
    related_urls = related_product_html.xpath('//a[@class="cs-carousel__title"]/@href')
    related_products_urls = []
    for related_url in related_urls:
        related_product_url = metrex_site_url + related_url
        related_products_urls.append(related_product_url)


# get_info()


def main(product_check, product_title, search_html):
    args = get_arguments()
    if product_check:
        product_check = if_product_exists(search_html)  # ?? not used
        return print("Товара с таким артикулом не сущетвует!")
    else:
        print(f"Наименование: {product_title}")



# main()


def product_info(args, product_price, product_specifications, related_products_urls):
    if args.price:
        if args.currency == 'uah':
            print(f"Цена: {round(product_price, 2)} {args.currency.upper()}")
        else:
            print(f"Цена: {round(currency_converter(args.currency.upper()), 2)} {args.currency.upper()}")

    if args.specifications:
        print(f"Характеристики:\n{product_specifications}")

    if args.related > len(related_products_urls):
        print(f"Подобных товаров меньше, чем {args.related}. Чтобы посмотреть подобные товары, введите число от 1 до {len(related_products_urls)} включительно.")
        # вывести все сопутствующие товары, которые есть
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


product_info()


# cd /Users/dmytrocash/Desktop/code/playground

# https://metrex.kiev.ua/site_search?search_term=10602
# https://metrex.kiev.ua/ua/p1489767212-samorez-dlya-profnastila.html

# python3 metrex-site-parser.py 10602 -p -s -r=2
# python3 metrex-site-parser.py 10602 -p -s -r=4 -c=uah
# python3 metrex-site-parser.py 10602 -p -s -r=7 -c=usd
# python3 metrex-site-parser.py 10602 -p -s -r=10 -c=eur




