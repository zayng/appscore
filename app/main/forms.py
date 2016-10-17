# -*- coding: utf-8 -*-
"""
Created on 2016/10/17

@author: wb-zy184129
"""
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(Form):
    username = StringField('用户', validators=[DataRequired(), Length(1, 16)])
    # password = PasswordField('密码', validators=[DataRequired()])
    # submit = SubmitField('登录')
