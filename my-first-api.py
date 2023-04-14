import mysql.connector
from flask import Flask

credentials = {'host': 'localhost',
               'user': 'root',
               'password': '',
               'database': 'devflix'}


def create_connection(host, user, password, database):
    return mysql.connector.connect(host=host, user=user, password=password, database=database)


def close_connection(con):
    return con.close()


app = Flask(__name__)  # ----> Forma padrão de inicializar o Flask.


app.run()  # ----> Comando para rodar a API
# conexao = create_connection(credentials['host'], credentials['user'], credentials['password'], credentials['database'])
# cursor = conexao.cursor()
# cursor.execute('SELECT * FROM filmes')
# dados = cursor.fetchall()
# result = str(dados).split()
# for item in result:
#     print(item, end='')
# close_connection(conexao)
