from flask import Blueprint, render_template, request, redirect, url_for

from app.domain.rules import username
from app.forms.registration import RegistrationForm


main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home():
    return redirect(url_for('main.register'))
"""
@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return "Form submitted successfully!"
    return render_template("register.html", form=form)
"""


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return f"Welcome {form.username.data}!"
    return render_template("register.html", form=form)