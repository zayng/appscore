# -*- coding: utf-8 -*-
"""
Created on 2016/9/26

@author: wb-zy184129
"""

from flask import Flask
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hand table'
    bootstrap.init_app(app)
    app.extensions['bootstrap']['cdns'] = 'cdn.bootcss.com'

    from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)

    return app
