import requests
import argparse
import lxml.html


metrex_site_url = 'https://metrex.kiev.ua'
currency_url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'


class Product:
    def __init__(self, product_title, product_price=None, product_id=None,
                 product_specifications=None):
        self.title = product_title
        self.price = product_price
        self.id = product_id
        self.specifications = product_specifications
        self.related = []

    def add(self, product):
        self.related.append(product)


class Currency:
    def __init__(self, url):
        self.url = url
        self.data = None

    def get_data(self):
        self.data = requests.get(self.url).json()

    def convert(self, to_currency, product_price):
        if to_currency == "uah":
            return "{} {}".format(product_price, to_currency.upper())
        for item in self.data:
            if item["cc"] == to_currency.upper():
                return "{} {}".format(round(product_price / item['rate'], 2),
                                      to_currency.upper())


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('product_id', type=str, help='Input product id')
    parser.add_argument('-p', '--price', action="store_true")
    parser.add_argument('-s', '--specifications', action="store_true")
    parser.add_argument('-r', '--related', default=0, type=int)
    parser.add_argument('-c', '--currency', default='uah', const='uah',
                        nargs='?', choices=['uah', 'usd', 'eur'])
    return parser.parse_args()


def get_search_url(product_id):
    return "{}/site_search?search_term={}".format(metrex_site_url, product_id)


def get_search_html(search_url):
    search_response = requests.get(search_url)
    return lxml.html.fromstring(search_response.text)


def get_product_url(search_html):
    return ''.join(search_html.xpath(
        '//div[@class="cs-product-gallery__title"]/a/@href'))


def get_product_html(product_url):
    product_response = requests.get(product_url)
    return lxml.html.fromstring(product_response.text)


def get_product_title(product_html):
    return ''.join(product_html.xpath('//h1/span/text()'))


def get_price(product_html):
    return float(''.join(product_html.xpath(
        '//p/span[@data-qaid="product_price"]/text()')).replace(',', '.'))


def get_product_specifications(product_html):
    unedited_specifications = product_html.xpath('//tr/td/text()')

    val = "\n"
    while val in unedited_specifications:
        unedited_specifications.remove("\n")

    edited_specifications = []
    for item in unedited_specifications:
        edited_specifications.append(
            item.replace('\n', '').replace('   ', '').replace('  ', ''))

    return ''.join(['    ' + edited_specifications[i] + ': '
                    + edited_specifications[i + 1]
                    + '\n' for i in range(0, len(edited_specifications), 2)])


def get_related_products_url(product_html):
    return metrex_site_url + ''.join(product_html.xpath(
        '//div[@data-qaid="related_products_block"]/@data-lazydiv-url'))


def get_product_id(product_html):
    return ''.join(product_html.xpath(
        '//span[@data-qaid="product_code"]/text()'))


def if_product_exists(search_html):
    if search_html.xpath('//h1/span[contains(text(),"0 наименований")]/text()'):
        return True
    else:
        return False


def get_product_info(product_url):
    product_html = get_product_html(product_url)
    product_title = get_product_title(product_html)
    product_price = get_price(product_html)
    product_id = get_product_id(product_html)
    product_specifications = get_product_specifications(product_html)
    product = Product(product_title, product_price, product_id,
                      product_specifications)

    return product, product_html


def get_related_products(output_related, product, product_html):
    related_products_url = get_related_products_url(product_html)
    related_product_html = get_product_html(related_products_url)
    related_urls = related_product_html.xpath(
        '//a[@class="cs-carousel__title"]/@href')

    related_products_urls = []
    for related_url in related_urls:
        related_product_url = metrex_site_url + related_url
        related_products_urls.append(related_product_url)
    selected_urls = related_products_urls[:output_related]

    for item in selected_urls:
        product_html = get_product_html(item)
        product_title = get_product_title(product_html)
        product_id = get_product_id(product_html)
        product_price = get_price(product_html)

        related_products = Product(product_title, product_price, product_id)
        product.add(related_products)

    return len(related_products_urls)


def output_products_info(output_price, output_related, output_specifications,
                         product, len_related_products, output_currency, currency):
    indent = '    '
    template = "{}{}: {}{}{}"
    print(template.format(indent, "Наименование", product.title, "", ""))
    print(template.format(indent, "Код товара", product.id, "", ""))
    if output_price:
        print(template.format(indent, "Цена", currency.convert(
            output_currency, product.price), "", ""))

    if output_specifications:
        print(template.format(indent, "Характеристики", "", "\n",
                              product.specifications))

    if output_related:
        print("{}{}".format(indent*2, "Сопутствующие товары:"))

        related_products_list = []
        for item in product.related:
            related_products_list.append(template.format(indent*2, "Наименование",
                                                         item.title, "", ""))
            related_products_list.append(template.format(indent*2, "Код товара",
                                                         item.id, "", ""))
            related_products_list.append(template.format(
                indent*2, "Цена", currency.convert(
                    output_currency, item.price), "", ""))

        print(*related_products_list, sep='\n')

    elif output_related > len_related_products:
        print("Подобных товаров меньше, чем {}. Чтобы посмотреть подобные "
              "товары, введите число от 1 до {} "
              "включительно.".format(output_related, len_related_products))


def main():
    args = get_arguments()
    output_price = args.price
    output_related = args.related
    output_specifications = args.specifications
    output_currency = args.currency

    currency = Currency(currency_url)
    currency.get_data()

    search_url = get_search_url(args.product_id)
    search_html = get_search_html(search_url)
    product_url = get_product_url(search_html)
    if product_url == '':
        print("Товар с таким артикулом не сущетвует!")
        return
    product, product_html = get_product_info(product_url)

    len_related_products = get_related_products(output_related, product,
                                                product_html)

    output_products_info(output_price, output_related, output_specifications,
                         product, len_related_products, output_currency, currency)


main()


# https://metrex.kiev.ua/site_search?search_term=10602
# https://metrex.kiev.ua/ua/p1489767212-samorez-dlya-profnastila.html

# cd /Users/dmytrocash/Desktop/code/projects-repo/metrex-site-parser/src

# python3 metrex-site-parser.py 10602 -p -s -r=2
# python3 metrex-site-parser.py 10602 -p -s -r=4 -c=uah
# python3 metrex-site-parser.py 10602 -p -s -r=7 -c=usd
# python3 metrex-site-parser.py 10602 -p -s -r=10 -c=eur

# python3 metrex-site-parser.py 6605 -p -s -r=3 -c=usd
