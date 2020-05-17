from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
	text = request.form['Push ups']
	print(text)
	return render_template("index.html")