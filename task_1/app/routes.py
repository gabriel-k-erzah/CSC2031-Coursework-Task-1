from flask import Blueprint, render_template, request, redirect, url_for
from task_1.app.forms.registration import RegistrationForm


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
    name = request.form.get('name') if request.method == 'POST' else ''
    return render_template('register.html', name=name)
