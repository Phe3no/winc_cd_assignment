from peewee import Model, CharField, AutoField
from flask import current_app
from ..db import get_db

with current_app.app_context():
    db = get_db()


class User(Model):
    id = AutoField
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db
