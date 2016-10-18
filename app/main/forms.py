# -*- coding: utf-8 -*-
"""
Created on 2016/10/17

@author: wb-zy184129
"""
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(Form):
    username = StringField('用户', validators=[DataRequired(), Length(1, 16)])
    password = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('登录')


class RegisterForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(1, 16)])
    email = StringField('Email Address', validators=[DataRequired(), Length(1, 16)])
    password = PasswordField('New Password', validators=[DataRequired(), EqualTo('confirm', 'Password must match')])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', validators=[DataRequired()])