from analisador import GamesLog
from ranking import gerar_ranking

parser = GamesLog('games.log')
parser.analisador()

print("Relatótio por jogo")
for i, jogo in enumerate(parser.jogos):
            print(f'Jogador_{i + 1}')
            print({
                'total_mortes:' : jogo.total_mortes,
                'Jogador:' : jogo.jogadores,
                'Mortes:' : jogo.mortes
            })
            print('-' * 30)

ranking = gerar_ranking(parser.jogos)
print("RANKING GERAL")
for jogador, mortes in ranking.items():
    print(f"{jogador} - {mortes} mortes")

    