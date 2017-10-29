from flask_sqlalchemy import SQLAlchemy

base = SQLAlchemy()

def initalize_database(app):
    base.init_app(app)
    base.app = app # esto es truco o está bien ????
