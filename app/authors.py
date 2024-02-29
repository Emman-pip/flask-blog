from flask import Blueprint, request, render_template, redirect, url_for, flash
from .models import db, AuthorAccounts, Authors, Articles
from werkzeug.security import generate_password_hash, check_password_hash


authors = Blueprint("authors", __name__)


@authors.route("/author-options")
def options():
    return render_template("authors/options.html")


@authors.route("/author-login")
def login():
    return render_template("authors/authorLogin.html")


@authors.route("/author-signup")
def signup():
    return render_template("authors/authorSignup.html")


@authors.route("/author-signup", methods=["POST"])
def signup_post():
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")

    authorEmail = AuthorAccounts.query.filter_by(email=email).first()
    authorUsername = AuthorAccounts.query.filter_by(username=username).first()

    if authorUsername or authorEmail:
        flash("Invalid email or username")
        return redirect(url_for("authors.signup"))

    authorAccount = AuthorAccounts(
        username=username,
        email=email,
        password=generate_password_hash(password, method="pbkdf2:sha1"),
    )

    db.session.add(authorAccount)
    db.session.commit()

    return redirect(url_for("authors.login"))
