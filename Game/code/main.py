from settings import *
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

        #teste da ui
        player_surf = pygame.Surface((100, 100))
        self.player1 = Guerreiro('teste',[player_surf, player_surf],self.all_sprites)
        self.display_surface.fill('black')
        
        #ui
        self.uip1 = UI(self.player1)

        #timers



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
            self.all_sprites.draw(self.display_surface)

            self.uip1.draw()
            
            pygame.display.update()


        pygame.quit()



if __name__ == '__main__':
    jogo = Jogo()
    jogo.run()
