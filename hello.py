from curses import keyname
from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///tingsweb-datbas.db")

@app.route("/")
def hello_world():
    return render_template("ting/tingsweb-signup.html")

@app.route("/registered", methods=["POST"])
def registered():
    print(request.form)
    username = request.form.get("username")
    password = request.form.get("password")
    lastname = request.form.get("lastname")
    firstname = request.form.get("firstname")
    email = request.form.get("email")
    phonenumber = request.form.get("phonenumber")
    db.execute("INSERT INTO registrants (username, password, lastname, firstname, email, phonenumber) VALUES(?, ?, ?, ?, ?, ?)", username, password, lastname, firstname, email, phonenumber)
    return render_template("ting/tingsweb.html")



# @app.route("/register")
# def register():
#     connection = sqlite3.connect('example.db')
#     cursor = connection.cursor()
#     cursor.execute("SELECT * from users")
#     print(cursor.fetchall())
#     user = request.args.get("user")
#     password = request.args.get("password")
#     cursor.execute("INSERT INTO users VALUES (?,?,?,?,?)", ("Ting","email","123",user,password))
#     connection.commit()
#     connection.close()
#     with open('tingsweb.html', 'r') as file:
#         data = file.read()
#         return data