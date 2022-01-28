import csv
from bottle import route, run

html_all_products = """
    <html> 
        <head>
            <style>
                body {{background-color: black;}}
                h1 {{color: white;}}
                p {{color: white;}}
            </style>
        </head>
        <body>
            <h1>Products list:</h1>
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
        <p>{item[0]} - {item[1]}</p>
        """
        product_info_html += product_info
    print(product_info_html)
        
    return html_all_products.format(product_info_html)

run(host='localhost', port=8080)

