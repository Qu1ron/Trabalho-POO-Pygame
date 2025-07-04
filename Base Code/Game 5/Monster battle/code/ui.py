from settings import *

class UI:
    def __init__(self,monster,monster_list,get_input):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 30)
        self.left = WINDOW_WIDTH /2 - 100
        self.top = WINDOW_HEIGHT/2 + 50
        self.monster = monster
        self.monster_list = monster_list
        self.available_monsters = [monster for monster in self.monster_list if monster != self.monster and monster.health > 0]

        #control 

        self.get_input = get_input

        self.general_options = ['attack', 'heal', 'switch', 'escape']
        self.general_index = {'col': 0, 'row': 0}
        self.attack_index = {'col': 0, 'row': 0}
        self.switch_index = 0
        self.state = 'general'
        self.rows,self.cols = 2,2
        self.visible_monsters = 4

    def input(self):
        keys = pygame.key.get_just_pressed()
        if self.state == 'general':
            self.general_index['col'] = (self.general_index['col'] + int(keys[pygame.K_d]) - int(keys[pygame.K_a])) % self.cols
            self.general_index['row'] = (self.general_index['row'] + int(keys[pygame.K_s]) - int(keys[pygame.K_w])) % self.rows

            if keys[pygame.K_SPACE]:
                self.state = self.general_options[self.general_index['col'] + self.general_index['row']*2]

        elif self.state == 'attack':
            self.attack_index['col'] = (self.attack_index['col'] + int(keys[pygame.K_d]) - int(keys[pygame.K_a])) % self.cols
            self.attack_index['row'] = (self.attack_index['row'] + int(keys[pygame.K_s]) - int(keys[pygame.K_w])) % self.rows

            if keys[pygame.K_SPACE]:
                attack = self.monster.abilities[self.attack_index['col'] + self.attack_index['row']*2]
                self.get_input(self.state, attack)
                self.state = 'general'

        elif self.state == 'switch':
            if self.available_monsters:
                self.switch_index = (self.switch_index + int(keys[pygame.K_s]) - int(keys[pygame.K_w])) % len(self.available_monsters)
                
                if keys[pygame.K_SPACE]:
                    self.get_input(self.state, self.available_monsters[self.switch_index])
                    self.state = 'general'

        elif self.state == 'heal':
            self.get_input(self.state, 'heal')
            self.state = 'general'

        elif self.state == 'escape':
            self.get_input(self.state)
            
        if keys[pygame.K_ESCAPE]:
            self.state = 'general'
            self.general_index = {'col': 0, 'row': 0}
            self.attack_index = {'col': 0, 'row': 0}
            self.switch_index = 0

    def quad_select(self,index,options):
        #bg
        rect = pygame.FRect(self.left+40,self.top+60,400,200)
        pygame.draw.rect(self.display_surface, COLORS['white'], rect, 0, 4)
        pygame.draw.rect(self.display_surface, COLORS['gray'], rect, 4, 4)

        #menus
        for col in range(self.cols):
            for row in range(self.rows):
                x = rect.left + (rect.width/(self.cols*2)) + (rect.width*col/self.cols)
                y = rect.top + (rect.height/(self.rows*2)) + (rect.height*row/self.rows)

                i = col + 2*row

                color = COLORS['gray'] if col == index['col'] and row == index['row'] else COLORS['black']

                text_surf = self.font.render(options[i], True, color)
                text_rect = text_surf.get_frect(center = (x,y))
                self.display_surface.blit(text_surf,text_rect)

    def switch(self):
        #bg
        rect = pygame.FRect(self.left+40,self.top-100,400,400)
        pygame.draw.rect(self.display_surface, COLORS['white'], rect, 0, 4)
        pygame.draw.rect(self.display_surface, COLORS['gray'], rect, 4, 4)

        #menu
        v_offset = 0 if self.switch_index < self.visible_monsters else -(self.switch_index-self.visible_monsters+1)*(rect.height/self.visible_monsters)
        for i in range(len(self.available_monsters)):
            x = rect.centerx
            y = rect.top + rect.height / (self.visible_monsters *2) + (rect.height/self.visible_monsters)*i + v_offset

            color = COLORS['gray'] if i == self.switch_index else COLORS['black']

            name = self.available_monsters[i].name
            icon = self.available_monsters[i].simple_surf
            icon_rect = icon.get_frect(center = (rect.left+50,y))
            text_surf = self.font.render(name, True, color)
            text_rect = text_surf.get_frect(center = (x,y))



            if rect.collidepoint(text_rect.center):
                self.display_surface.blit(text_surf,text_rect)
                self.display_surface.blit(icon,icon_rect)

    def update(self):
        self.input()
        self.available_monsters = [monster for monster in self.monster_list if monster != self.monster and monster.health > 0]

    def stats(self):
        #bg
        rect = pygame.FRect(self.left,self.top,250,80)
        pygame.draw.rect(self.display_surface, COLORS['white'], rect, 0, 4)
        pygame.draw.rect(self.display_surface, COLORS['gray'], rect, 4, 4)

        #data
        name_surf = self.font.render(self.monster.name, True, COLORS['black'])
        name_rect = name_surf.get_frect(topleft = rect.topleft + pygame.Vector2(rect.width*0.05,12))
        self.display_surface.blit(name_surf,name_rect)

        #health bar
        health_rect = pygame.FRect(name_rect.left,name_rect.bottom + 10, rect.width*0.9, 20)
        pygame.draw.rect(self.display_surface, COLORS['gray'], health_rect)
        self.draw_bar(health_rect,self.monster.health,self.monster.max_health)

    def draw_bar(self, rect , value ,max_value):
        ratio = rect.width / max_value
        progress_rect = pygame.FRect(rect.topleft,(value*ratio,rect.height))
        pygame.draw.rect(self.display_surface, COLORS['red'], progress_rect)




    def draw(self):
        match self.state:

            case 'general':  self.quad_select(self.general_index, self.general_options)
               
            case 'attack': self.quad_select(self.attack_index,self.monster.abilities)

            case 'heal':
                pass
            case 'switch': self.switch()

        if self.state != 'switch':
            self.stats()
        
class OpponentUI:
    def __init__(self,monster):
        self.display_surface = pygame.display.get_surface()
        self.monster = monster
        self.font = pygame.font.Font(None, 30)

    def draw(self):
        #bg
        rect = pygame.FRect((0,0),(250,80)).move_to(midleft = (500,self.monster.rect.centery))
        pygame.draw.rect(self.display_surface, COLORS['white'], rect, 0, 4)
        pygame.draw.rect(self.display_surface, COLORS['gray'], rect, 4, 4)

        name_surf = self.font.render(self.monster.name, True, COLORS['black'])
        name_rect = name_surf.get_frect(topleft = rect.topleft + pygame.Vector2(rect.width *0.05, 12))
        self.display_surface.blit(name_surf,name_rect)

        #health bar
        health_rect = pygame.FRect(name_rect.left,name_rect.bottom + 10, rect.width*0.9, 20)
        pygame.draw.rect(self.display_surface, COLORS['gray'], health_rect)
        self.draw_bar(health_rect,self.monster.health,self.monster.max_health)

    def draw_bar(self, rect , value ,max_value):
        ratio = rect.width / max_value
        progress_rect = pygame.FRect(rect.topleft,(value*ratio,rect.height))
        pygame.draw.rect(self.display_surface, COLORS['red'], progress_rect)