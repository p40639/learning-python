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

@app.route("/login")
def hello_world():
    if session.get("username") is not None:
        return redirect("/")
    error=request.args.get("error")
    if error is not None:
        if error == "fail-to-login":
            return render_template("ting/tingsweb-login.html",error = "Invalid")
        return render_template("ting/tingsweb-login.html",error = error)
    return render_template("ting/tingsweb-login.html",error = "")

@app.route("/registered", methods=["GET","POST"])
def registered():
    username = request.form.get("username")
    password = request.form.get("password")
    lastname = request.form.get("lastname")
    firstname = request.form.get("firstname")
    email = request.form.get("email")
    phonenumber = request.form.get("phonenumber")
    db.execute("INSERT INTO registrants (username, password, lastname, firstname, email, phonenumber) VALUES(?, ?, ?, ?, ?, ?)", username, password, lastname, firstname, email, phonenumber)
    return render_template("ting/tingsweb.html")

@app.route("/", methods=["GET","POST"])
def logined():
    if session.get("username") is not None:
        print("You are logined")
    if request.method == "POST":
        print(request.form)
        username = request.form.get("username")
        password = request.form.get("password")
        info = db.execute(f"SELECT * from registrants where username = '{username}'")
        if len(info) != 1:
            return redirect("/login?error=fail-to-login")
        if info[0]['password'] == password:
            session["username"] = username
            return render_template("ting/tingsweb.html")
        return redirect("/login?error=fail-to-login")
    return render_template("ting/tingsweb.html")

@app.route("/register", methods=["GET","POST"])
def register():
    return render_template("ting/tingsweb-signup.html")




