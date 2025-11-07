from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.domain.rules import *

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    confirm_password = StringField('Confirm Password', validators=[DataRequired()])
    bio_or_comment = StringField('Bio or Comment', validators=[DataRequired()])
    submit = SubmitField('Register')

    #method in Registration Form to validate username
    def validate_username(self, field):
        try:
            username(field.data)
        except ValueError as e:
            raise ValidationError(str(e))


    def validate_email(self, field):
        try:
            email(field.data)
        except ValueError as e:
            raise ValidationError(str(e))


    def validate_password(self, field):
        try:
            password(
                field.data,
                username_value=self.username.data,
                email_value=self.email.data
            )
        except ValueError as e:
            raise ValidationError(str(e))

    def validate_confirm_password(self, field):
        try:
            confirm_password(self.password.data, field.data)
        except ValueError as e:
            raise ValidationError(str(e))


    def validate_bio_or_comment(self):
        pass




