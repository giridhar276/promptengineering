from flask import Flask, request, jsonify
import sqlite3
import subprocess

app = Flask(__name__)
ADMIN_PASSWORD = "admin123"

@app.post("/login")
def login():
    data = request.json
    if data["username"] == "admin" and data["password"] == ADMIN_PASSWORD:
        return jsonify({"token": "admin-token"})
    return jsonify({"error": "invalid"}), 401

@app.get("/user")
def get_user():
    username = request.args.get("username")
    conn = sqlite3.connect("users.db")
    row = conn.execute(
        "SELECT username, email, ssn FROM users WHERE username = '" + username + "'"
    ).fetchone()
    return jsonify(row)

@app.get("/download")
def download():
    return open(request.args.get("path"), "r").read()

@app.post("/ping")
def ping():
    host = request.json["host"]
    return subprocess.check_output("ping -c 1 " + host, shell=True)
