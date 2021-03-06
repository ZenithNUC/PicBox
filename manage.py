# -*- encoding:utf-8 -*-
# -*- python:3.8     -*-
# -*- author:LiuBX   -*-
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from app import app
from exts import db
import model

manager = Manager(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()