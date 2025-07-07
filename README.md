# RPG Realm

## Sobre o Jogo

RPG Realm é um jogo de batalha em turnos desenvolvido em Python com a biblioteca Pygame. Neste jogo, dois jogadores escolhem seus heróis de diferentes classes e se enfrentam em um combate estratégico até que apenas um reste de pé. Gerencie seus pontos de vida e mana, utilize ataques básicos e libere habilidades especiais para garantir a vitória!

## Funcionalidades

-   **Sistema de Combate por Turnos**: Batalhas estratégicas inspiradas em clássicos do gênero, onde cada jogador escolhe sua ação a cada turno.
-   **Seleção de Personagens**: Escolha entre três classes únicas:
    -   **Guerreiro**: Um tanque resistente com alta defesa e pontos de vida.
    -   **Mago**: Focado em causar dano massivo com suas habilidades mágicas.
    -   **Arqueiro**: Um lutador ágil, com alta velocidade e chance de se esquivar de ataques.
-   **Efeitos Visuais e Sonoros**: Para uma imersão completa, o jogo conta com efeitos visuais para feedback de dano, trilha sonora para cada mapa e efeitos sonoros para as ações.
-   **Sistema de Log**: Todas as ações da batalha são salvas no arquivo `battle_log.txt` para análise posterior.

## Como Executar o Jogo

Para rodar o RPG Realm em sua máquina, siga os passos abaixo.

### Requisitos
-   Python 3.x
-   Biblioteca `pygame-ce`

### Instalação
1.  **Instale o `pygame-ce`**: Abra seu terminal ou prompt de comando e execute:
    ```bash
    pip install pygame-ce
    ```
2.  **Obtenha os Arquivos**: Clone o repositório do projeto ou baixe e extraia os arquivos em um diretório de sua preferência.
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    ```
3.  **Execute o Jogo**: Navegue até o diretório raiz do projeto (onde se encontra o arquivo `main.py`) e execute o seguinte comando:
    ```bash
    python main.py
    ```

## Estrutura do Projeto

-   `main.py`: Ponto de entrada do jogo. Controla o game loop, os estados do jogo e a lógica principal da batalha.
-   `classes.py`: Contém as definições das classes dos personagens (`Mago`, `Guerreiro`, `Arqueiro`) e suas mecânicas base (ataque, dano, esquiva).
-   `ui.py`: Gerencia toda a Interface do Usuário (UI), como menus de seleção, barras de status (HP/MP) e a captura de input do jogador.
-   `efeitos.py`: Centraliza o carregamento de todos os assets (imagens, sons) e as funções de efeitos visuais, como o de "piscar" ao levar dano.
-   `settings.py`: Arquivo de configurações globais, como dimensões da janela, cores e o dicionário de ataques.
-   `Timer.py`: Classe utilitária para gerenciar temporizadores de forma organizada.
-   `assets/`: Diretório que contém todas as mídias do jogo (imagens, sons, músicas, fontes).

## Distribuição de Tarefas

A equipe foi dividida com as seguintes responsabilidades principais:

-   **Lucas (Arquiteto de Jogo)**:
    -   Estruturação do motor principal do jogo (game loop, janela, estados).
    -   Implementação da lógica central de combate e turnos.
    -   Integração entre a lógica de backend (`classes.py`) e a interface (`ui.py`).
    -   Gerenciamento e correção de bugs na lógica principal.

-   **Júlia (Desenvolvedora de UI)**:
    -   Desenvolvimento completo do sistema de Interface do Usuário (UI).
    -   Criação dos menus interativos (Seleção de Personagem, Menu de Ações).
    -   Implementação da lógica de exibição de status (barras de HP e MP).
    -   Testes de usabilidade e correção de bugs na interface.

-   **Pedro (Desenvolvedor de Assets e Efeitos)**:
    -   Gestão e curadoria de todos os assets visuais e sonoros (sprites, cenários, fontes, etc.).
    - Implementação do sistema de áudio (músicas de fundo e efeitos sonoros).
    -   Desenvolvimento dos efeitos visuais (feedback de dano, animações).
    -   Criação e manutenção da documentação do projeto (README).

## Créditos

Para o aprendizado sobre a biblioteca Pygame, utilizamos diversas videoaulas, das quais duas foram essenciais para o desenvolvimento deste projeto:

-   [Master Python by making 5 games \[the new ultimate introduction to pygame\]](https://youtu.be/8OMghdHP-zs?si=6hDSZdQh4QtayV3v)
-   [Creating a Pokémon inspired RPG in Python & Pygame](https://youtu.be/fo4e3njyGy0?si=x5lxNSAhV8zXUTnf)

