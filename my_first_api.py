from connection import create_connection, close_connection, MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, PORT, load_dotenv
from flask import Flask
import json
from json import JSONEncoder


app = Flask(__name__)  # ----> Forma padrão de inicializar o Flask.


class CustomEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


@app.route('/')
def homepage():
    return 'API online. Acesse /filmes para ver os filmes disponíveis'


@app.route('/filmes')
def filmes():
    conexao = create_connection(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, PORT)
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM filmes')
    dados = cursor.fetchall()
    lista = list()
    movies = list()
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
