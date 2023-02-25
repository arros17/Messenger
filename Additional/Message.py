import json
class Message:
    __sender = ''
    # TODO: сделать массивом
    __receivers = []
    __text = ''
    #
    # def __init__(self, sender, receiver, text):
    #     self.__sender = sender
    #     self.__receiver = receiver
    # #     self.__text = text
    def toJSON(self):
        return json.dumps(obj=self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def getSender(self):
        return self.__sender

    def getReceivers(self):
        return self.__receivers

    def getText(self):
        return self.__text

    def setSender(self, sender):
        self.__sender = sender

    def setReceivers(self, receivers):
        self.__receivers = receivers

    def setText(self, text):
        self.__text = text

    def addReceiver(self, receiver):
        self.__receivers.append(receiver)