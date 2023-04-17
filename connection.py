import mysql.connector


def create_connection(host, user, password, database, port):
    return mysql.connector.connect(host=host, user=user, password=password, database=database, port=port)


def close_connection(con):
    return con.close()
