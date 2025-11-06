from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.domain.rules import username

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Register')

    #method in Registration Form to validate username
    def validate_username(self, value):
        try:
            username(value.data)
        except ValueError as e:
            raise ValidationError(str(e))


    def validate_email(self, value):
        pass


    def validate_password(self, value):
        pass

    def validate_confirm_password(self, value):
        pass


    def validate_bio_or_comment(self):
        pass




