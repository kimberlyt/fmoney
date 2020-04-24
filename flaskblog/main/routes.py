from flask import render_template, request, Blueprint
from flaskblog.models import Post
from flask_login import current_user, login_required
from flaskblog.users.forms import TransferForm


main = Blueprint('main',__name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')#, posts=posts)


@main.route("/dash")
def dash():
    return render_template('layout.html')#, posts=posts)

@main.route("/transfer", methods=['GET','POST'])
def transfer():
    if current_user.is_authenticated:
       #return redirect(url_for('dash'))
        form = TransferForm()
    if form.validate_on_submit():
        #user = User(username=form.username.data)
        flash('SENT','success')
        return render_template('dash')
    return render_template('transfer.html', title='Transfer', form=form)
    


@main.route("/about")
def about():
    return render_template('about.html', title='About')