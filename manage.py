# -*- coding: utf-8 -*-

from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app.models import User

app = create_app('default')
manage = Manager(app)
migrate = Migrate(app, db)


def make_context_shell():
    return dict(app=app, db=db, User=User)

manage.add_command('Shell', Shell(make_context=make_context_shell))
manage.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manage.run()
