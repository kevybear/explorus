#app.py 
from apis import *
from flask import jsonify
from flask import Flask
from flask import render_template, request
from instagram import *
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello(name=None):

	# get city
	# run algorithm
	# listPics = ['url', 'url1']
	myCity = None
	if request.method == 'POST':
		myCity = request.form['search']
		print myCity
	
		listPics = getPhotos(myCity)
		c = []
		for x in listPics:
			if x[1] != []:
				temp = x[1][0].get_low_resolution_url()
				
				c.append(temp)
		print c
		return render_template('index.html', listPics=c, name=myCity)
	return render_template('index.html', name=name)




@app.route("/about")
def about():
	return getPointsCoors("New York")

if __name__ == "__main__":
    app.run(debug=True)