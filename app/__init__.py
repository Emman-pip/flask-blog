from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import select, Integer, func, Column, Integer, String, ForeignKey, text

from app import pages

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(pages.bp)

db.init_app(app)

class Users(db.Model):
    account_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

class Authors(db.Model):
    author_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    description = Column(String, nullable=False)
    account_id = Column(Integer, ForeignKey(Users.account_id))
    
class Articles(db.Model):
    article_id = Column(Integer, primary_key=True)
    article_title = Column(String, nullable=False)
    article_content = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey(Authors.author_id))
    total_views = Column(Integer, default=0)