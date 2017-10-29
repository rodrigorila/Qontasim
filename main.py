from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap
from reservas_db import Reservas

# App config.
# DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '020ac046-b107-11e7-b478-00e04c534458'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://rod:tt8uyi_ddP9@localhost/Qontasim_SachaDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


def initialize():

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

    Reservas.init_app(app)

@app.route("/counter", methods=['GET'])
def counter():
    return render_template("counter.html")


@app.route("/nueva", methods=['GET'])
def nueva():
    return render_template('nueva.html')


@app.route("/agregar", methods=['POST'])
def agregar():
    nombre = request.form.get('Nombre', None)
    telefono = request.form.get('Telefono', None)
    fecha = request.form.get('Fecha', None)
    hora = request.form.get('Hora', None)

    Reservas.add(nombre, telefono, fecha, hora)

    return redirect("/")


@app.route("/lista", methods=['GET'])
def lista():
    return render_template('lista.html', Reservas = Reservas.query_today())


@app.route("/", methods=['GET'])
def welcome():
    return render_template('welcome.html')

if __name__ == "__main__":
    initialize()

    Bootstrap(app)
    app.run()