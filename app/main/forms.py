# -*- coding: utf-8 -*-
"""
Created on 2016/10/17

@author: wb-zy184129
"""
from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_uploads import UploadSet, IMAGES


class LoginForm(Form):
    username = StringField('用户', validators=[DataRequired(), Length(1, 16)])
    password = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('登录')


class RegisterForm(Form):
    username = StringField('用户', validators=[DataRequired(), Length(1, 16)])
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 16)])
    password = PasswordField('新密码', validators=[DataRequired(), EqualTo('confirm', 'Password must match')])
    confirm = PasswordField('确认密码')
    accept_tos = BooleanField('我已阅读并同意协议', validators=[DataRequired()])
    register = SubmitField('注册')

images = UploadSet('images', IMAGES)


class UploadForm(Form):
    photo = FileField('Your images', validators=[FileRequired(), FileAllowed(['jpg', 'png'], '仅支持图片上传.')])
    comment = StringField('Comment')
