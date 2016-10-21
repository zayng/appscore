# -*- coding: utf-8 -*-
"""
Created on 2016/10/20

@author: wb-zy184129
"""
from flask_nav.elements import Navbar, View

topbar = Navbar('None',
                View('Home', 'main.index'),
                View('login', 'main.login'),
                View('register', 'main.register'),
                View('upload', 'main.upload')
                )
