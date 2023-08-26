from flask import (Blueprint, render_template)

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/')
def index(): 
    return render_template('facts/index.html')

@bp.route('/new')
def new(): 
    return render_template('facts/new.html')