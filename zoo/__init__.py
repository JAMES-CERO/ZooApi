from flask import Flask
#factory

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABSE_URI'] = 'postgresql://postgres:Bratva@localhost:5432/ballpy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)

    return app

#database posql


