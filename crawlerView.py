import json
import datetime
import path 
import sys
import os
from flask import Flask, request, json, Blueprint
from flask_cors import CORS, cross_origin
import time
from crawler2 import *


chatBot = Blueprint('chatBot',__name__, url_prefix='/chatBot')
@chatBot.route("/ask",methods=["POST"])

def askQuestion():
    data=json.loads(request.data)
    time.sleep(1)
    askedquestion=data["question"]
    try:
        finalResponce={"status": "Success", "message": answer_question(df,question=askedquestion)}
    except:
        finalResponce={'status':"Failed","message":"Something went wrong"}
    return finalResponce

# chatBot.run()
