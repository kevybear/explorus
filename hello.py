#app.py 
from apis import *
from flask import jsonify
from flask import Flask
from flask import render_template
from instagram import *
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):

	# get city
	# run algorithm
	# listPics = ['url', 'url1']
	listPics = getPhotos()
	return render_template('index.html', listPics=listPics)


@app.route("/about")
def about():
	return getPointsCoors("New York")

if __name__ == "__main__":
    app.run(debug=True)