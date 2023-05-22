from flask import Flask
#factory

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABSE_URI'] = 'postgresql://postgres:Bratva@localhost:5432/zoo'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app

#database posql


