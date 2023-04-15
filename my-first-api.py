from connection import create_connection, close_connection
from credentials import credentials
from flask import Flask, jsonify

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
