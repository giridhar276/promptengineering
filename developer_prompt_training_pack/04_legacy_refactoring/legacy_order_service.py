import sqlite3

def process_order(order_id, customer_id, product_id, quantity):
    conn = sqlite3.connect("orders.db")
    cur = conn.cursor()
    product = cur.execute(
        "select stock, price from products where product_id='" + product_id + "'"
    ).fetchone()
    if product == None:
        return "product missing"
    stock, price = product
    if quantity > stock:
        return "no stock"
    total = quantity * price
    cur.execute(
        "insert into orders values ('" + order_id + "','" + customer_id + "','" +
        product_id + "'," + str(quantity) + "," + str(total) + ")"
    )
    cur.execute(
        "update products set stock=" + str(stock - quantity) +
        " where product_id='" + product_id + "'"
    )
    conn.commit()
    conn.close()
    return total
