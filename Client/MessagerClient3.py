import http.client
import json
import sys
import time
sys.path.append('../Additional')
from flask import jsonify, Flask, current_app, request
from user import User
from Message import Message
from types import SimpleNamespace

app = Flask(__name__)
myLogin = 'arros'

def sendMessage(message):
    connection = http.client.HTTPConnection('localhost', 5000, timeout=10)
    headers = {'Content-type': 'application/json'}
    json_data = json.dumps(message)
    connection.request('POST', '/msg', json_data, headers)
    response = connection.getresponse()
    print(response.getcode())


def enterOnline(sender):
    connection = http.client.HTTPConnection('localhost', 5000, timeout=10)
    headers = {'Content-type': 'application/json'}
    json_data = json.dumps(sender)
    try:
        connection.request('POST', '/connect', json_data, headers)
    except ConnectionRefusedError as e:
        print('server offline')


def disconnect():
    connection = http.client.HTTPConnection('localhost', 5000)
    headers = {'Content-type': 'application/json'}
    json_data = json.dumps(myLogin)
    connection.request('POST', '/disconnect', json_data, headers)


@app.route('/message', methods=['POST'])
def receiveMessage():
    message = Message()
    print(request.json)
    tmp = json.dumps(request.json)
    x = json.loads(tmp, object_hook=lambda d: SimpleNamespace(**d))
    message.setText(x._Message__text)
    message.setReceivers(x._Message__receivers)
    message.setSender(x._Message__sender)
    print(message.getReceivers(), message.getSender(), message.getText())
    return jsonify(), 200





# TEST ===============================================================================

# arros = User()
# arros.setLogin('arros')
# arros.setPort('8365')
gorshok = Message()
gorshok.setText('arrrr')
gorshok.setSender('uu')
gorshok.setReceivers(['arros'])

uu2 = User()
uu2.setLogin('uu2')
uu2.setPort('8367')


with app.app_context():
    enterOnline(json.dumps(uu2.__dict__))
    # sendMessage(json.dumps(gorshok.__dict__))
app.run(port= 8367)