'''
Python Flask Framework login and logout Example application

'''
from flask import Flask,render_template,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField , PasswordField , BooleanField
from wtforms.validators import InputRequired , Email , Length
from flask_sqlalchemy import SQLAlchemy 
from werkzeug.security import generate_password_hash , check_password_hash
from flask_login import LoginManager , UserMixin , login_user , login_required,logout_user,current_user

# initializing the application
application = Flask(__name__)
# setting up the secret key
application.config['SECRET_KEY'] = '123XDASDLAM!@#qDASDA'
# setting up the database url
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////code/python3/flaskApplications/login_test/database.db'
# initializing the bootstrap application
Bootstrap(application)
# initializing the database 
db = SQLAlchemy(application)
# initializing the loginManager
login_manager = LoginManager()
# application init for the login Manager to work on
login_manager.init_app(application)
# view set up
login_manager.login_view  = 'login'


# Creating the database class
# Database table name = User
class User(UserMixin,db.Model):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(15),unique=True)
	email = db.Column(db.String(50),unique=True)
	password = db.Column(db.String(80),unique=True)

# python3
# from application import db
# db.createall()

'''
Login Manager function
'''
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

'''
	LoginForm Derived from the flaskform
'''
class LoginForm(FlaskForm):
	# The username field
	username = StringField('username',validators=[InputRequired(),Length(min=4,max=15)])
	# The password field
	password = PasswordField('password',validators=[InputRequired(),Length(min=8,max=80)])
	# The remember me field
	remember = BooleanField('remember me')

# Registration Form 
class RegisterForm(FlaskForm):
	email = StringField('email',validators=[InputRequired(),Email(message='Invalid'),Length(max=50)])
	username = StringField('username',validators=[InputRequired(),Length(min=4,max=15)])
	password = PasswordField('password',validators=[InputRequired(),Length(min=8,max=80)])

'''
	Home Page of the application
'''
@application.route('/')
def index():
	return render_template('index.html')


# The login route
@application.route('/login',methods=['GET','POST'])
def login():

	form = LoginForm() # Form form object

	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if check_password_hash(user.password,form.password.data):
				login_user(user,remember=form.remember.data)
				return redirect(url_for('dashboard'))

		return '<h1>Invalid username or password </h1>'
		#return '<h1>'+form.username.data + ' '+form.password.data +'</h1>'
	return render_template('login.html',form=form)

# The signup route
@application.route('/signup',methods=['GET','POST'])
def signup():
	form = RegisterForm()

	if form.validate_on_submit():
		hashed_password = generate_password_hash(form.password.data,method='sha256')
		new_user = User(username=form.username.data,email=form.email.data,password=hashed_password)
		db.session.add(new_user)
		db.session.commit()

		return '<h1>New user has created!</h1>'
		#return '<h1>'+form.username.data + form.email.data + form.password.data + '</h1>'
	return render_template('signup.html',form=form)

@application.route('/dashboard')
@login_required # this decorator check if the user is loged in or not
def dashboard():
	return render_template('dashboard.html',name=current_user.username)

# logout method
@application.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))

if __name__ == '__main__':
	application.run(port=5000,debug=True)