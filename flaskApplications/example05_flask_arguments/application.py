from flask import Flask , render_template

application = Flask(__name__)

@application.rouet("/")
def index():
	return "Hello World!"

@application.route("/members/name/<string:name>")
def members(name):

	quotes = []

  randomNUmber = randint(0,len(quotes-1))
  quote = quotes[randomNUmber]

  return render_template('page.html',**locals())


if __name__ == '__main__':
	application.run(debug=True,port=80)