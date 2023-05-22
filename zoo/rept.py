from flask import Blueprint
import json
bp = Blueprint('rept', __name__, url_prefix ='/reptiles')

reptiles = json.load(open('reptiles.json'))
print(reptiles)

@bp.route('/')
def index():
    return 'Hello world'

@bp.route('/<id>')
def show(id):
    reptiles = reptiles[id -1]
    return reptiles