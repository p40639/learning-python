from flask import Flask, redirect, request
import sqlite3
app = Flask(__name__)

@app.route("/")
def hello_world():
    with open('tingsweb-signup.html', 'r') as file:
        data = file.read()
        return data

@app.route("/register")
def register():
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * from users")
    print(cursor.fetchall())
    user = request.args.get("user")
    password = request.args.get("password")
    cursor.execute("INSERT INTO users VALUES (?,?,?,?,?)", ("Ting","email","123",user,password))
    connection.commit()
    connection.close()
    with open('tingsweb.html', 'r') as file:
        data = file.read()
        return data