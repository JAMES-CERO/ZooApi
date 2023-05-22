from flask import ( Blueprint, jsonify, request )
import json
bp = Blueprint('reptile', __name__, url_prefix ='/reptiles')

reptiles = json.load(open('reptiles.json'))
print(reptiles)

@bp.route('/', methods =['GET', 'POST'])
def index():
    return 'Hello world'

@bp.route('/int:id')
def show(id):
    reptile = reptiles[id -1]
    return jsonify(reptile)