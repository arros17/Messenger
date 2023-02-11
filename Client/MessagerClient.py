import http.client
import json
import sys
sys.path.append('../Additional')
from flask import jsonify, Flask, current_app
from user import User
from Message import Message
app = Flask(__name__)

# TODO: сделать класс Message, поля класса: sender, receiver, message
# TODO: переделать по образу и подобию enterOnline;
def sendMessage(message):
    connection = http.client.HTTPConnection('localhost', 5000, timeout=10)
    headers = {'Content-type': 'application/json'}
    json_data = json.dumps(message)
    connection.request('POST', '/msg', json_data, headers)
    # response = connection.getresponse()

def enterOnline(sender):
    connection = http.client.HTTPConnection('localhost', 5000, timeout=10)
    headers = {'Content-type': 'application/json'}
    json_data = json.dumps(sender)
    connection.request('POST', '/connect', json_data, headers)



# TEST ===============================================================================

arros = User()
arros.setLogin('arros')
arros.setPort('8100')
gorshok = Message()
gorshok.setText('arr')
gorshok.setSender('arros')
gorshok.setReceiver('rec')


with app.app_context():
    enterOnline(json.dumps(arros.__dict__))
    sendMessage(json.dumps(gorshok.__dict__))
