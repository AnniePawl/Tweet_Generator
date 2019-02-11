
from flask import Flask
from flask import render_template


# Instance of Flask class
app = Flask(__name__)

# Tell Flask what url should trigger function, return message
@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/testing')
