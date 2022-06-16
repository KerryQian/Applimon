from flask import Flask
import requests
from rhino3dm import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hello from kerry"
