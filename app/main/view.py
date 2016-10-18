# -*- coding: utf-8 -*-
"""
Created on 2016/10/12

@author: wb-zy184129
"""
from flask import flash, redirect, request, render_template, url_for
from . import main
from .forms import LoginForm, RegisterForm


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data != 'admin' or \
                form.password.data != 'secret':
            flash('Invalid credentials')
        else:
            flash('You were successfully logged in')
            return redirect(url_for('.index'))
    return render_template('login.html', form=form)


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.username.data == 'admin':
            flash('Thank you register.')
            return render_template(url_for('.login'))
        flash('无效注册.')
    return render_template('register.html', form=form)