def gerar_ranking(jogos):
    ranking = {}

    for jogo in jogos:
        for jogador, kills in jogo.mortes.items():
            if jogador not in ranking:
                ranking[jogador] = 0

            ranking[jogador] += kills

    ranking_ordenado = dict(sorted(ranking.items(), key=lambda item: item[1], reverse=True))

    return ranking_ordenado