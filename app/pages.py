from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

bp = Blueprint('pages', __name__)

@bp.route('/')
def home():
    return "<h1>Hello world</h1>"