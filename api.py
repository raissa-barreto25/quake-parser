from flask import Flask, jsonify, request
from analisador import GamesLog
from ranking import gerar_ranking

app = Flask(__name__)

parser = GamesLog("games.log")
parser.analisador()

@app.route('/game/<int:game_id>', methods=['GET'])
def get_jogo(game_id):
    index = game_id - 1

    if index < 0 or index >= len(parser.jogos):
        return jsonify({'erro':'Game não encontrado'}), 404
    
    jogo = parser.jogos[index]

    resultado = {
        "total_mortes": jogo.total_mortes,
        "jogadores": jogo.jogadores,
        "mortes": jogo.mortes
    }

    return jsonify(resultado)

@app.route('/games')
def home():
    resultado = {}

    for i, jogo in enumerate(parser.jogos):
        resultado[f"game_{i+1}"] = {
            "total_mortes": jogo.total_mortes,
            "jogadores": jogo.jogadores,
            "mortes": jogo.mortes
        }

    return jsonify(resultado)

@app.route('/')
def menu():
    return '''
        <h2>Consultar jogo</h2>
        <form action="/buscar" method="get">
            <label>Digite o ID do jogo:</label>
            <input type="number" name="game_id" required>
            <button type="submit">Buscar</button>
        </form>
    '''

@app.route('/buscar')
def buscar():
    from flask import request

    game_id = int(request.args.get("game_id"))

    if game_id - 1 >= len(parser.jogos) or game_id <= 0:
        return {"erro": "Game não encontrado"}

    jogo = parser.jogos[game_id - 1]

    return {
        "total_mortes": jogo.total_mortes,
        "jogadores": jogo.jogadores,
        "mortes": jogo.mortes
    }

if __name__ == "__main__":
    app.run(debug=True)