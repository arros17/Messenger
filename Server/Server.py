import json
from types import SimpleNamespace
import http.client
import sys
sys.path.append('..\\Additional')
from flask import Flask, request, abort, jsonify
from UserList import UserList
from user import User
from Message import Message
app = Flask(__name__)   # Инстанцирование класса приложения Flask
db = UserList()

@app.route('/msg', methods=['POST'])
def redirectMessage():
    if not request.json:
        abort(400)
    message = Message()
    x = json.loads(request.json, object_hook=lambda d: SimpleNamespace(**d))
    message.setText(x._Message__text)
    message.setReceiver(x._Message__receiver)
    message.setSender(x._Message__sender)
    # print(message.getReceiver(), message.getSender(), message.getText())
    if db.findUserByLogin(message.getReceiver()):
        sendMessage(message)
        return jsonify(), 200, print(db.findUserByLogin(message.getReceiver()))
    else:
        return jsonify('User ' + message.getReceiver() + ' is not online'), 200
@app.route('/connect', methods=['POST'])
def userConnected():
    user = User()
    # user.setLogin(request.json['login'])
    print(request.json)
    x = json.loads(request.json, object_hook=lambda d: SimpleNamespace(**d))
    user.setLogin(x._User__login)
    user.setPort(x._User__port)
    user.setIp(request.remote_addr)
    print(user.getIp())
    saveUser(user)

    return jsonify(), 200

def userDisconnect(user):
    db.delete(user)

def sendMessage(message):
    user = db.findUserByLogin(message.getReceiver())
    connection = http.client.HTTPConnection(user.getIp(), user.getPort(), timeout=10)
    headers = {'Content-type': 'application/json'}
    json_data = message.toJSON()
    connection.request('POST', '/message', json_data, headers)


def saveUser(user):
    db.save(user)

app.run()
