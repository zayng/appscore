# -*- coding: utf-8 -*-
"""
Created on 2016/10/12

@author: wb-zy184129
"""
from flask import Blueprint

main = Blueprint('main', __name__)

from . import view
