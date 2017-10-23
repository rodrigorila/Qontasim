from datetime import datetime, date

from flask import Flask, render_template, flash, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

# App config.
# DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '020ac046-b107-11e7-b478-00e04c534458'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://rod:tt8uyi_ddP9@localhost/Qontasim_SachaDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Reservas(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Creacion = db.Column(db.DateTime, nullable=False, default=datetime.now())
    Nombre = db.Column(db.String(240), nullable=False)
    Telefono = db.Column(db.String(40), nullable=True)
    Reserva = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __repr__(self):
        return '<User {0} {1}>'.format(self.ID, self.Nombre)

db.drop_all()
db.create_all()

mamanis = Reservas(Nombre='Rosendo Mamani y Familia', Telefono='758-18931', Creacion=datetime.now(), Reserva=datetime.now())
choques = Reservas(Nombre='Jhonny Choque', Telefono='375-9998', Creacion=datetime.now(), Reserva=datetime.now())

db.session.add(mamanis)
db.session.add(choques)
db.session.commit()

print ("Query all: {0}".format(Reservas.query.all()))

def ValidateVersions():
    def ValidateVersion(name, expected, current):
        if expected == current:
            return

        raise Exception("{0} expected version is {1} but {2} version found".format(name, expected, current))

    import flask
    import sqlalchemy
    import flask_sqlalchemy
    import flask_bootstrap

    ValidateVersion("Flask", "0.12.2", flask.__version__)
    ValidateVersion("SQLAlchemy", "1.1.14", sqlalchemy.__version__)
    ValidateVersion("Flask-SQLAlchemy", "2.3.1", flask_sqlalchemy.__version__)
    ValidateVersion("Flask-Bootstrap", "3.3.7.1.dev1", flask_bootstrap.__version__)

    print("Flask: {0}".format(flask.__version__))
    print("SQLAlchemy: {0}".format(sqlalchemy.__version__))
    print("Flask-SQLAlchemy {0}".format(flask_sqlalchemy.__version__))
    print("Flask-Bootstrap {0}".format(flask_bootstrap.__version__))

ValidateVersions()

@app.route("/counter", methods=['GET'])
def counter():
    return render_template("counter.html")


@app.route("/nueva", methods=['GET'])
def nueva():
    reservas = Reservas.query.all()
    return render_template('nueva.html', Reservas= reservas)


@app.route("/agregar", methods=['POST'])
def agregar():
    def reserva_de_fecha_hora(fecha, hora):
        # datetime.date.today() + datetime.timedelta(days=1)
        return datetime.now()

    nombre = request.form.get('Nombre', None)
    telefono = request.form.get('Telefono', None)
    fecha = request.form.get('Fecha', None)
    hora = request.form.get('Hora', None)

    reserva = Reservas(Nombre = nombre, Telefono=telefono, Creacion=datetime.now(),
                       Reserva = reserva_de_fecha_hora(fecha, hora))
    db.session.add(reserva)
    db.session.commit()

    return redirect("/")


@app.route("/", methods=['GET'])
def main():
    reservas = Reservas.query.all()
    return render_template('lista.html', Reservas = reservas)


if __name__ == "__main__":
    Bootstrap(app)
    app.run()