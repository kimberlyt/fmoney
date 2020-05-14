from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError,Optional
from flask_login import current_user
from flaskblog.models import User

class TransferForm(FlaskForm):
    username = StringField('Recipient', validators=[DataRequired(), Length(min=2,max=20)], render_kw={"placeholder": "Username"})
    amount = DecimalField('Payment', validators=[DataRequired()], places=2, render_kw={"placeholder": "Amount of Money"})
    note = TextAreaField('Note',validators=[Optional()])
    
    submit= SubmitField()
    def validate_username(self,username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user is None:
                raise ValidationError('That username does not exist.Please choose a different one')