
class DatabaseCredentials:

    def __init__(self, host: str, user: str, password: str, dbname: str, port: int):
        self.host = host
        self.user = user
        self.password = password
        self.dbName = dbname
        self.port = port

    def getHost(self) -> str:
        return self.host

    def getUser(self) -> str:
        return self.user

    def getPass(self) -> str:
        return self.password

    def getDbName(self) -> str:
        return self.dbName

    def getPort(self) -> int:
        return self.port

    def toURI(self) -> str:
        uri = "jdbc:mysql://" + self.host + ":" + str(self.port) + "/" + self.dbName
        return uri
