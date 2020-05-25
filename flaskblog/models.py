from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flaskblog import db, login_manager,app
from flask_login import UserMixin
from flask import current_app
from twilio.rest import Client, TwilioException

#from flask_table import Table, Col





@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    balance = db.Column(db.Integer,nullable=True,default=0)
    email = db.Column(db.String(120),unique=True, nullable=False)
    image_file = db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    phonenum = db.Column(db.String,nullable=True)
    posts= db.relationship('Post', backref='author', lazy=True)

    def two_factor_enabled(self):
        return self.phonenum is not None
    
   

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}','{self.balance}')"


    def get_reset_token(self, expires_sec = 1800):
        s= Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s= Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def _get_twilio_verify_client():
        return Client(
            current_app.config['TWILIO_ACCOUNT_SID'],
            current_app.config['TWILIO_AUTH_TOKEN']).verify.services(
                current_app.config['TWILIO_VERIFY_SERVICE_ID'])


    def request_verification_token(phone):
        verify = _get_twilio_verify_client()
        try:
            verify.verifications.create(to=phone, channel='sms')
        except TwilioException:
            verify.verifications.create(to=phone, channel='call')


    def check_verification_token(phone, token):
        verify = _get_twilio_verify_client()
        try:
            result = verify.verification_checks.create(to=phone, code=token)
        except TwilioException:
            return False
        return result.status == 'approved'    

    

class Post(db.Model):
    id = db.Column(db.Integer,primary_key= True)
    username = db.Column(db.String(100), nullable=True)
    #sento= db.Column(db.String(100),nullable=True)
    amount = db.Column(db.Numeric(10,2),nullable=True)
    note = db.Column(db.Text, nullable=True)
    date_posted= db.Column(db.DateTime, nullable = False,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)


 



    
    
    

    def __repr__(self):
        
        return f"Post('{self.username}','{self.date_posted}',{self.amount}')"
