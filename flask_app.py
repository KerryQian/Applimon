from flask import Flask
from rhino3dm import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hello from kerry test 1"
