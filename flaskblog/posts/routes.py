from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post,User
from flaskblog.posts.forms import TransferForm


posts = Blueprint('posts', __name__)




@posts.route("/transfer", methods=['GET','POST'])
@login_required
def transfer():
    #if current_user.is_authenticated:
   bal1 = 0
   bal2 = 0
   form= TransferForm()
   if form.validate_on_submit():
       # existing_user = User.query.filter_by(email=email).first()
        #post = Post(username=form.username.data,amount=form.amount.data,note=form.note.data)
        #db.session.add(post)
        #db.session.commit()
        usr = User.query.filter_by(username=form.username.data).first()
        usr.balance = int(usr.balance) + int(form.amount.data)
        bal1=usr.balance
        current_user.balance = int(current_user.balance) - int(form.amount.data)
       
        post=Post(username=form.username.data,amount=form.amount.data,note=form.note.data)

        
        db.session.add(post)
        db.session.commit()
        
        

        flash('SENT','success')
        return render_template('history.html')
        bal1=0
   return render_template('transfer.html',title='Send Money',form=form)

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
