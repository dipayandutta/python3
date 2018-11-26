from flask import Flask,flash ,redirect,render_template,request,session,abort


application = Flask (__name__)

@application.route('/')

def index():
	return "Flask Template Learning"

@application.route("/hello/<string:name>")

def hello(name):
	return render_template('page.html',name=name)

if __name__ == '__main__':
	application.run(port=80,debug=True)