from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import select, Integer, func, Column, Integer, String, ForeignKey, text, Text

from app import pages
from app import models

# class Base(DeclarativeBase):
#     pass

# db = SQLAlchemy(model_class=Base)

def create_app():    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/blog'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(pages.bp)
    models.db.init_app(app)
    return app
