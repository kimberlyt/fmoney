import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_mail import Mail
from flask_migrate import Migrate



app = Flask(__name__)

#app.config['AUTHY_API_KEY']='ccdd23dd47639146a124ced0219b5134'
app.config['TWILIO_ACCOUNT_SID'] = 'AC1d76c0fb6bebd3dbe8cafb0712816284'
app.config['TWILIO_AUTH_TOKEN'] = 'ccdd23dd47639146a124ced0219b5134'
app.config['TWILIO_VERIFY_SERVICE_ID'] = 'VAd3a63f3cc9ae1514e6120445afe6cf23'


app.config['SECRET_KEY']= '859bd31bb2f0b6f02fca6ffbfaf8c8d3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USER'] = 'smtp.gmail.com'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail=Mail(app)
migrate = Migrate(app,db)



from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main
from flaskblog.errors.handlers import errors


app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(errors)
