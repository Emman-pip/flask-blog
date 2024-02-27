from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, func
from app.models import db, AuthorAccounts

bp = Blueprint('pages', __name__)

@bp.route('/')
def home():
    data = db.session.scalars(select(AuthorAccounts)).all()
    return render_template('pages/home.html')