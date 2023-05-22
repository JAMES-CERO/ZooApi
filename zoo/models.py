from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Reptile(db.Model):
    __tablename__ = 'reptiles'

    id = db.Column(db.Integer, primary_key=True)
    scientific_name = db.Column(db.String(50))
    conservation_status = db.Column(db.String(50))
    native_habitat = db.Column(db.String(100))
    fun_fact = db.Column(db.Text)



# The main endpoint should be /reptiles.
# The database should be named ballpy.
# The table should be named reptiles.