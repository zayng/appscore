# -*- coding: utf-8 -*-
"""
Created on 2016/10/12

@author: wb-zy184129
"""
from flask import flash, redirect, render_template, url_for
from werkzeug.utils import secure_filename
from . import main
from .forms import LoginForm, RegisterForm, UploadForm
from app.models import User
from app import db


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                flash('You were successfully logged in')
                return redirect(url_for('.index'))
            else:
                flash('用户密码不正确.')
        else:
            flash('用户名{}不存在'.format(form.username.data))
        return redirect(url_for('.login'))
    return render_template('login.html', form=form)


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.accept.data:
            user = User(
                username=form.username.data,
                email=form.email.data,
                password=form.password.data
            )
            db.session.add(user)
            db.session.commit()
            flash('用户{}注册成功.'.format(form.username.data))
        else:
            flash('请同意并勾选协议.')
        return redirect(url_for('.register'))
    return render_template('register.html', form=form)


@main.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        filename = secure_filename(form.photo.data.filename)
        form.photo.data.save('uploads/' + filename)
        flash("you already uploaded {}".format(filename))
    else:
        filename = None
    return render_template('upload.html', form=form, filename=filename)

