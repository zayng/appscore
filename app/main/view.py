# -*- coding: utf-8 -*-
"""
Created on 2016/10/12

@author: wb-zy184129
"""
from flask import flash, redirect, request, render_template, url_for
from . import main
from .forms import LoginForm


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # if form.username.data != 'admin' or \
        #         form.password.data != 'secret':
        if form.username.data != 'admin':
            flash('Invalid credentials')
        else:
            flash('You were successfully logged in')
            return redirect(url_for('.index'))
    return render_template('login.html', form=form)