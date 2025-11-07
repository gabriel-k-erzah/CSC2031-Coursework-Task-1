from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.forms.registration import RegistrationForm

main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def index():
    return redirect(url_for("main.register"))


#registration route
@main.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.is_submitted():
        print("Form submitted")
        print("Form valid:", form.validate())
        print("Form errors:", form.errors)

    if form.validate_on_submit():
        flash("Registration successful!", "success")
        return redirect(url_for("main.loading", username=form.username.data, bio=form.bio_or_comment.data))
    return render_template("register.html", form=form)


#loading route
@main.route("/loading")
def loading():
    username = request.args.get("username")
    bio = request.args.get("bio")
    return render_template("loading.html", username=username, bio=bio)


#home route
@main.route("/home")
def home():
    username = request.args.get("username")
    bio = request.args.get("bio")
    return render_template("home.html", username=username, bio=bio)