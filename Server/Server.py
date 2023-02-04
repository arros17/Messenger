import json
from types import SimpleNamespace
import http.client
import sys
sys.path.append('../Additional')
from flask import Flask, request, abort, jsonify
from UserList import UserList
from user import User
app = Flask(__name__)   # Инстанцирование класса приложения Flask
db = UserList()

@app.route('/msg', methods=['POST'])
def redirectMessage():
    if not request.json or not "receiver" in request.json:
        abort(400)

    if db.findUserByLogin(request.json['receiver']):
        sendMessage(request.json)
        return jsonify(), 200
    else:
        return jsonify('User ' + request.json['receiver'] + ' is not online'), 200
@app.route('/connect', methods=['POST'])
def userConnected():
    user = User()
    # user.setLogin(request.json['login'])
    print(request.json)
    x = json.loads(request.json, object_hook=lambda d: SimpleNamespace(**d))
    user.setLogin(x._User__login)
    user.setPort(x._User__port)
    user.setIp(request.json.remote_addr)
    saveUser(user)

    return jsonify(), 200

def userDisconnect(user):
    db.delete(user)

def sendMessage(message):
    receiverIp = db.findUserByLogin(message['receiver']).getIp()
    connection = http.client.HTTPConnection(receiverIp, 8100, timeout=10)
    headers = {'Content-type': 'application/json'}
    messageObject = {
        'sender' : message['sender'],
        'message' : message['message'],
        'receiver' : message['receiver']
    }
    json_data = json.dumps(messageObject)
    connection.request('POST', '/message', json_data, headers)
def saveUser(user):
    db.save(user)

app.run()
