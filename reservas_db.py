from datetime import datetime, timedelta, date
from sqlalchemy_base import base, initalize_database
from sqlalchemy import desc, and_


import uuid
# Column(String(32), default=lambda: uuid.uuid4().hex, primary_key=True)

class Reservas(base.Model):
    ID = base.Column(base.Integer, primary_key=True)
    # ID = db.Column(db.String(32), default=lambda: uuid.uuid4().hex, primary_key=True)
    Creacion = base.Column(base.DateTime, nullable=False, default=datetime.now())
    Nombre = base.Column(base.String(240), nullable=False)
    Telefono = base.Column(base.String(40), nullable=True)
    Reserva = base.Column(base.DateTime, nullable=False, default=datetime.now())

    def __repr__(self):
        return '<Reserva {0} para {1}>'.format(self.ID, self.Nombre)

    @staticmethod
    def __reserva_de_fecha_hora__(fecha, hora):
        # datetime.date.today() + datetime.timedelta(days=1)
        return datetime.now()

    @staticmethod
    def add(nombre, telefono, fecha, hora):
        reserva = Reservas(Nombre=nombre, Telefono=telefono, Creacion=datetime.now(),
                           Reserva=Reservas.__reserva_de_fecha_hora__(fecha, hora))
        base.session.add(reserva)
        base.session.commit()

    @staticmethod
    def query_today():
        # return Reservas.query.order_by(desc(Reservas.Reserva)).all()
        print(date.today())
        return Reservas.query.filter(and_(
            Reservas.Reserva >= date.today(),
            Reservas.Reserva < date.today() + timedelta(days=1))).order_by(Reservas.Reserva).all()

    @staticmethod
    def today():
        return Reservas.query.all()

    @staticmethod
    def init_app(app):
        initalize_database(app)

        base.drop_all()
        base.create_all()

        reservas = [
            Reservas(
                Nombre='Ayersondio Perales',
                Telefono='758-18931',
                Creacion=datetime.now(),
                Reserva=date.today() - timedelta(days=1)),

            Reservas(
                Nombre='Mañanedio Peponi',
                Telefono='758-18931',
                Creacion=datetime.now(),
                Reserva=date.today() + timedelta(days=1)),

            Reservas(
                Nombre='Julio Ortega y Familia',
                Telefono='758-18931',
                Creacion=datetime.now(),
                Reserva=datetime.today() + timedelta(minutes=15)),

            Reservas(
                Nombre='Isabel Lozano',
                Telefono='689-34545',
                Creacion=datetime.now(),
                Reserva=datetime.today() + timedelta(minutes=30)),

            Reservas(
                Nombre='Dolores Flores',
                Telefono='758-18931',
                Creacion=datetime.now(),
                Reserva=datetime.today() + timedelta(hours=2)),

            Reservas(
                Nombre='Silvia Savioncelo',
                Telefono='758-18931',
                Creacion=datetime.now(),
                Reserva=datetime.today() + timedelta(hours=5)),

            Reservas(
                Nombre='Amanda Moratti',
                Telefono='375-9998',
                Creacion=datetime.now(),
                Reserva=datetime.today() + timedelta(hours=10))]

        base.session.add_all(reservas)
        base.session.commit()

        print("Query all: {0}".format(Reservas.query.all()))
