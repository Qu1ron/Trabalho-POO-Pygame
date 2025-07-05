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
        self.Turn_tracker = 1
        self.Turn = 'atacante'


        #groups
        self.all_sprites = pygame.sprite.Group()
        

        #data

        self.player1 = Mago('Dummy1', False)
        self.player2 = Guerreiro('Dummy1', True)

        self.dmg_p1 = 0
        self.dmg_p2 = 0

        self.desvio_p1 = False
        self.desvio_p2 = False
        
        
        
        
        #ui
        self.uip1 = UI(self.player1, self.player2, self.get_input)
        

        #timers
        self.timer_tend = Timer(1000, func = self.change_turn)
        self.timer_tres = Timer(1000, func = self.turn_result)
        self.timer_tres_extra = Timer(1000)
        


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
            if self.uip1.atacante.Mp >= Ataques[data1]['Mp']:
                self.apply_atk(data1)
                self.timer_tend.activate()
            else:
                self.uip1.state = 'Principal'
        
        elif state == 'Desviar':
            if self.Turn == 'atacante':
                self.desvio_p1 = self.uip1.atacante.dodge()
            else:
                self.desvio_p2 = self.uip1.atacante.dodge()
            self.timer_tend.activate()
          
        elif state == 'Ataque Básico':
            self.apply_atk(data1)
            self.timer_tend.activate()
        
     def apply_atk(self,skill):
        if skill != 'atk_basico':
            dmg = Ataques[skill]['Damage']
            mp = Ataques[skill]['Mp']
            print(f"Mp antes: {self.uip1.atacante.Mp}\n")
            self.uip1.atacante.Mp -=mp
        else:
            dmg = self.uip1.atacante.ataque()
        if self.Turn == 'atacante':
            self.dmg_p1 = dmg
        else:
            self.dmg_p2 = dmg

        print(f"Mp depois: {self.uip1.atacante.Mp}\n")
         
     def change_turn(self):
        self.uip1.atacante.kill()
        self.uip1.defensor.kill()

        self.uip1.atacante, self.uip1.defensor = self.uip1.defensor, self.uip1.atacante

        self.uip1.atacante.p2 = False
        self.uip1.atacante.check_p2()
        self.uip1.defensor.p2 = True
        self.uip1.defensor.check_p2()

        self.all_sprites.add(self.uip1.atacante)
        self.all_sprites.add(self.uip1.defensor)

        
        if self.Turn == 'atacante': self.Turn = 'defensor'
        else: self.Turn = 'atacante'
        self.timer_tres.activate()
        sleep(1)
        self.uip1.state = 'Principal'
        
     def turn_result(self):
        if self.Turn_tracker != 2:
            self.Turn_tracker += 1

            self.uip1.state = 'Principal'
            return
        
        print(f"Hp player 1 antes: {self.uip1.atacante.Hp}")
        print(f"Hp player 2 antes: {self.uip1.defensor.Hp}\n")

        if self.desvio_p1 and not self.desvio_p2:
            #self.uip1.defensor.damage_cal(self.dmg_p1)
            #self.uip1.atacante.damage_cal(self.dmg_p2)
            pass

        elif not self.desvio_p1 and self.desvio_p2:
            #self.uip1.defensor.damage_cal(self.dmg_p1)
            #self.uip1.atacante.damage_cal(self.dmg_p2)
            pass

        elif not self.desvio_p1 and not self.desvio_p2:
            self.uip1.defensor.damage_cal(self.dmg_p1)
            self.uip1.atacante.damage_cal(self.dmg_p2)

        elif self.desvio_p1 and self.desvio_p2:
            pass

        if self.dmg_p1 != 0 and not self.desvio_p2:
            SONS['dano'].play()
            efeito_mudar_cor(self.uip1.defensor.image,COLORS['red'],pygame.time.get_ticks())
        
        sleep(1)

        if self.dmg_p2 != 0 and not self.desvio_p1:
            SONS['dano'].play()
            efeito_mudar_cor(self.uip1.atacante.image,COLORS['red'],pygame.time.get_ticks())
        
        print(f"Hp player 1 depois: {self.uip1.atacante.Hp}")
        print(f"Hp player 2 depois: {self.uip1.defensor.Hp}\n")
        
        if not self.uip1.atacante.survived():
            print("Player 2 Ganhou!")
            self.running = False

        if not self.uip1.defensor.survived():
            print("Player 1 Ganhou!")
            self.running = False

        print("\nRecuperando mana...\n")

        # Recuperação para o Atacante
        if isinstance(self.uip1.atacante, Mago) and self.uip1.atacante.Mp <= self.uip1.atacante.MaxMp - 20:
            self.uip1.atacante.Mp += 20
        elif isinstance(self.uip1.atacante, Arqueiro) and self.uip1.atacante.Mp <= self.uip1.atacante.MaxMp - 12:
            self.uip1.atacante.Mp += 12
        elif isinstance(self.uip1.atacante, Guerreiro) and self.uip1.atacante.Mp <= self.uip1.atacante.MaxMp - 5:
            self.uip1.atacante.Mp += 5
        
        # Recuperação para o Defensor
        if isinstance(self.uip1.defensor, Mago) and self.uip1.defensor.Mp <= self.uip1.defensor.MaxMp - 20:
            self.uip1.defensor.Mp += 20
        elif isinstance(self.uip1.defensor, Arqueiro) and self.uip1.defensor.Mp <= self.uip1.defensor.MaxMp - 12:
            self.uip1.defensor.Mp += 12
        elif isinstance(self.uip1.defensor, Guerreiro) and self.uip1.defensor.Mp <= self.uip1.defensor.MaxMp - 5:
            self.uip1.defensor.Mp += 5

        self.dmg_p1 = 0
        self.dmg_p2 = 0
        self.desvio_p1 = False
        self.desvio_p2 = False
        self.Turn_tracker = 1
        self.uip1.state = 'Principal'
        
     
     def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update
            self.timer_tend.update()
            self.timer_tres.update()
            self.all_sprites.update(dt)
            self.uip1.update()
            self.timer_tres_extra.update()
            
            # draw
            self.display_surface.blit(MAPAS['floresta'], (0,0))

            self.uip1.draw()

            self.all_sprites.draw(self.display_surface)

            

            
            
            
            pygame.display.update()


        pygame.quit()



if __name__ == '__main__':
    jogo = Jogo()
    jogo.run()
