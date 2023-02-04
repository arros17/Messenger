class UserList:

    __users = {}

    def save(self, user):
        self.__users[user.getLogin()] = user

    def updateIp(self, ip, login):
        user = self.findUserByLogin(login)
        user.setIp(ip)
        self.save(user)

    def delete(self, login):
        self.__users.pop(login)

    def findUserByLogin(self, login):
        return self.__users.get(login)