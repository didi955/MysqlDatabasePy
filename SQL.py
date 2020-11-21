from mysql.connector.pooling import *


def update(connection: PooledMySQLConnection, qry: str):
    cursor = connection.cursor()
    cursor.execute(qry)
    cursor.close()


def query(connection: PooledMySQLConnection, qry: str) -> list:
    cursor = connection.cursor()
    cursor.execute(qry)
    rs = cursor.fetchall()
    cursor.close()
    return rs