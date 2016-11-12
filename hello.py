#app.py 

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('index.html', name=name)


@app.route("/about")
def about():
	return "hey, this is my page"

if __name__ == "__main__":
    app.run(debug=True)