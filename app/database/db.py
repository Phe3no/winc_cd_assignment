from peewee import SqliteDatabase
from flask import current_app, g
import click


def get_db():
    if "db" not in g:
        g.db = SqliteDatabase(
            current_app.config["DATABASE"]
        )

    return g.db


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()
    # from ..database.models.Model import Model
    from ..database.models.user import User
    db.connect()
    # db.create_tables([Model, Model, Model])
    db.create_tables([User])


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
