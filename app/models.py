from sqlalchemy import select, Integer, func, Column, Integer, String, ForeignKey, text, Text
# from app import db
from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Users(db.Model):
    account_id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

class Authors(db.Model):
    author_id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    account_id = Column(Integer, ForeignKey(Users.account_id))
    
class Articles(db.Model):
    article_id = Column(Integer, primary_key=True)
    article_title = Column(Text, nullable=False)
    article_content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey(Authors.author_id))
    total_views = Column(Integer, default=0)
