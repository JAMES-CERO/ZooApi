from flask import ( Blueprint, jsonify, request, redirect)
import json
from . import models
bp = Blueprint('reptile', __name__, url_prefix ='/reptiles')

reptiles = json.load(open('reptiles.json'))
print(reptiles)

@bp.route('/', methods =['GET', 'POST'])
def index():
    if request.method == 'POST':

        common_name = request.form['common_name']
        scientific_name = request.form['scientific_name']
        conservation_status = request.form['conservation_status']
        native_habitat = request.form['native_habitat']
        fun_fact = request.form['fun_fact']

        new_reptile = models.Reptile(
            common_name=common_name,
            scientific_name=scientific_name,
            conservation_status=conservation_status,
            native_habitat=native_habitat,
            fun_fact=fun_fact
        )

        models.db.session.add(new_reptile)
        models.db.session.commit()

        return redirect('/reptiles')
    
    return jsonify(reptiles)


@bp.route('/<int:id>', methods=['GET'])
def show(id):
    if id >= 1 and id <= len(reptiles):
        reptile = reptiles[id - 1]
        return jsonify(reptile)
    else:
        return jsonify({'error': 'Reptile not found'}), 404