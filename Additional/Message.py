import json
class Message:
    __sender = ''
    # TODO: сделать массивом
    __receiver = ''
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

    def getReceiver(self):
        return self.__receiver

    def getText(self):
        return self.__text

    def setSender(self, sender):
        self.__sender = sender

    def setReceiver(self, receiver):
        self.__receiver = receiver

    def setText(self, text):
        self.__text = text