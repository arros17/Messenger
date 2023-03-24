import json
class Message:
    __sender = ''
    __receivers = ''
    __text = ''

    def toJSON(self):
        return json.dumps(obj=self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def getSender(self):
        return self.__sender

    def getReceiver(self):
        return self.__receivers

    def getText(self):
        return self.__text

    def setSender(self, sender):
        self.__sender = sender

    def setReceiver(self, receivers):
        self.__receivers = receivers

    def setText(self, text):
        self.__text = text
