# FLASK QUICKSTART

from flask import Flask
# Instance of Flask class
app = Flask(__name__)

# Tell Flask what url should trigger function, return message
@app.route('/')
def hello_world():
    return 'Hello, World!'
