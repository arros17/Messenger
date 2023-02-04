import http.client
import json
import sys
sys.path.append('../Additional')
from flask import jsonify, Flask, current_app
from user import User

app = Flask(__name__)


def sendMessage(sender, receiver, message):
    connection = http.client.HTTPConnection('localhost', 5000, timeout=10)
    headers = {'Content-type': 'application/json'}
    messageObject = {
        'sender': sender,
        'receiver': receiver,
        'message': message
    }
    json_data = json.dumps(messageObject)
    connection.request('POST', '/message', json_data, headers)
    response = connection.getresponse()

def enterOnline(sender):
    connection = http.client.HTTPConnection('localhost', 5000, timeout=10)
    headers = {'Content-type': 'application/json'}
    json_data = json.dumps(sender)
    connection.request('POST', '/connect', json_data, headers)

arros = User()
arros.setLogin('arros')

with app.app_context():
    enterOnline(json.dumps(arros.__dict__))
# sendMessage('lolo', 'arr', 'fff')