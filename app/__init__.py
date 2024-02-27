from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import select, Integer, func, Column, Integer, String, ForeignKey, text, Text
from flask_login import LoginManager

from app import pages
from app import models
from app import auth

# class Base(DeclarativeBase):
#     pass

# db = SQLAlchemy(model_class=Base)

def create_app():    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Ssecret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/blog'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return models.ReaderAccounts.query.get(user_id)
    
    app.register_blueprint(pages.bp)
    app.register_blueprint(auth.auth)
    
    models.db.init_app(app)
    return app
