import csv
from bottle import route, run


html_template = """
    <html> 
        <head>
            <style>
                body {{background-color: black;}}
                h1 {{color: white;}}
                p {{color: white;}}
            </style>
        </head>
        <body>
            <h1><em>Product info:</em></h1>
            {} 
        </body>
    </html>
"""

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


def check_product(product_id, min, max):
    try:
        product_id = int(product_id)
    except ValueError as e:
        return "Error: product is not number"
    
    if min > product_id or product_id > max:
        return f"Error: product not in range {min} - {max}"


@route('/product/<product_id>')
def product_from_db(product_id):
    import sqlite3
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    cur.execute("select count(*) from product")  
    max = cur.fetchone()[0]
    print(max)
    min = 0
    error = check_product(product_id, min, max)
    
    if error:
        return html_template.format(f"<p>{error}</p>")
    row = int(product_id)
    print(row)
    
    # Get row from db
    product = get_product(product_id)
    print(product)

    # Return html_template with product's code and name
    product_info_html = f"""
    <p>Product code is: {product["code"]}</p> 
    <p>Product name is: {product["name"]}</p>
    <p>Product price is: {product["price"]}</p> 
    """

    return html_template.format(product_info_html)


@route('/products')
def products():
    import sqlite3
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    cur.execute("select id, name from product")
    result = cur.fetchall()
    print(result)
    # result = [(1, 'Cup'), (2, 'Plate'), (3, 'Jar'), (4, 'Wineglass')]

    product_info_html = ''
    for item in result:
        
        products_id_with_name = f"""
        <p><a href="http://localhost:8080/product/{item[0]}">{item[0]}.{item[1]}</a></p>
        """
        product_info_html += products_id_with_name
    print(product_info_html)

    con.close()
    return html_all_products.format(product_info_html)


def get_product(product_id):
    # Create DB connection
    import sqlite3
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    cur.execute("select code, name, price from product where id=:id", {"id": product_id})
    result = cur.fetchall()
    # result = [('1011', 'Plate', '300')]

    product_code_value = result[0][0]
    product_name_value = result[0][1]
    product_price_value = result[0][2]

    # Close DB connection
    con.close()

    return {"code": product_code_value, "name": product_name_value, "price": product_price_value}


# Run webserver
run(host='localhost', port=8080)
