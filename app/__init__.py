# -*- coding: utf-8 -*-
"""
Created on 2016/9/26

@author: wb-zy184129
"""

from flask import Flask
from config import config
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
nav = Nav()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)
    nav.init_app(app)
    db.init_app(app)

    from .navbar import topbar
    nav.register_element('top', topbar)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
