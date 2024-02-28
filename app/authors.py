from flask import Blueprint, request, render_template


authors = Blueprint('authors', __name__)


@authors.route('/author-options')
def options():
    return render_template('authors/options.html')

@authors.route('/author-login')
def login():
    return 'login_sudo'

    
@authors.route('/author-signup')
def signup():
    return 'signup'
