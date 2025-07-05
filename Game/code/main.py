from settings import *
from efeitos import *
from ui import *
from classes import *

class Jogo:
     def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('RPG Realm')
        self.clock = pygame.time.Clock()
        self.running = True


        #groups
        self.all_sprites = pygame.sprite.Group()

        #data
        self.player1 = Mago('Dummy1', self.all_sprites, False)
        self.player1.kill()
        self.player2 = Guerreiro('Dummy1', self.all_sprites, True)
        
        #teste da ui
        
        
        #ui
        self.uip1 = UI(self.player1, self.get_input)

        #timers


     def get_input(self, state, data1, data2 = None):
        if state == 'Escolha':
            if data2 == 'P1':
                if data1 == 'Mago':
                    self.player1 = Mago('Dummy1', self.all_sprites, False)
                if data1 == 'Guerreiro':
                    self.player1 = Guerreiro('Dummy1', self.all_sprites, False)
                if data1 == 'Arqueiro':
                    self.player1 = Arqueiro('Dummy1', self.all_sprites, False)
            self.uip1.player = self.player1
            
                
            if data2 == 'P2':
                if data1 == 'Mago':
                    self.player2 = Mago('Dummy2', self.all_sprites, True)
                if data1 == 'Guerreiro':
                    self.player2 = Guerreiro('Dummy2', self.all_sprites, True)
                if data1 == 'Arqueiro':
                    self.player2 = Arqueiro('Dummy2', self.all_sprites, True)
        
        elif state == 'Principal':
            pass

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
