import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DB"] = os.environ.get("MONGO_DB")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    drinks = mongo.db.drinks.find()
    return render_template("drinks.html", drinks=drinks)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # CHECK IF USERNAME OR EMAIL IS ALREADY REGISTERED ON SITE
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Sorry, that username already exists")
            return redirect(url_for("register"))

        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_email:
            flash("Sorry, that email's already registered")
            return redirect(url_for("register"))

        register = {
            "your_name": request.form.get("your_name").lower(),
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(
                request.form.get("password")),
            "d_o_b": request.form.get("d_o_b").lower()
        }
        mongo.db.users.insert_one(register)

        # START USER IN A SESSION
        session["user"] = request.form.get("username").lower()
        flash("You have been succesfully registered")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # CHECK IF USER EXISTS
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # DOES PASSWORD MATCH USER INPUT
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome back {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # INCORRECT PASSWORD
                flash("Username and/or password is incorrect")
                return redirect(url_for("login"))

        else:
            # INCORRECT USERNAME
            flash("Username and/or password is incorrect")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    #
    flash("You have logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_drink", methods=["GET", "POST"])
def add_drink():
    if request.method == "POST":
        new_drink = {
            "drink_category": request.form.get("drink_category"),
            "drink_name": request.form.get("drink_name"),
            "drink_ingredients": request.form.get("drink_ingredients"),
            "drink_instructions": request.form.get("drink_instructions"),
            "created_by": session["user"]
        }
        mongo.db.drinks.insert_one(new_drink)
        flash("Drink added to database")
        return redirect(url_for("home"))

    return render_template("add_drink.html")


@app.route("/edit_drink/<drink_id>", methods=["GET", "POST"])
def edit_drink(drink_id):
    drink = mongo.db.drinks.find_one({"_id": ObjectId(drink_id)})
    return render_template("edit_drink.html", drink=drink)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
