import os
import sys
import path
from flask import Flask, request, json, Blueprint
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent)

from crawlerView import *

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_main():
    return "Hello!"

app.register_blueprint(chatBot)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)