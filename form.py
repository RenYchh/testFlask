# encoding=utf-8

from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length,input_required,ValidationError
from wtforms import IntegerField,SubmitField


class FortyTwoForm(FlaskForm):
    answer = IntegerField('The Answer')
    submit = SubmitField()

    def Validate_answer(form,field):
        if field.data != 42:
            raise ValidationError('Must be 42.')


class LoginForm(FlaskForm):
    # def __init__(self):
    #     super(LoginForm,self).__init__()
    #     print("实例化表单")
    # username = StringField("Username", validators=[DataRequired()from])
    username = StringField("validate_Username", render_kw={'placeholder':'Your Username'})
    password = PasswordField("Password", validators=[DataRequired(),Length(8,128)])
    remember = BooleanField("Remember me")
    submit = SubmitField("Log in")
