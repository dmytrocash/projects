import csv
from bottle import route, run

html_all_products = """
    <html> 
        <head>
            <style>
                body {{background-color: white;}}
                h1 {{color: black;}}
                p {{color: black;}}
            </style>
        </head>
        <body>
            <h1>Обожаю таблицы</h1>
            {}
        </body>
    </html>
"""

@route('/products')
def products():
    
    result = []
    with open('products.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            result.append(row)


    product_info_html = ''
    for item in result:
        
        product_info = f"""
        <table border="1">
                <tr><td width="550"><p>{item[0]}</p></td><td width="150"><p>{item[1]}</p></td></tr>
        </table>
        """
        product_info_html += product_info
    #print(product_info_html)
        
    return html_all_products.format(product_info_html)

run(host='localhost', port=8080)

