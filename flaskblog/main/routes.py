from flask import render_template, request, Blueprint
from flaskblog import db
from flaskblog.models import Post,User
from flask_login import current_user, login_required



main = Blueprint('main',__name__)


@main.route("/")

@main.route("/home")
#@login_required
def home():
    return render_template('home.html')#, posts=posts)


@main.route("/dash")
@login_required
def dash():
    return render_template('layout.html')#, posts=posts)


@main.route("/about")
@login_required
def about():
    return render_template('about.html', title='About')






@main.route("/history",methods=['GET','POST'])# move to posts
@login_required
def history():
    posts = Post.query.all()
    return render_template('history.html',title='Transaction History',posts=posts)
