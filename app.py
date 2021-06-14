import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


# cloudinary.config(
#     cloud_name=os.environ.get("CLOUD_NAME"),
#     api_key=os.environ.get("API_KEY"),
#     api_secret=os.environ.get("API_SECRET")
# )


app = Flask(__name__)

app.config["MONGO_DB"] = os.environ.get("MONGO_DB")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    # LIST ALL OF THE DRINKS IN THE DATABASE
    drinks = mongo.db.drinks.find()
    return render_template("drinks.html", drinks=drinks)


@app.route("/search", methods=["GET", "POST"])
def search():
    # SEARCH FUNCTION FROM HOMEPAGE
    search = request.form.get("search")
    drinks = mongo.db.drinks.find({"$text": {"$search": search}})
    return render_template("drinks.html", drinks=drinks)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # CHECK IF USERNAME OR EMAIL IS ALREADY REGISTERED ON SITE
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # ERROR MESSAGE IF USERNAME ALREADY EXISTS
        if existing_user:
            flash("Sorry, that username already exists")
            return redirect(url_for("register"))

        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})
        # ERROR MESSAGE IF EMAIL ALREADY EXISTS
        if existing_email:
            flash("Sorry, that email's already registered")
            return redirect(url_for("register"))
        # DETAILS TO REGISTER IN MONGO DB FOR NEW USERS
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
        # LOAD PROFILE PAGE IF USER ALREADY EXISTS
        return render_template("profile.html", username=username)
    else:
        # RETURNS USER TO LOGIN PAGE
        return redirect(url_for("login"))


@app.route("/drinks_by")
def drinks_by():
    drinks_by = mongo.db.drinks.find()
    return render_template("drinks_by.html", drinks_by=drinks_by)

    # mongo.db.drinks.find({"created_by": "username"})
    # return render_template("drinks_by.html")
#     drinks = mongo.db.drinks.find()
#     return render_template("drinks.html", drinks=drinks)


@app.route("/logout")
def logout():
    # LOGGS USER OUT OF THEI SESSION
    flash("You have logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_drink", methods=["GET", "POST"])
def add_drink():
    # IF USER IS POSTING INFORMATION TO THE WEBSITE
    if request.method == "POST":
        new_drink = {
            "drink_category": request.form.get("drink_category"),
            "drink_name": request.form.get("drink_name"),
            "drink_ingredients": request.form.get("drink_ingredients"),
            "drink_instructions": request.form.get("drink_instructions"),
            "preperation_time": request.form.get("preperation_time"),
            "serves": request.form.get("serves"),
            "created_by": session["user"]
        }
        mongo.db.drinks.insert_one(new_drink)
        flash("Drink added to database")
        return redirect(url_for("home"))

    return render_template("add_drink.html")


@app.route("/edit_drink/<drink_id>", methods=["GET", "POST"])
def edit_drink(drink_id):
    if request.method == "POST":
        new_drink = {
            "drink_category": request.form.get("drink_category"),
            "drink_name": request.form.get("drink_name"),
            "drink_ingredients": request.form.get("drink_ingredients"),
            "drink_instructions": request.form.get("drink_instructions"),
            "preperation_time": request.form.get("preperation_time"),
            "serves": request.form.get("serves"),
            "created_by": session["user"]
        }
        mongo.db.drinks.update({"_id": ObjectId(drink_id)}, new_drink)
        flash("Drink has been updated")
        return redirect(url_for("home"))

    drink = mongo.db.drinks.find_one({"_id": ObjectId(drink_id)})
    # return redirect(url_for("home"))
    return render_template("edit_drink.html", drink=drink)


@app.route("/delete_drink/<drink_id>")
def delete_drink(drink_id):
    # FINDS DRINK BY ITS UNIQUE ID AND DELETE IT
    mongo.db.drinks.remove({"_id": ObjectId(drink_id)})
    flash("Drink has been deleted", "info")
    return redirect(url_for("home"))


@app.route("/shop")
def shop():
    # PAGE FOR USERS TO SHOP FOR COCKTAIL ESSENTIALS
    return render_template("shop.html")


# @app.route('/<drink_id>', methods=["POST"])
# def upvote(drink_id):
#     mongo.db.drinks.update_one({"_id": ObjectId(drink_id)}, {"$inc": {'upvotes': 1}})
#     return redirect(url_for("home"))
    # return redirect(url_for('recipe_description', recipe_id=recipe_id))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)


if request.method == "POST":
    photo = request.files['photo_url']
    photo_upload = cloudinary.uploader.upload(photo)
    review = {
        "photo_url": photo_upload["secure_url"]
    }
