from settings import *
import os
from classes import *
from efeitos import SONS
from Timer import Timer

class UI:
    def __init__ (self,player1,player2,get_input):

        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(os.path.join(os.path.dirname(__file__), '..', 'assets', 'fontes', 'PressStart2P-Regular.ttf'), 24) # Para ficar com a fonte bonitinha
        self.left = WINDOW_WIDTH/2
        self.top = WINDOW_HEIGHT/2 + 50

        self.player1 = player1
        self.player2 = player2
        self.atacante = None
        self.defensor = None
        self.player_choice = 'P1'

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
                    self.state = 'Principal'

                if self.player_choice == 'P1':
                    self.player_choice = 'P2'
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
                
                    
            if keys[pygame.K_ESCAPE]:
                SONS['clique'].play()
                self.state = 'Principal'


        elif self.state == 'Desviar':
            self.get_input(self.state)
            self.state = 'Aguardando'
            

        elif self.state == 'Ataque Básico':
            self.get_input(self.state,'atk_basico')
            self.state = 'Aguardando'
            


    def menu(self,index,options):
        #background do menu
        rect = pygame.FRect(0,0,WINDOW_WIDTH-600,WINDOW_HEIGHT/2-100)
        rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT/2 +200)
        pygame.draw.rect(self.display_surface,COLORS['white'],rect,0,4)
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

    def update (self):

        self.input()


    def draw(self):
        match self.state:
            case 'Escolha': 
                self.menu(self.escolha_index,self.options_escolha)
            case 'Principal':
                self.menu(self.geral_index,self.options_geral)
            case 'Ataque Especial':
                
                self.menu(self.ataque_index,self.options_ataque)
            case 'Ataque Básico': 
                pass 
            case 'Desviar': 
                pass 
