import mysql
from mysql.connector import pooling
from mysql.connector import Error
from DatabaseCredentials import *


class DatabaseAccess:

    connection = None

    def __init__(self, credentials: DatabaseCredentials):
        self.credentials = credentials

    def setupPoolingConnection(self):
        try:
            connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="pool1",
                                                                          pool_size=10,
                                                                          pool_reset_session=True,
                                                                          host=self.credentials.host,
                                                                          database=self.credentials.dbName,
                                                                          user=self.credentials.user,
                                                                          password=self.credentials.password,
                                                                          port=self.credentials.port)

            self.connection = connection_pool.get_connection()

        except Error as e:
            print("Error while connecting to MySQL using Connection pool ", e)

    def getConnection(self) -> mysql.connector.pooling.PooledMySQLConnection:
        return self.connection

    def initPool(self):
        self.setupPoolingConnection()

    def stopPool(self):
        self.connection.close()
