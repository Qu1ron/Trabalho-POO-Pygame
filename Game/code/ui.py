from settings import *
import os
from classes import *
from efeitos import SONS
from Timer import Timer

class UI:
    def __init__ (self,player1,player2,get_input):

        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(os.path.join(os.path.dirname(__file__), '..', 'assets', 'fontes', 'PressStart2P-Regular.ttf'), 20) # Para ficar com a fonte bonitinha

        self.player1 = player1
        self.player2 = player2
        self.atacante = None
        self.defensor = None
        self.player_choice = 'P1'
        self.player_ident = 'P1'

        self.get_input = get_input

        self.state = 'Escolha'

        self.options_escolha = ['Guerreiro','Mago','Arqueiro']
        self.options_geral = ['Ataque Básico','Ataque Especial','Desviar']
        self.nome_ataque =[]
        self.options_ataque = []

        self.index = {'row':0}
        self.escolha_index = {'row':0}
        self.geral_index = {'row':0}
        self.ataque_index = {'row':0}


        SONS['clique'].set_volume(0.35)

    def get_skills(self,player):
        for nome, detalhes in Ataques.items():
            if detalhes['Classe'] == player.classe:
                self.nome_ataque.append(nome)
                texto_formatado = f"{nome} | Mana: {detalhes['Mp']} | Dano: {detalhes['Damage']}"
                self.options_ataque.append(texto_formatado)

    def input(self):
        
        keys = pygame.key.get_just_pressed()
        if self.state == 'Escolha':
            
            self.escolha_index['row'] = (self.escolha_index['row'] + int(keys[pygame.K_s]) - int(keys[pygame.K_w])) % len(self.options_escolha)
            if keys[pygame.K_SPACE]:
                SONS['clique'].play()
                self.classe = self.options_escolha[self.escolha_index['row']]
                
                self.get_input(self.state,self.classe,self.player_choice)

                if self.player_choice == 'P2':
                    self.player_ident = 'P1'
                    self.state = 'Principal'

                if self.player_choice == 'P1':
                    self.player_choice = 'P2'
                    self.player_ident = 'P2'
                    self.state = 'Escolha'
                
                
        elif self.state == 'Principal':
            self.geral_index['row'] = (self.geral_index['row'] + int(keys[pygame.K_s]) - int(keys[pygame.K_w])) % len(self.options_geral)
            if keys[pygame.K_SPACE]:
                SONS['clique'].play()
                self.nome_ataque =[]
                self.options_ataque = []
                self.get_input(self.state)
                self.state = self.options_geral[self.geral_index['row']]
                print(f"Opções {self.options_geral[self.geral_index['row']]}")

        elif self.state == 'Ataque Especial':
            
            self.ataque_index['row'] = (self.ataque_index['row'] + int(keys[pygame.K_s]) - int(keys[pygame.K_w])) % len(self.options_ataque)
            if keys[pygame.K_SPACE]:
                SONS['clique'].play()
                
                self.get_input(self.state,self.nome_ataque[self.ataque_index['row']])
                print(f"Ataque {self.options_ataque[self.ataque_index['row']]}")
                if self.state != 'Principal':
                    self.state = 'Aguardando'
                    if self.player_ident == 'P1':
                        self.player_ident = 'P2'
                    elif self.player_ident == 'P2':
                        self.player_ident = 'P1'
                
                    
            if keys[pygame.K_ESCAPE]:
                SONS['clique'].play()
                self.state = 'Principal'
                


        elif self.state == 'Desviar':
            self.get_input(self.state)
            self.state = 'Aguardando'
            if self.player_ident == 'P1':
                self.player_ident = 'P2'
            elif self.player_ident == 'P2':
                self.player_ident = 'P1'
            

        elif self.state == 'Ataque Básico':
            self.get_input(self.state,'atk_basico')
            self.state = 'Aguardando'
            if self.player_ident == 'P1':
                self.player_ident = 'P2'
            elif self.player_ident == 'P2':
                self.player_ident = 'P1'
            
    def menu(self,index,options):
        #background do menu
        rect = pygame.FRect(0,0,WINDOW_WIDTH-500,WINDOW_HEIGHT/2-100)
        rect.bottomright = (WINDOW_WIDTH-10, WINDOW_HEIGHT-10)
        pygame.draw.rect(self.display_surface,COLORS['white'],rect,0,7)
        pygame.draw.rect(self.display_surface,COLORS['gray'],rect,6,6)

        #menu
        for i, options_text in enumerate (options):
            x = rect.centerx
            altura = rect.height/len(options)
            y = rect.top + (altura/2) + (altura*i)

            color = COLORS['gray'] if i == index['row'] else COLORS['black']
            
            text_surf = self.font.render(options_text,True,color)
            text_rect = text_surf.get_rect(center = (x,y))
            self.display_surface.blit(text_surf,text_rect)

    def identificacao(self,player):
        rect = pygame.FRect(0,0,190,60)
        rect.bottomleft = ((WINDOW_WIDTH-300)/2, (WINDOW_HEIGHT/2)+100)
        pygame.draw.rect(self.display_surface,COLORS['white'],rect,0,7)
        pygame.draw.rect(self.display_surface,COLORS['gray'],rect,6,6)

        match player:
            case 'P1': texto = 'Player 1:'
            case 'P2': texto = 'Player 2:'
        
        text_surf = self.font.render(texto,True,'black')
        text_rect = text_surf.get_rect(center = rect.center)
        self.display_surface.blit(text_surf,text_rect)

    def status(self):
        rect = pygame.FRect(0,0,500,160)
        pygame.draw.rect(self.display_surface,COLORS['white'],rect,0,7)
        pygame.draw.rect(self.display_surface,COLORS['gray'],rect,6,6)

        barra_vida1 = pygame.FRect(rect.left+10,rect.top+30,480,13)
        barra_mana1 = pygame.FRect(rect.left+10,barra_vida1.bottom+10,480,13)
        barra_vida2 = pygame.FRect(rect.left+10,barra_vida1.bottom+60,480,13)
        barra_mana2 = pygame.FRect(rect.left+10,barra_vida2.bottom+10,480,13)

        text1 = self.font.render('Player 1:',True,'black')
        text1_rect = text1.get_rect(bottomleft = barra_vida1.topleft)
        self.display_surface.blit(text1,text1_rect)

        text2 = self.font.render('Player 2:',True,'black')
        text2_rect = text2.get_rect(bottomleft = barra_vida2.topleft)
        self.display_surface.blit(text2,text2_rect)

        pygame.draw.rect(self.display_surface,COLORS['gray'],barra_vida1)
        pygame.draw.rect(self.display_surface,COLORS['gray'],barra_mana1)

        pygame.draw.rect(self.display_surface,COLORS['gray'],barra_vida2)
        pygame.draw.rect(self.display_surface,COLORS['gray'],barra_mana2)

        self.barra(barra_vida1,self.player1.Hp,self.player1.MaxHp)
        self.barra(barra_mana1,self.player1.Mp,self.player1.MaxMp)
        self.barra(barra_vida2,self.player2.Hp,self.player2.MaxHp)
        self.barra(barra_mana2,self.player2.Mp,self.player2.MaxMp)

    def barra(self, rect, valor, valor_max):
        prop = rect.width / valor_max
        self.font_pequena = pygame.font.Font(os.path.join(os.path.dirname(__file__), '..', 'assets', 'fontes', 'PressStart2P-Regular.ttf'), 13)
        barra = pygame.FRect(rect.topleft, ( valor*prop,rect.height))
        if valor_max == self.player1.MaxHp or valor_max == self.player2.MaxHp:
            color = COLORS['red']
        else:
            color = COLORS['blue']
        pygame.draw.rect(self.display_surface,color,barra)

        texto = self.font_pequena.render(f'{valor} / {valor_max}',True,'black')
        texto_rect = texto.get_rect(center = rect.center)
        self.display_surface.blit(texto,texto_rect)

    def update(self):
        self.input()

    def draw(self):
        match self.state:
            case 'Escolha': 
                self.identificacao(self.player_ident)
                self.menu(self.escolha_index,self.options_escolha)

            case 'Principal':
                self.identificacao(self.player_ident)
                self.menu(self.geral_index,self.options_geral)

            case 'Ataque Especial':
                self.identificacao(self.player_ident)
                self.menu(self.ataque_index,self.options_ataque)

            case 'Ataque Básico': 
                pass

            case 'Desviar': 
                pass

        if self.state != 'Escolha':
            self.status()
                 
