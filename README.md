# RPG Realm

Este é um projeto de jogo RPG simples desenvolvido em Python usando a biblioteca Pygame.

## Funcionalidades Implementadas

- **Sistema de Combate por Turnos**: Os jogadores se enfrentam em um combate baseado em turnos, onde cada personagem tem habilidades e atributos únicos.
- **Seleção de Personagens**: Escolha entre diferentes classes de personagens (Mago, Guerreiro, Arqueiro), cada uma com suas próprias estatísticas e ataques especiais.
- **Efeitos Visuais**: Implementação de efeitos visuais para indicar dano e outras interações no jogo.
- **Músicas de Fundo**: Músicas ambientais que mudam de acordo com o mapa atual, proporcionando uma experiência imersiva.
- **Efeito de Mudança de Cor ao Receber Dano**: Personagens mudam de cor temporariamente ao receber dano, fornecendo feedback visual claro.

## Como Rodar o Jogo

Para rodar este jogo, siga os passos abaixo:

1. **Pré-requisitos**:
   Certifique-se de ter o Python 3.x instalado em seu sistema. Você também precisará da biblioteca `pygame`.

   Para instalar o `pygame`, abra seu terminal ou prompt de comando e execute:

   ```bash
   pip install pygame
   ```

2. **Clonar o Repositório (ou baixar os arquivos)**:
   Se você recebeu os arquivos diretamente, pule esta etapa. Caso contrário, clone o repositório do projeto:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd RPG-Realm
   ```

3. **Executar o Jogo**:
   Navegue até o diretório principal do projeto (onde o arquivo `main.py` está localizado) e execute o seguinte comando:
   ```bash
   python main.py
   ```

## Estrutura do Projeto

- `main.py`: O ponto de entrada principal do jogo, onde a lógica do jogo é iniciada e o loop principal é executado.
- `classes.py`: Contém as definições das classes dos personagens (Mago, Guerreiro, Arqueiro) e a lógica de combate.
- `efeitos.py`: Gerencia o carregamento de recursos (imagens, sons, músicas) e define funções para efeitos visuais e sonoros.
- `settings.py`: Armazena configurações globais do jogo, como dimensões da janela, cores e dados de ataques.
- `ui.py`: Responsável pela interface do usuário, incluindo a exibição de informações dos personagens e opções de combate.
- `Timer.py`: Uma classe utilitária para gerenciar temporizadores no jogo.
- `log.py`: Um módulo para registrar eventos do jogo em um arquivo de log.
- `assets/`: Diretório contendo todos os recursos do jogo (imagens, sons, músicas, fontes).

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias e correções de bugs.
