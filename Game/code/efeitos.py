import pygame
import os
import random
from settings import *

pygame.init()
pygame.mixer.init()

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

# Função para carregar uma imagem da pasta assets/imagens
def carregar_imagem(nome_arquivo, redimensionar = None):
    caminho = os.path.join('assets', 'imagens', nome_arquivo)
    imagem = pygame.image.load(caminho).convert_alpha()
    
    if redimensionar:
        imagem = pygame.transform.scale(imagem, redimensionar)

    return imagem

# Função para carregar um som da pasta assets/imagens
def carregar_som(nome_arquivo):
    caminho = os.path.join('assets', 'sons', nome_arquivo)

    return pygame.mixer.Sound(caminho)

# Sprites com suas respectivas imagens frente e costas
SPRITES = {
    'mago': {
        'frente': carregar_imagem('mago_frente.png', (150, 150)),
        'costas': carregar_imagem('mago_costas.png', (150, 150))
    },
    'guerreiro': {
        'frente': carregar_imagem('guerreiro_frente.png', (150, 150)),
        'costas': carregar_imagem('guerreiro_costas.png', (150, 150))
    },
    'arqueiro': {
        'frente': carregar_imagem('arqueiro_frente.png', (150, 150)),
        'costas': carregar_imagem('arqueiro_costas.png', (150, 150))
    }
}

MAPAS = {
    'floresta': carregar_imagem('mapa_floresta.png', (LARGURA_TELA, ALTURA_TELA)),
    'castelo': carregar_imagem('mapa_floresta.png', (LARGURA_TELA, ALTURA_TELA)),
    'caverna': carregar_imagem('mapa_floresta.png', (LARGURA_TELA, ALTURA_TELA))
}

MUSICAS = {
    'floresta': [
        os.path.join('assets', 'musicas', 'musica_floresta1.mp3'), 
        os.path.join('assets', 'musicas', 'musica_floresta2.mp3')
    ],
    'castelo': [
        os.path.join('assets', 'musicas', 'musica_castelo_1.wav'), 
        os.path.join('assets', 'musicas', 'musica_castelo_2.mp3')
    ],
    'caverna': [
        os.path.join('assets', 'musicas', 'musica_caverna_1.mp3'),
        os.path.join('assets', 'musicas', 'musica_caverna_2.wav')
    ]
}

SONS = {
    'ataque': carregar_som('ataque.wav'),
    'dano': carregar_som('dano.mp3'),
    'clique': carregar_som('clique.wav'),
}

FONTE_DANO = pygame.font.Font(os.path.join('assets', 'fontes', 'fonte_pixel.ttf'), 36)


def tocar_musicas_por_mapa(nome_mapa):
    # Escolhe uma música aleatória do mapa e toca em loop

    if nome_mapa in MUSICAS:
        listaDeMusicas = MUSICAS[nome_mapa]
        musica_escolhida = random.choice(listaDeMusicas)

        pygame.mixer.music.load(musica_escolhida)
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)

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


# Função o personagem mudar de cor quando receber dano
def efeito_mudar_cor(sprite_original, cor_efeito, tempo_inicio):
    tempo_atual = pygame.time.get_ticks()
    tempo_decorrido = tempo_atual - tempo_inicio
    
    DURACAO_EFEITO_COR = 300 

    if tempo_decorrido > DURACAO_EFEITO_COR:
        return None

    superficie_cor = pygame.Surface(sprite_original.get_size(), pygame.SRCALPHA)
    superficie_cor.fill(cor_efeito)
    
    superficie_cor.blit(sprite_original, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    
    return superficie_cor

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
