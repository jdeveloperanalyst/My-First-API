import mysql.connector
from flask import Flask, jsonify

credentials = {'host': 'localhost',
               'user': 'root',
               'password': '',
               'database': 'devflix'}


def create_connection(host, user, password, database):
    return mysql.connector.connect(host=host, user=user, password=password, database=database)


def close_connection(con):
    return con.close()


app = Flask(__name__)  # ----> Forma padrão de inicializar o Flask.


@app.route('/')
def homepage():
    return 'API online. Acesse /filmes para ver os filmes disponíveis'


@app.route('/filmes')
def filmes():
    conexao = create_connection(credentials['host'], credentials['user'], credentials['password'], credentials['database'])
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM filmes')
    dados = cursor.fetchall()
    response = {'Filmes': dados}
    cursor.close()
    close_connection(conexao)
    return jsonify(response)


app.run()  # ----> Comando para rodar a API.
