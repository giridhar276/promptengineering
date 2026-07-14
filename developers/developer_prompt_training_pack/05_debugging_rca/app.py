from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.get("/balance/<account_id>")
def balance(account_id):
    conn = sqlite3.connect("bank.db")
    row = conn.execute(
        "SELECT balance FROM accounts WHERE account_id = ?",
        (account_id,)
    ).fetchone()
    return jsonify({"account_id": account_id, "balance": row[0]})
