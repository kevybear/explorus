#app.py 
from apis import *
from flask import jsonify
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('index.html', name=name)


@app.route("/about")
def about():
	return getPointsCoor("New York").content

if __name__ == "__main__":
    app.run(debug=True)