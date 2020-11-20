from enum import Enum
from DatabaseCredentials import DatabaseCredentials
from DatabaseAccess import DatabaseAccess


class DatabaseManager(Enum):
    BDD1 = (DatabaseCredentials("*****", "****", "*********", "*********", 3306))

    def __init__(self, credentials: DatabaseCredentials):
        self.databaseAccess = DatabaseAccess(credentials)

    def getDatabaseAccess(self):
        return self.databaseAccess

    @staticmethod
    def initAllDatabaseConnections():
        for key in DatabaseManager.__members__.values():
            key.databaseAccess.initPool()

    @staticmethod
    def closeAllDatabaseConnection():
        for key in DatabaseManager.__members__.values():
            key.databaseAccess.stopPool()
