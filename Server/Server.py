import json
from types import SimpleNamespace
import http.client
import sys
sys.path.append('../Additional')
from flask import Flask, request, abort, jsonify
from UserList import UserList
from user import User
from Message import Message
from UndeliveredMessages import UndeliveredMessages
app = Flask(__name__)   # Инстанцирование класса приложения Flask
db = UserList()
undeliveredMessages = UndeliveredMessages()

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
        return jsonify(), 200
    else:
        undeliveredMessages.saveUndeliveredMessage(message)
        return jsonify('User ' + message.getReceiver() + ' is not online'), 200

@app.route('/connect', methods=['POST'])
def userConnected():
    user = User()
    # user.setLogin(request.json['login'])
    x = json.loads(request.json, object_hook=lambda d: SimpleNamespace(**d))
    user.setLogin(x._User__login)
    user.setPort(x._User__port)
    user.setIp(request.remote_addr)
    saveUser(user)
    mes = undeliveredMessages.getMessagesForReceiver(user.getLogin())
    mes.reverse()
    # print(mes)
    while len(mes) != 0:
        sendMessage(mes.pop())

    return jsonify(), 200

@app.route('/disconnect', methods=['POST'])
def userDisconnect():
    db.delete(request.json)
    return jsonify(), 200



def sendMessage(message):
    user = db.findUserByLogin(message.getReceiver())
    connection = http.client.HTTPConnection(user.getIp(), user.getPort(), timeout=10)
    headers = {'Content-type': 'application/json'}
    json_data = message.toJSON()
    try:
        connection.request('POST', '/message', json_data, headers)
    except ConnectionRefusedError as e:
        UndeliveredMessages.saveUndeliveredMessage(message)


def saveUser(user):
    db.save(user)

app.run()
