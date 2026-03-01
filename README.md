# Quake Log Parser API

Este projeto foi desenvolvido com o objetivo de analisar o arquivo games.log do Quake e disponibilizar as informações das partidas por meio de uma API simples utilizando Flask.

A aplicação lê o arquivo de log, processa os dados e permite consultar as estatísticas de cada jogo através de rotas HTTP. Além disso, existe um arquivo menu.py que permite visualizar os resultados diretamente pelo terminal.

### Objetivo do Projeto

O sistema identifica as partidas presentes no arquivo de log e calcula:

 - Total de mortes por partida;

 - Lista de jogadas e jogadores;

 - Número de mortes por jogador;

 - Ranking geral consolidado.


### Como a Solução Funciona:

1 - O arquivo games.log é lido linha por linha.

2 - Quando uma nova partida é identificada, é criado um novo objeto para armazenar seus dados.

3 - A cada evento de morte:

 - O total de mortes da partida é incrementado.

 - Os jogadores são registrados.

 - A quantidade de mortes por jogador é atualizada.

 - Caso a morte seja causada pelo world, o jogador perde 1 ponto.

4 - Após o processamento completo, os dados ficam disponíveis para:

 - Consulta via API (api.py)

 - Visualização no terminal através do menu.py

A separação entre processamento do log, geração de ranking e camada HTTP foi feita para deixar o código mais organizado e facilitar futuras melhorias.

Estrutura do Projeto:

    ├── api.py
    ├── analisador.py
    ├── ranking.py
    ├── menu.py
    ├── games.log
    └── README.md

 - analisador.py → Responsável pela leitura e processamento do log

 - ranking.py → Responsável pela geração do ranking geral

 - api.py → Responsável pelas rotas da API

 - menu.py → Interface simples via terminal para exibir os resultados do analisador e do ranking

Setup
1. Clonar o repositório:

    git clone <url-do-repositorio>
    cd <nome-do-projeto>
    
2. (Opcional) Criar ambiente virtual:

    python -m venv venv

Ativar:

 - Windows:
 
    venv\Scripts\activate

 - Linux/Mac:
 
    source venv/bin/activate
   
3. Instalar dependências:

    pip install flask

4. Executando o Projeto
 - Rodar a API:
 
    python api.py

 - A aplicação ficará disponível em:

    http://127.0.0.1:5000
   
 - Rodar o Menu no Terminal:
 
    python menu.py

O menu exibirá no console os dados processados pelo analisador e o ranking geral.

Rotas Disponíveis:

    GET /games → Retorna todas as partidas
    
    GET /game/<id> → Retorna uma partida específica
    
    GET / → Interface simples para buscar jogo por ID

