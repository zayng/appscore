# -*- coding: utf-8 -*-
"""
Created on 2016/10/20

@author: wb-zy184129
"""
from datetime import datetime
from . import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, index=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(128))
    sex = db.Column(db.Integer)
    member_since = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    ts = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    def __repr__(self):
        return '<User %r>' % self.username


