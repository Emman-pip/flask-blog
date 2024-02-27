from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, func
from app.models import db, AuthorAccounts
from flask_login import current_user

bp = Blueprint('pages', __name__)

@bp.route('/')
def home():
    data = db.session.scalars(select(AuthorAccounts)).all()
    return render_template('pages/home.html', name=current_user)