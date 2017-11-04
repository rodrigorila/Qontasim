from datetime import datetime, timedelta, date
from sqlalchemy_base import sqla, initalize_database
from sqlalchemy import asc, and_


import uuid
# Column(String(32), default=lambda: uuid.uuid4().hex, primary_key=True)

class Reservas(sqla.Model):
    ID = sqla.Column(sqla.Integer, primary_key=True)
    # ID = db.Column(db.String(32), default=lambda: uuid.uuid4().hex, primary_key=True)
    Creacion = sqla.Column(sqla.DateTime, nullable=False, default=datetime.now())
    Nombre = sqla.Column(sqla.String(240), nullable=False)
    Telefono = sqla.Column(sqla.String(40), nullable=True)
    NroPersonas = sqla.Column(sqla.Integer, nullable=False, default=1)
    Reserva = sqla.Column(sqla.DateTime, nullable=False, default=datetime.now())
    Estado = sqla.Column(sqla.String(10), nullable=False, default="pendiente")

    def __repr__(self):
        return '<Reserva {0} de {1} para {2} personas en fecha {3}>'.format(self.ID, self.Nombre, self.NroPersonas, self.Reserva)

    @staticmethod
    def __reserva_de_fecha_hora__(fecha, hora):
        # datetime.date.today() + datetime.timedelta(days=1)
        return datetime.now()

    @staticmethod
    def add(nombre, telefono, fecha, hora):
        reserva = Reservas(Nombre=nombre, Telefono=telefono, Creacion=datetime.now(),
                           Reserva=Reservas.__reserva_de_fecha_hora__(fecha, hora))
        sqla.session.add(reserva)
        sqla.session.commit()

    @staticmethod
    def query_days_from_now(days):
        return Reservas.query.filter(
            and_(
                Reservas.Reserva >= date.today() + timedelta(days=days),
                Reservas.Reserva < date.today() + timedelta(days=days+1)
            )).order_by(Reservas.Reserva).all()

    @staticmethod
    def query_all():
        return Reservas.query.order_by(asc(Reservas.Reserva)).all()

    @staticmethod
    def enter(id):
        r = Reservas.query.get(id)
        r.Estado = "ingresada"
        sqla.session.commit()

    @staticmethod
    def cancel(id):
        r = Reservas.query.get(id)
        r.Estado = "cancelada"
        sqla.session.commit()

    @staticmethod
    def range_dates(from_date, to_date, delta):
        d = from_date
        while d <= to_date:
            yield d
            d = d + delta

    @staticmethod
    def __default_reservas__():
        return [
            Reservas(
                Nombre='Andrés Cortazar',
                Telefono='758-18931',
                Creacion=datetime.now(),
                Reserva=date.today() - timedelta(days=1)),

            Reservas(
                Nombre='Olga Martinez',
                Telefono='758-18931',
                Creacion=datetime.now(),
                Reserva=date.today() + timedelta(days=1)),

            Reservas(
                Nombre='Julio Ortega y Familia',
                Telefono='758-18931',
                Creacion=datetime.now(),
                Reserva=datetime.today() - timedelta(minutes=15)),

            Reservas(
                Nombre='Isabel Lozano',
                Telefono='689-34545',
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

    @staticmethod
    def __generate_reservas__(from_date, to_date, delta):
        list = []
        for d in Reservas.range_dates(from_date, to_date, delta):
            list.append(
                Reservas(
                    Nombre = d,
                    Telefono = d,
                    Creacion = datetime.now(),
                    Reserva = d)
            )
        return list

    @staticmethod
    def init_app(app):
        initalize_database(app)

        sqla.drop_all()
        sqla.create_all()

        reservas = Reservas.__default_reservas__()

        # reservas = Reservas.__generate_reservas__(
        #     datetime.today() - timedelta(days=1),
        #     datetime.today() + timedelta(days=1),
        #     timedelta(minutes=15)
        # )

        # reservas = Reservas.__generate_reservas__(
        #     datetime(2017,10,31),
        #     datetime(2017,11,1),
        #     timedelta(hours=1)
        # )

        sqla.session.add_all(reservas)
        sqla.session.commit()
