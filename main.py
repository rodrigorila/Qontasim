from flask import Flask, render_template, request, url_for, redirect, make_response
from flask_bootstrap import Bootstrap
from reservas_db import Reservas

from configuration import Configuration

config = Configuration('config.xml')
print('Connection string: {}'.format(config.connection_string))


# App config.
# DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '020ac046-b107-11e7-b478-00e04c534458'
app.config['SQLALCHEMY_DATABASE_URI'] = config.connection_string
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
        ValidateVersion("SQLAlchemy", "1.1.15", sqlalchemy.__version__)
        ValidateVersion("Flask-SQLAlchemy", "2.3.2", flask_sqlalchemy.__version__)
        ValidateVersion("Flask-Bootstrap", "3.3.7.1.dev1", flask_bootstrap.__version__)

        print("Flask: {0}".format(flask.__version__))
        print("SQLAlchemy: {0}".format(sqlalchemy.__version__))
        print("Flask-SQLAlchemy {0}".format(flask_sqlalchemy.__version__))
        print("Flask-Bootstrap {0}".format(flask_bootstrap.__version__))

    ValidateVersions()

    Reservas.init_app(app)

# This method renders a page that helps validate the Reservation (reservation.js) object
# @app.route("/counter", methods=['GET'])
# def counter():
#     return render_template("counter.html")
 
@app.route("/update_reservation", methods=['POST'])
def update_reservation():
    nombre = request.form.get('Nombre', None)
    telefono = request.form.get('Telefono', None)
    fecha = request.form.get('Fecha', None)
    hora = request.form.get('Hora', None)
    notes = request.form.get('Notas', None)

    if request.form.action is "add":
        Reservas.update_reservation(nombre, telefono, fecha, hora, notes)

    if request.form.action is "edit":
        id = request.form.get('ID', None)
        Reservas.update_reservation(nombre, telefono, fecha, hora, notes, id)

    return make_response ("updated", 200)

@app.route("/add_reservation", methods=['GET'])
def add_reservation():
    return render_template("reservation.html", action="add")

@app.route("/edit_reservation", methods=['POST'])
def edit_reservation():
    id = request.form.get('id', None)

    if not id:
        raise Exception('No es posible editar la reserva')

    r = Reservas.get(id)

    if not r:
        raise Exception('La reserva "{0}" no existe'.format(id))

    # REDIRECT VS RENDER_TEMPLATE
    # (https://stackoverflow.com/questions/21668481/difference-between-render-template-and-redirect)
    #
    # return redirect(url_for('index', var=var))
    # return render_template('index.html', var=var)
    #
    # redirect returns a 302 header to the browser, with
    # its Location header as the URL for the index function.
    # render_template returns a 200, with the index.html
    # template returned as the content at that URL.

    return render_template("reservation.html", action="edit", reservation=r)

@app.route("/get_reservations", methods=['POST'])
def get_reservations():
    lapse = request.form.get('filter')
    auto_hide = request.form.get('auto_hide', True)

    lapses = {
        'all': lambda: Reservas.query_all(),
        'today': lambda: Reservas.query_days_from_now(0),
        'tomorrow': lambda: Reservas.query_days_from_now(1),
    }

    query = lapses.get(lapse, lambda: print("Filter {0} does not exist".format(lapse)));

    return render_template('reservations_table.html', Reservas = query())


@app.route("/change_reservation", methods=['POST'])
def change_reservation():
    action = request.form.get('action')
    id = request.form.get('id')

    actions = {
        'enter': lambda: Reservas.enter(id),
        'cancel': lambda: Reservas.cancel(id),
    }

    method = actions.get(action, lambda: print("Action {0} does not exist".format(action)));

    method()

    return make_response(id, 200)


@app.route("/show_reservations", methods=['GET'])
def show_reservations():
    return render_template('reservations.html')


@app.route("/", methods=['GET'])
def welcome():
    return render_template('welcome.html')

if __name__ == "__main__":
    initialize()

    Bootstrap(app)
    app.run()