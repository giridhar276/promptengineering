from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.get("/orders")
def orders():
    conn = sqlite3.connect("shop.db")
    customers = conn.execute("SELECT id, name FROM customers").fetchall()
    result = []
    for customer in customers:
        orders = conn.execute(
            "SELECT id, amount, created_at FROM orders WHERE customer_id = ?",
            (customer[0],)
        ).fetchall()
        result.append({"customer_id": customer[0], "customer_name": customer[1], "orders": orders})
    conn.close()
    return jsonify(result)
