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
    j = json.dumps(request.json)
    x = json.loads(j, object_hook=lambda d: SimpleNamespace(**d))
    message.setText(x._Message__text)
    message.setReceiver(x._Message__receiver)
    message.setSender(x._Message__sender)
    print(message.getReceiver(), message.getSender(), message.getText())
    return jsonify(), 200

# TEST ===============================================================================

arros = User()
arros.setLogin('arros')
arros.setPort('8365')
gorshok = Message()
gorshok.setText('arr')
gorshok.setSender('arros')
gorshok.setReceiver('uu')


with app.app_context():
    enterOnline(json.dumps(arros.__dict__))
    # sendMessage(json.dumps(gorshok.__dict__))
    time.sleep(2)
    # disconnect()
app.run(port= 8365)