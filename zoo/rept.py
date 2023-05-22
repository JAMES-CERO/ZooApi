from flask import Blueprint
bp = Blueprint('rept', __name__, '/reptiles')

@bp.route('/')
def index():
    return 'Hello world'