from settings import *
from support import *
from Timer import Timer
from monster import *
from ui import *
from attack import *


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Monster Battle')
        self.clock = pygame.time.Clock()
        self.running = True
        self.player_active = True
        self.import_assets()
        self.audio['music'].set_volume(0.25)
        self.audio['music'].play(-1)
        # groups 
        self.all_sprites = pygame.sprite.Group()

        # data
        player_monsters_list = ['Sparchu', 'Charmadillo', 'Ivieron','Gulfin','Pouch','Larvea']
        self.opponent_name = choice(list(MONSTER_DATA.keys()))
        self.opponent_monster = Opponent(self.opponent_name, self.front_surfs[self.opponent_name],simple_surf=self.simple_surfs[self.opponent_name], groups=self.all_sprites)
        self.player_monsters = [Monster(name, self.back_surfs[name],self.simple_surfs[name]) for name in player_monsters_list]
        self.monster = self.player_monsters[0]
        self.all_sprites.add(self.monster)

        #ui 
        self.ui = UI(self.monster,self.player_monsters,self.get_input)
        self.opponent_ui = OpponentUI(self.opponent_monster)

        #timers
        self.timers = {'player_end': Timer(1000, func = self.opponent_turn),'opponent_end': Timer(1000, func = self.player_turn)}

    def draw_monster_floor(self):
        for sprite in self.all_sprites:
            if isinstance(sprite,Creature):
                floor_rect = self.bg_surfs['floor'].get_frect(center = sprite.rect.midbottom + pygame.Vector2(0,-10))
                self.display_surface.blit(self.bg_surfs['floor'], floor_rect)
            
    def get_input(self, state, data):
        if state == 'attack':
            self.apply_attack(self.opponent_monster,data)
        
        elif state == 'heal':
            self.monster.health += 50
            AttackAnimationSprite(self.monster,self.attack_frames['green'],self.all_sprites)
            self.audio['green'].set_volume(0.25)
            self.audio['green'].play()

        elif state == 'switch':
            self.monster.kill()
            self.monster = data
            self.all_sprites.add(self.monster)
            self.ui.monster = self.monster

        elif state == 'escape':
            self.running = False
        print(data)
        self.player_active = False
        self.timers['player_end'].activate()

    def apply_attack(self,opponent_monster,attack):
        attack_data = ABILITIES_DATA[attack]
        #multiplier
        attack_mult = ELEMENT_DATA[attack_data['element']][opponent_monster.element]

        opponent_monster.health -= attack_data['damage'] * attack_mult
        AttackAnimationSprite(opponent_monster,self.attack_frames[attack_data['animation']],self.all_sprites)
        self.audio[attack_data['animation']].set_volume(0.25)
        self.audio[attack_data['animation']].play()

    def player_turn(self):
        self.player_active = True
        if self.monster.health <= 0:
            available_monsters = [monster for monster in self.player_monsters if monster.health > 0]
            if available_monsters:
                self.monster.kill()
                self.monster = available_monsters[0]
                self.all_sprites.add(self.monster)
                self.ui.monster = self.monster
            else: 
                self.running = False
            
    def opponent_turn(self):
        if self.opponent_monster.health <=0:
            self.player_active = True
            self.opponent_monster.kill()
            monster_name = choice(list(MONSTER_DATA.keys()))
            self.opponent_monster = Opponent(monster_name,self.front_surfs[monster_name],self.all_sprites,self.simple_surfs[monster_name])
            self.opponent_ui.monster = self.opponent_monster
        else:
            attack = choice(self.opponent_monster.abilities)
            self.apply_attack(self.monster,attack)
            self.timers['opponent_end'].activate()

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def import_assets(self):
        self.back_surfs = folder_importer('images', 'back')
        self.front_surfs = folder_importer('images','front')
        self.bg_surfs = folder_importer('images', 'other')
        self.simple_surfs = folder_importer ('images', 'simple')
        self.attack_frames = tile_importer(4,'images','attacks')
        self.audio = audio_importer('audio')

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
           
            # update
            self.update_timers()
            self.all_sprites.update(dt)
            if self.player_active == True:
                self.ui.update()

            # draw  
            self.display_surface.blit(self.bg_surfs['bg'], (0,0))
            self.draw_monster_floor()
            
            self.all_sprites.draw(self.display_surface)
            self.ui.draw()
            self.opponent_ui.draw()
            pygame.display.update()
        
        pygame.quit()
    
if __name__ == '__main__':
    game = Game()
    game.run()