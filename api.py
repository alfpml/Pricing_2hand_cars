from bottle import route, run, get, post, request
from bson.json_util import dumps
import json
import dns
import requests
import mongofnc as mf
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

@route("/")
def index():
    return {'This is the chat sentiment api'}

@get("/<chat_id>/messages")
def getMessages(chat_id):
    """Get messages from a given chat"""
    return dumps(coll.find({'idChat':int(chat_id)}))

@get("/users")
def getUsers():
    """Get all users"""
    return dumps(coll.aggregate([{"$group":{"_id": {"idUser":"$idUser", "userName":"$userName"}}}]))

@get("/<username>/usermessages")
def getUserMessages(username):
    """Gets user messages"""
    return dumps(coll.find({'userName':str(username)},{"text": 1,"_id":0}))

@post('/user/create')
def createuser():
    """New user creation"""
    name = str(request.forms.get("name"))
    new_id = max(user.distinct("idUser")) + 1
    names = list(user.aggregate([{'$project':{'userName':1}}]))

    if name in [n['userName'] for n in names]:
        return "name already in database"
    else:
        new_user = {
            "idUser": new_id,
            "userName": name
        }
        user.insert_one(new_user)
        return f"user_id for {name} is {new_id}"
