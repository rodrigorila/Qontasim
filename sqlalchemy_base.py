from flask_sqlalchemy import SQLAlchemy

sqla = SQLAlchemy()

def initalize_database(app):
    sqla.init_app(app)
    sqla.app = app # esto es truco o está bien ????
