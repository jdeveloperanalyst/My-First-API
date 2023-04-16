from connection import create_connection, close_connection
from flask import Flask
from credentials import credenciais
import json
from json import JSONEncoder

lista = list()
movies = list()

app = Flask(__name__)  # ----> Forma padrão de inicializar o Flask.


class CustomEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


@app.route('/')
def homepage():
    return 'API online. Acesse /filmes para ver os filmes disponíveis'


@app.route('/filmes')
def filmes():
    conexao = create_connection(credenciais['host'], credenciais['user'], credenciais['password'], credenciais['database'])
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM filmes')
    dados = cursor.fetchall()
    for f in dados:
        lista.append(f)
    for l in lista:
        movies.append(
            {'Id': l[0],
             'Título': l[1],
             'Ano': l[2],
             'Direção': l[3]})
    cursor.close()
    close_connection(conexao)
    return json.dumps(movies, indent=4, cls=CustomEncoder, ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=True)  # ----> Comando para rodar a API.
