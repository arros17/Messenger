class UndeliveredMessages:
    __m = {}                                    # {'receiver': [Message]}

    def getUndeliveredMessages(self):
        return self.__m

    def setUndeliveredMessages(self, m):
        self.__m = m

    def saveUndeliveredMessage(self, message):
        if message.getReceiver() in self.__m:
            self.__m[message.getReceiver()].append(message)
        else:
            self.__m[message.getReceiver()] = [message]

    def getMessagesForReceiver(self, receiver):
        if receiver in self.__m:
            return self.__m[receiver]
        else:
            return []
