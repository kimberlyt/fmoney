from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm

posts = Blueprint('posts', __name__)

#posts = [
   # {
    #    'author': 'Corey Schafer',
    #    'title': 'Blog Post 1',
    #    'content': 'First post content',
    #    'date_posted': 'April 20, 2018'
    #},
   # {
   #     'author': 'Jane Doe',
   #     'title': 'Blog Post 2',
    #    'content': 'Second post content',
   #     'date_posted': 'April 21, 2018'
   # }
#]


#posts = [
   # {
    #    'author': 'Corey Schafer',
    #    'title': 'Blog Post 1',
    #    'content': 'First post content',
    #    'date_posted': 'April 20, 2018'
    #},
   # {
   #     'author': 'Jane Doe',
   #     'title': 'Blog Post 2',
    #    'content': 'Second post content',
   #     'date_posted': 'April 21, 2018'
   # }
#]
