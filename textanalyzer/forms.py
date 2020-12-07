from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_wtf.file import FileField, FileAllowed

class TextForm(FlaskForm):
    text = TextAreaField('', validators=[DataRequired()])
    submit = SubmitField('')

class FileForm(FlaskForm):
    text_file = FileField('', validators=[FileAllowed(['txt']), DataRequired()])
    submit2 = SubmitField('')

