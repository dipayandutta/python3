from flask import Flask , render_template 

application = Flask(__name__)

@application.route("/")
def index():
	return "Flask application"

@application.route("/members/name/<string:name>")
def members(name):

	
	return render_template('page.html',name=name,)

if __name__ == '__main__':
	application.run(debug=True,port=80)