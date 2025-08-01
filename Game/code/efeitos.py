import pygame
import random
from settings import *
from concurrent.futures import ThreadPoolExecutor

pygame.init()
pygame.mixer.init()

tela = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Cria um pool de threads para carregamento paralelo
executor = ThreadPoolExecutor(max_workers=4) # Pode ajustar o número de workers

# Função para carregar uma imagem da pasta assets/imagens
def carregar_imagem(nome_arquivo, redimensionar = None):
    caminho = os.path.join(BASE_DIR, 'assets', 'imagens', nome_arquivo)
    try:
        imagem = pygame.image.load(caminho).convert_alpha()
        if redimensionar:
            imagem = pygame.transform.scale(imagem, redimensionar)
        return imagem
    except Exception as e:
        print(f"Erro ao carregar imagem {nome_arquivo}: {e}")
        return pygame.Surface((100, 100)) # Retorna uma superfície vazia em caso de erro

# Função para carregar um som da pasta assets/imagens
def carregar_som(nome_arquivo):
    caminho = os.path.join(BASE_DIR, 'assets', 'sons', nome_arquivo)
    try:
        return pygame.mixer.Sound(caminho)
    except Exception as e:
        print(f"Erro ao carregar som {nome_arquivo}: {e}")
        return None # Retorna None em caso de erro

# Funções auxiliares para submeter tarefas ao executor
def submit_carregar_imagem(nome_arquivo, redimensionar=None):
    return executor.submit(carregar_imagem, nome_arquivo, redimensionar)

def submit_carregar_som(nome_arquivo):
    return executor.submit(carregar_som, nome_arquivo)

# Submete o carregamento de todos os assets em paralelo
# Sprites com suas respectivas imagens frente e costas
SPRITES_FUTURES = {
    'mago': {
       'frente': submit_carregar_imagem('mago_frente.png', (150, 150)),
       'costas': submit_carregar_imagem('mago_costas.png', (300, 300))
    },
    'guerreiro': {
       'frente': submit_carregar_imagem('guerreiro_frente.png', (150, 150)),
       'costas': submit_carregar_imagem('guerreiro_costas.png', (300, 300))
    },
    'arqueiro': {
       'frente': submit_carregar_imagem('arqueiro_frente.png', (150, 150)),
       'costas': submit_carregar_imagem('arqueiro_costas.png', (300, 300))
    },
}

MAPAS_FUTURES = {
    'floresta': submit_carregar_imagem('mapa_floresta.png', (WINDOW_WIDTH, WINDOW_HEIGHT)),
    'castelo': submit_carregar_imagem('mapa_floresta.png', (WINDOW_WIDTH, WINDOW_HEIGHT)),
    'caverna': submit_carregar_imagem('mapa_floresta.png', (WINDOW_WIDTH, WINDOW_HEIGHT))
}

MUSICAS = {
    'floresta': [
        os.path.join(BASE_DIR, 'assets', 'musicas', 'musica_floresta1.mp3'), 
        os.path.join(BASE_DIR, 'assets', 'musicas', 'musica_floresta2.mp3'),
        os.path.join(BASE_DIR, 'assets', 'musicas', 'musica_castelo1.wav'), 
        os.path.join(BASE_DIR, 'assets', 'musicas', 'musica_castelo2.mp3'),
        os.path.join(BASE_DIR, 'assets', 'musicas', 'musica_caverna1.mp3'),
        os.path.join(BASE_DIR, 'assets', 'musicas', 'musica_caverna2.wav')
    ]
}

SONS_FUTURES = {
    'ataque': submit_carregar_som('ataque.wav'),
    'dano': submit_carregar_som('dano.mp3'),
    'clique': submit_carregar_som('clique.wav'),
}

# Aguarda a conclusão de todas as tarefas e obtém os resultados
SPRITES = {k: {sk: sf.result() for sk, sf in v.items()} for k, v in SPRITES_FUTURES.items()}
MAPAS = {k: f.result() for k, f in MAPAS_FUTURES.items()}
SONS = {k: f.result() for k, f in SONS_FUTURES.items()}

FONTE_DANO = pygame.font.Font(os.path.join(BASE_DIR, 'assets', 'fontes', 'PressStart2P-Regular.ttf'), 36)


def tocar_musicas_por_mapa(nome_mapa):
    # Escolhe uma música aleatória do mapa e toca em loop

    if nome_mapa in MUSICAS:
        listaDeMusicas = MUSICAS[nome_mapa]
        musica_escolhida = random.choice(listaDeMusicas)
        try:
            pygame.mixer.music.load(musica_escolhida)
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1)
        except pygame.error as e:
            print(f"Erro ao carregar ou tocar música {musica_escolhida}: {e}")

def tocar_som(nome_som):
    if SONS[nome_som]:
        SONS[nome_som].play()

# Função para mostrar um número de dano acima do personagem

def mostrar_dano(alvo_rect, texto_dano):
    texto_surface = FONTE_DANO.render(str(texto_dano), True, (255, 0, 0))
    texto_rect = texto_surface.get_rect()
    texto_rect.centerx = alvo_rect.centerx
    texto_rect.bottom = alvo_rect.top - 5

    tela.blit(texto_surface, texto_rect)


def animacao_impulso_ataque(atacante_rect, tempo_inicio_impulso, direcao_personagem):
    tempo_atual = pygame.time.get_ticks()
    tempo_decorrido = tempo_atual - tempo_inicio_impulso
    
    DURACAO_IMPULSO = 200
    DISTANCIA_IMPULSO = 15

    if tempo_decorrido > DURACAO_IMPULSO:
        return None

    fase = tempo_decorrido / DURACAO_IMPULSO

    deslocamento_x = 0
    if fase <= 0.5:
        deslocamento_x = DISTANCIA_IMPULSO * (fase / 0.5)
    else:
        deslocamento_x = DISTANCIA_IMPULSO * (1 - ((fase - 0.5) / 0.5))

    if direcao_personagem == 'costas':
        return deslocamento_x
    else: # 'frente'
        return -deslocamento_x


