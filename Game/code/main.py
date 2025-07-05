from settings import *
from efeitos import *
from ui import UI
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
        
        self.player1 = Guerreiro('Quiron', self.all_sprites, False)
        self.player2 = Mago('Dummy', self.all_sprites, True)

        #teste da ui
        
        
        #ui
        self.uip1 = UI(self.player1, self.get_input)

        #timers

     def get_input(self, state, data):
        if state == 'Escolha':
            pass
        
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

            self.all_sprites.draw(self.display_surface)

            self.uip1.draw()

            
            
            
            pygame.display.update()


        pygame.quit()



if __name__ == '__main__':
    jogo = Jogo()
    jogo.run()
