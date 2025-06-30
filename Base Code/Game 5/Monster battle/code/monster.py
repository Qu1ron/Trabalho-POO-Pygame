from settings import *
from random import sample

class Creature:
    def get_data(self, name, simple_surf):
        self.name = name
        self.simple_surf = simple_surf
        self.element = MONSTER_DATA[name]['element']
        self._health = self.max_health = MONSTER_DATA[name]['health']
        self.abilities = sample(list(ABILITIES_DATA.keys()), 4)

    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self,value):
        self._health = min(self.max_health,max(0,value))

class Monster(pygame.sprite.Sprite, Creature):
    def __init__(self, name, surf,simple_surf):
        super().__init__()
        self.image = surf
        self.rect = self.image.get_frect(bottomleft = (100,WINDOW_HEIGHT))

        #data
        self.get_data(name,simple_surf)

class Opponent(pygame.sprite.Sprite, Creature):
    def __init__(self, name, surf, groups,simple_surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = (WINDOW_WIDTH-250, 300))

        #data
        self.get_data(name,simple_surf)