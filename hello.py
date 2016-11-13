#app.py 
from apis import *
from flask import jsonify
from flask import Flask
from flask import render_template, request
from instagram import *
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def hello(name=None):

	# get city
	# run algorithm
	myCity = None
	if request.method == 'POST':
		myCity = request.form['search']
		listPics = getPhotos(myCity)
		print myCity
		return render_template('about.html', listPics=listPics, name=myCity)
	return render_template('about.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)