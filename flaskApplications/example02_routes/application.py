from flask import Flask 

application = Flask(__name__)

@application.route("/")
def index():
	return "Home Page"

@application.route("/hello")
def hello():
	return "Hello World!"

@application.route("/members/name/<string:name>")
def member_names(name):
	return "Hello "+name 

@application.route("/members/age/<int:age>")
def member_age(age):
	return "Age: "+str(age) 

if __name__ == '__main__':
	application.run(port=80,debug=True)