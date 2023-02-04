class User:
    __login = ''
    __ip = ''
    __port = ''

    def getLogin(self):
        return self.__login

    def getIp(self):
        return self.__ip

    def setLogin(self, login):
        self.__login = login

    def setIp(self, ip):
        self.__ip = ip

    def getPort(self):
        return self.__port

    def setPort(self, port):
        self.__port = port