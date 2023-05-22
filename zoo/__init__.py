from flask import Flask
from flask_migrate import Migrate
from . import models
#factory

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Bratva@localhost:5432/ballpy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    

    
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    from . import reptile
    app.register_blueprint(reptile.bp)



    return app



