from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms.registration import RegistrationForm

main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def index():
    return redirect(url_for("main.register"))

@main.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.is_submitted():
        print("Form submitted")
        print("Form valid:", form.validate())
        print("Form errors:", form.errors)

    if form.validate_on_submit():
        flash("Registration successful!", "success")
        return redirect(url_for("main.loading"))  # POST → Redirect → GET
    return render_template("register.html", form=form)

@main.route("/loading")
def loading():
    return render_template("loading.html")

@main.route("/home")
def home():
    return render_template("home.html")

