from flask import Flask, Blueprint, Response, request
import json
from app.controllers import filme_controller

routes = Blueprint("routes", __name__)

@routes.route("/")
def home():
    return Response(json.dumps({"message": "API disponível! Use /filmes para CRUD."}))

@routes.route("/filmes", methods=["GET"])
def get_filmes():
    return Response(json.dumps(filme_controller.listar_filmes(),
        ensure_ascii=False, indent=4), 
        mimetype='application/json'
    )

@routes.route("/filmes/<int:filme_id>", methods=["GET"])
def get_filme(filme_id):
    filme = filme_controller.obter_filme_por_id(filme_id)
    if not filme:
        return Response(json.dumps({"error": "Filme não encontrado"})), 404
    
    # Usa json.dumps para manter a ordem
    return Response(
        json.dumps(filme, ensure_ascii=False, indent=4),
        mimetype='application/json'
    )

@routes.route("/filmes", methods=["POST"])
def post_filme():
    data = request.json
    resultado = filme_controller.adicionar_filme(data)
    json_str = json.dumps(resultado, ensure_ascii=False)
    return Response(json_str, status=201, mimetype='application/json')

@routes.route("/filmes/<int:filme_id>", methods=["PUT"])
def put_filme(filme_id):
    data = request.json
    filme = filme_controller.atualizar_filme(filme_id, data)
    if not filme:
        return Response(json.dumps({"error": "Filme não encontrado"})), 404
    return Response(json.dumps(filme))

@routes.route("/filmes/<int:filme_id>", methods=["DELETE"])
def delete_filme(filme_id):
    result = filme_controller.deletar_filme(filme_id)
    if not result:
        return Response(json.dumps({"error": "Filme não encontrado"})), 404
    return Response(json.dumps({"message": "Filme deletado com sucesso"}))
