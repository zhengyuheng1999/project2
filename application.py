import os
import requests

from flask import Flask, render_template, jsonify, request
from flask import session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import *
from sqlalchemy import and_, or_
from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods = ["GET","POST"])
def chat():
    return render_template("chat.html")

@socketio.on("submit word")
def talk(data):
    name = data["name"]
    sentence = data["sentence"]
    message = name+':   '+sentence
    emit("say a sentence", {"message": message}, broadcast=True)

#if __name__ == '__main__':
 #  socketio.run(app, debug=True)