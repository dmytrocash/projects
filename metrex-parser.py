import requests
import argparse
import lxml.html


parser = argparse.ArgumentParser()
parser.add_argument('product_id', type=str, help='Input product id')
parser.add_argument('-p', '--price', action="store_true")
parser.add_argument('-s', '--specifications', action="store_true")
parser.add_argument('-r', '--related', default=0, type=int)
parser.add_argument('-c', '--currency', default='uah', const='uah', nargs='?', choices=['uah', 'usd', 'eur'])
args = parser.parse_args()


url = 'https://metrex.kiev.ua/ua/site_search?search_term=' + args.product_id
page = requests.get(url)
root = lxml.html.fromstring(page.text)
title = root.xpath('//h1/span[contains(text(),"0 наименований")]/text()') 
if title:
    print("Товара с таким артикулом не сущетвует!")
else:
    print("Товар с таким артикулом сущетвует!")
    

    product_link = root.xpath('//div[@class="cs-product-gallery__title"]/a/@href')
    new_link = ''.join(product_link)
    product_page = requests.get(new_link)
    product_root = lxml.html.fromstring(product_page.text)
    product_title = product_root.xpath('//h1/span/text()')
    new_title = ''.join(product_title)
    
    print(f"Наименование: {new_title}")


    if args.price:
        product_price = product_root.xpath('//p/span[@data-qaid="product_price"]/text()')
        new_price = float(''.join(product_price).replace(',','.')) 
        
        if args.currency:
            c = args.currency
            url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
            
            if c == 'usd':
                response = requests.get(url).json()
                for currency in response:
                    if currency["cc"] == "USD":
                        usd_rate = currency['rate']
                usd = new_price/usd_rate

                print(f"Цена: {round(usd, 2)} {c}")
            elif c == 'eur':
                response = requests.get(url).json()
                for currency in response:
                    if currency["cc"] == "EUR":
                        eur_rate = currency['rate']
                eur = new_price/eur_rate

                print(f"Цена: {round(eur, 2)} {c}")
            else:
                print(f"Цена: {round(new_price, 2)} {c}")

    
    if args.specifications:
        list = product_root.xpath('//tr/td/text()')
        
        val = "\n"
        while val in list:
            list.remove("\n")

        newlist1 = []
        for item in list:
            newlist1.append(item.replace('\n',''))

        newlist2 = []
        for item in newlist1:
            newlist2.append(item.replace('   ',''))

        newlist3 = []
        for item in newlist2:
            newlist3.append(item.replace('  ',''))

        product_specifications = ['    ' + newlist3[i] + ': ' + newlist3[i+1] + '\n' for i in range(0,len(newlist3),2)]
        print(f"Характеристики:\n{''.join(product_specifications)}")


    if args.related:
        r = args.related
        
        related_products_url = 'https://metrex.kiev.ua/related_slider_block_html?product_id=1489767212&page_type=cs_product_view'
        related_page = requests.get(related_products_url)
        related_root = lxml.html.fromstring(related_page.text)
        related_links = related_root.xpath('//a[@class="cs-carousel__title"]/@href')
        
        new_list = []
        for link in related_links:
            new_link = 'https://metrex.kiev.ua' + link
            new_list.append(new_link)

        if r > len(new_list):
            print(f"Подобных товаров меньше, чем {r}. Чтобы посмотреть подобные товары, введите число от 1 до {len(new_list)} включительно.")
        else:
            print(f"Сопутствующие товары:")
            
            selected_products = new_list[:r]
            related_products_list = []
            for product in selected_products:
                new_link = ''.join(product)
                product_page = requests.get(new_link)
                product_root = lxml.html.fromstring(product_page.text)

                product_title = ''.join(product_root.xpath('//h1/span/text()'))
                product_code = ''.join(product_root.xpath('//span[@data-qaid="product_code"]/text()'))
                product_price = float(''.join(product_root.xpath('//p/span[@data-qaid="product_price"]/text()')).replace(',','.'))
                ''.join(product_title)
                related_products_list.append(f'  - Название: {product_title}')
                related_products_list.append(f'    Код товара: {product_code}')

                
                if args.currency:
                    c = args.currency
                    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'

                    if c == 'usd':
                        response = requests.get(url).json()
                        for currency in response:
                            if currency["cc"] == "USD":
                                usd_rate = currency['rate']
                        usd = product_price/usd_rate

                        related_products_list.append(f'    Цена: {round(usd, 2)} {c}')
                    elif c == 'eur':
                        response = requests.get(url).json()
                        for currency in response:
                            if currency["cc"] == "EUR":
                                eur_rate = currency['rate']
                        eur = product_price/eur_rate

                        related_products_list.append(f'    Цена: {round(eur, 2)} {c}')
                    else:
                        related_products_list.append(f'    Цена: {round(product_price, 2)} {c}')

            print(*related_products_list, sep='\n')

# cd /Users/dmytrocash/Desktop/code/

# https://metrex.kiev.ua/site_search?search_term=10602
# https://metrex.kiev.ua/ua/p1489767212-samorez-dlya-profnastila.html

# python3 metrex-parser.py 10602 -p -s -r=2
# python3 metrex-parser.py 10602 -p -s -r=4 -c=uah
# python3 metrex-parser.py 10602 -p -s -r=7 -c=usd
# python3 metrex-parser.py 10602 -p -s -r=10 -c=eur
 
