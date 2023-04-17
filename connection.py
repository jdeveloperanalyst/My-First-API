import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()  # carrega as variáveis de ambiente do arquivo .env

MYSQL_HOST = os.environ.get('MYSQL_HOST')
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_DB = os.environ.get('MYSQL_DB')
PORT = os.environ.get('PORT')


def create_connection(host, user, password, database, port):
    return mysql.connector.connect(host=host, user=user, password=password, database=database, port=port)


def close_connection(con):
    return con.close()
