from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash
from .models import db, ReaderAccounts

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('auth/login.html')

# TODO: Do the authentication stuff first then do the database itself.

@auth.route('/signup')
def signup():
    return render_template('auth/signup.html')

@auth.route('/signup', methods=["POST"])
def signup_post():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    user = db.session.query(ReaderAccounts).filter_by(email=email).first()
    
    if user:
        print(user)
        flash('You already have an account.')
        return redirect(url_for('auth.signup'))
    
    db.session.add(ReaderAccounts(email=email, username=username, password=generate_password_hash(password, method='pbkdf2:sha1')))
    db.session.commit()
    
    return redirect(url_for('auth.login'))

    # return render_template('auth/signup.html')