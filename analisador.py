class Jogador:
    def __init__(self):
        self.total_mortes = 0
        self.jogadores = []
        self.mortes = {}

    def add_jogador(self, nome):
        if nome not in self.jogadores:
            self.jogadores.append(nome)
            self.mortes[nome] = 0

    def add_morte(self, killer, victim):
        self.total_mortes += 1

        if victim not in self.jogadores:
            self.add_jogador(victim)

        if killer == '<world>':
            self.mortes[victim] -= 1
        else:
            if killer not in self.jogadores:
                self.add_jogador(killer)
                
            self.mortes[victim] += 1

class GamesLog:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.jogos = []

    def analisador(self): 
        current_game = None

        with open(self.caminho_arquivo, 'r') as arquivo:
            for linha in arquivo:
                if 'InitGame' in linha:
                    current_game = Jogador()
                    self.jogos.append(current_game)

                elif 'Kill:' in linha:
                    partes = linha.split(':')

                    info = partes[3].strip()
                    info = info.split('killed')

                    killer = info[0].strip()
                    resto = info[1].split('by')
                    victim = resto[0].strip()

                    current_game.add_morte(killer, victim)

    def get_resultado(self):
        resultados = {}

        for i, jogo in enumerate(self.jogos):
            resultados[f'jogador_{i + 1}'] = {'total_mortes' : jogo.total_mortes, 
                                              'jogadores' : jogo.jogadores,
                                              'mortes' : jogo.mortes}

        return resultados
    
parser = GamesLog('games.log')
parser.analisador()

resultado = parser.get_resultado()
for nome_jogo, dados in resultado.items():
    print(nome_jogo)
    print('total_mortes:', dados['total_mortes'])
    print('jogadores:', dados['jogadores'])
    print('mortes:', dados['mortes'])
    print()