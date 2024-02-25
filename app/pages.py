from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, func
from app.models import db, Users

bp = Blueprint('pages', __name__)

@bp.route('/')
def home():
    data = db.session.scalars(select(Users)).all()
    return render_template('pages/home.html', data=data)