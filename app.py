from curses import keyname
from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# db = SQL("sqlite:///froshims.db")

# REGISTRANTS = {}

# SPORTS = [
#     "Basketball",
#     "Soccer",
#     "Ultimate Frisbee"
# ]


# @app.route("/")
# def index():
#     return render_template("appdetails.html", sports=SPORTS)


# @app.route("/register", methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         # Validate submission
#         name = request.form.get("name")
#         sport = request.form.get("sport")
#         session["key"] = 99
#         if not name or sport not in SPORTS:
#             return render_template("failure.html")

#         # Remember registrant
#         db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", name, sport)

#     # Confirm registration
#     return redirect("/registrants")


# @app.route("/registrants")
# def registrants():
#     registrants = db.execute("SELECT * FROM registrants")
#     return render_template("registrants.html", registrants=registrants)

# @app.route("/deregister", methods=["POST"])
# def deregister():

#     # Forget registrant
#     id = request.form.get("id")
#     if id:
#         db.execute("DELETE FROM registrants WHERE id = ?", id)
#     return redirect("/registrants")

# Connect to database
db = SQL("sqlite:///store.db")
...
@app.route("/")
def appdetails():
    books = db.execute("SELECT * FROM books")
    return render_template("books.html", books=books)

@app.route("/cart", methods=["GET", "POST"])
def cart():

    # Ensure cart exists
    if "cart" not in session:
        session["cart"] = []

    # POST
    if request.method == "POST":
        id = request.form.get("id")
        if id:
            session["cart"].append(id)
        return redirect("/cart")

    # GET
    books = db.execute("SELECT * FROM books WHERE id IN (?)", session["cart"])
    return render_template("cart.html", books=books)
