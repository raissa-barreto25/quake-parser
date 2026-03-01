from flask import Flask, jsonify
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

@app.route('/')
def menu():
    resultado = {}

    for i, jogo in enumerate(parser.jogos):
        resultado[f"game_{i+1}"] = {
            "total_mortes": jogo.total_mortes,
            "jogadores": jogo.jogadores,
            "mortes": jogo.mortes
        }

    return jsonify(resultado)

if __name__ == "__main__":
    app.run(debug=True)