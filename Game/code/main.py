from settings import *
from efeitos import *
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
        
        self.player1 = Mago('Quiron',SPRITES['mago'], self.all_sprites, False)
        self.player2 = Guerreiro('Dummy', SPRITES['guerreiro'], self.all_sprites, True)

        #ui

        #timers



     def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update

            self.all_sprites.update(dt)
            

            # draw  

            self.all_sprites.draw(self.display_surface)
            
            
            pygame.display.update()


        pygame.quit()



if __name__ == '__main__':
    jogo = Jogo()
    jogo.run()
