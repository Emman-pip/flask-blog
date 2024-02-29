from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, func, text
from app.models import db, Articles, Authors, AuthorAccounts
from flask_login import current_user

bp = Blueprint('pages', __name__)

@bp.route('/')
def home():
    data = db.session.execute(text("SELECT a.article_id, a.article_title, a.article_content, acc.username FROM articles AS a INNER JOIN authors ON authors.author_id=a.author_id INNER JOIN author_accounts AS acc ON acc.account_id=authors.account_id;"))
    return render_template('pages/home.html', name=current_user, data=data)

# TODO: Like titles to full articles