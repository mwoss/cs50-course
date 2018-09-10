from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'm\x15C\xe7\xcd)\xf0\x98"\x0c\x87E\x15\xf5\'\xd7\x03\xa9\x89\x1a\x80W\x95s\xc6\x1e7d;\xc6'
socketio = SocketIO(app)

from webchat import views
