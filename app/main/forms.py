# -*- coding: utf-8 -*-
"""
Created on 2016/10/17

@author: wb-zy184129
"""
from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from flask_uploads import UploadSet, IMAGES
from app.models import User


class LoginForm(Form):
    username = StringField('用户', validators=[DataRequired(), Length(1, 16)])
    password = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('登录')


class RegisterForm(Form):
    username = StringField('用户', validators=[DataRequired(), Length(1, 16)])
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 16)])
    password = PasswordField('新密码', validators=[DataRequired(), EqualTo('confirm', 'Password must match')])
    confirm = PasswordField('确认密码')
    accept = BooleanField('我已阅读并同意协议')
    submit = SubmitField('注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已被注册.')

    def validate_email(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('邮箱已被注册.')


images = UploadSet('images', IMAGES)


class UploadForm(Form):
    photo = FileField('Your images', validators=[FileRequired(), FileAllowed(images, '仅支持图片上传.')])
    file_name = StringField('文件名称')
