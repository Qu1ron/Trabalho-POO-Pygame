from settings import *
from efeitos import *
from ui import *
from classes import *
from Timer import Timer

class Jogo:
     def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('RPG Realm')
        self.clock = pygame.time.Clock()
        self.running = True
        self.Turn = 'P1'


        #groups
        self.all_sprites = pygame.sprite.Group()
        self.group_p1 = pygame.sprite.Group()
        self.group_p2 = pygame.sprite.Group()

        #data
        self.player1 = Mago('Dummy1', False)
        self.player2 = Guerreiro('Dummy1', True)
        
        
        #teste da ui
        
        
        #ui
        self.uip1 = UI(self.player1, self.player2, self.get_input)
        

        #timers
        self.timers = {'atacante_end': Timer(1000, func = self.change_turn),'defesor_end': Timer(1000, func = self.change_turn)}


     def get_input(self, state, data1= None, data2 = None):
        if state == 'Escolha':
            if data2 == 'P1':
                if data1 == 'Mago':
                    self.player1 = Mago('Dummy1', False)
                if data1 == 'Guerreiro':
                    self.player1 = Guerreiro('Dummy1', False)
                if data1 == 'Arqueiro':
                    self.player1 = Arqueiro('Dummy1', False)
                self.uip1.player1 = self.player1
            
                
            if data2 == 'P2':
                if data1 == 'Mago':
                    self.player2 = Mago('Dummy2', True)
                if data1 == 'Guerreiro':
                    self.player2 = Guerreiro('Dummy2', True)
                if data1 == 'Arqueiro':
                    self.player2 = Arqueiro('Dummy2', True)
                self.uip1.player2 = self.player2

                if(self.uip1.player1.Speed >= self.uip1.player2.Speed):
                    self.uip1.atacante = self.player1
                    self.uip1.defensor = self.player2
                else:
                    self.player2.p2 = False
                    self.player2.check_p2()
                    self.player1.p2 = True
                    self.player1.check_p2()

                    self.uip1.atacante = self.player2
                    self.uip1.defensor = self.player1

                self.all_sprites.add(self.uip1.atacante)
                self.all_sprites.add(self.uip1.defensor)
                

        elif state == 'Principal':
            self.uip1.get_skills(self.uip1.atacante)
            

        elif state == 'Ataque Especial':
            pass
        
        elif self.state == 'Desviar':
            pass

        elif self.state == 'Ataque Básico':
            pass
        

     def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update

            self.all_sprites.update(dt)
            self.uip1.update()
            
            # draw
            self.display_surface.blit(MAPAS['floresta'], (0,0))
            self.uip1.draw()
            self.all_sprites.draw(self.display_surface)

            

            
            
            
            pygame.display.update()


        pygame.quit()



if __name__ == '__main__':
    jogo = Jogo()
    jogo.run()
