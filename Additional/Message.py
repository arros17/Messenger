class Message:
    __sender = ''
    __receiver = ''
    __text = ''

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