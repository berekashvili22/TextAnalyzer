from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo

class TextForm(FlaskForm):
    text = TextAreaField('', validators=[DataRequired()])
   
    submit = SubmitField('')

