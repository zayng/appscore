# -*- coding: utf-8 -*-
"""
Created on 2016/10/12

@author: wb-zy184129
"""
from flask import flash, redirect, request, render_template, url_for
from . import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            pass
        else:
            # flash('You were successfully logged in')
            return redirect(url_for('.index'))
    flash('Invalid credentials')
    return render_template('login.html')
