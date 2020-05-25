import os
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint,current_app)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post,User
from flaskblog.posts.forms import TransferForm
from flask_mail import Message
from flaskblog import mail


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
        msg = Message('MoneyReach Transfer Notification ', sender='noreply@moneyreach.com', recipients =[current_user.email])
        #msg.body = f'''Dear { current_user.username },Your Transfer of {form.amount.data} to {usr.username} was sucessful,Sincerely,The MoneyReach Team'''
        msg.body = render_template("email.txt",usr=usr, form=form)
        mail.send(msg)
        

        flash('SENT','success')
        return render_template('history.html')
        bal1=0
   return render_template('transfer.html',title='Send Money',form=form)


    

