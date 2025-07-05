from settings import *
from efeitos import SPRITES

# Nesse arquivo temos as classes

class Personagem:
        #Funcao para inicializar as variaveis
    def get_data(self, name, MaxHp, Hp, MaxMp, Mp, Defense, Speed):
        #Salvar os valores em variaveis:
        self.name = name
        self.MaxHp = MaxHp
        self.Hp = Hp
        self.MaxMp = MaxMp
        self.Mp = Mp 
        self.Defense = Defense
        self.Speed = Speed


        #para ui
        #self.image = self.perso_surfs[0]
        #self.rect = self.image.get_frect(bottomleft = (100,WINDOW_WIDTH))
    
        #Funcao pro ataque basico
    def ataque(self):
        self.dmg = 10
        return self.dmg
        
        #Funcao pra checar se o Personagem esta vivo
    def survived(self):
        if self.Hp <= 0:
            return False
        else:
            return True
    
        #funcao pra calcular o dano
    def damage_cal(self,dano):
        self.Hp = self.Hp - max(1, dano - (self.Defense / 2)) #max garante que o dano não seja menor que 1
        
    
        #funcao pro dodge, tem que testar pra ver se a formula funciona bem   
    def dodge(self):
        self.base_chance = max(5, min(5 + (self.Speed * 4), 85)) #Nova formula pro dodge, dando mais importancia a speed
        self.sorte = randint(0,3) #gera um numero aleatorio [0, 3] 
        self.chance_desvio = self.base_chance + self.sorte #Entao se voce tem 100 de speed, 50 de base chance + de 0 a 10 dependendo da sorte
        self.rolagem = randint(0,100) #pensa num dado de 100 lados, se o numero que sair for menor que a chance, vc toma :P
        print(f"\n{self.chance_desvio} > {self.rolagem}?")
        if self.chance_desvio > self.rolagem:
            return True
        else: 
            return False
               
class Mago(pygame.sprite.Sprite, Personagem):
    def __init__(self, name, groups, p2, MaxHp = 180, Hp = 180, MaxMp = 200, Mp = 200, Defense = 15, Speed = 10, skills = Ataques):
        super().__init__(groups)
        self.classe = 'Mago'
        
        self.get_data(name,MaxHp,Hp,MaxMp,Mp,Defense,Speed)
        
        if not p2:
            self.image = SPRITES['mago']['costas']
            self.rect = self.image.get_frect(bottomleft = (100,WINDOW_HEIGHT))
        else:
            self.image = SPRITES['mago']['frente']
            self.rect = self.image.get_frect(midbottom = (WINDOW_WIDTH-300, 350))

         

        #pra cada nome e detalhe no dicionario Ataques, se detalhe = 'Mago' agente copia todos os detalhes da skill com esse nome
        self.skills = {}
        for nome, detalhe in skills.items(): 
            if detalhe['Classe'] == 'Mago':
                self.skills[nome] = detalhe
    
    def ataque(self):
        if self.Mp >=8:
            self.dmg = 25
            self.Mp -= 8
        else:
            print("Não tem mana suficiente... Cajadada vai servir!")
            self.dmg = super().ataque() # Chama o ataque básico padrão 
        return int(self.dmg)
    
class Guerreiro(pygame.sprite.Sprite, Personagem):
    def __init__(self, name, groups, p2, MaxHp = 250, Hp = 250, MaxMp = 100, Mp = 100, Defense = 40, Speed = 7, skills = Ataques):
        super().__init__(groups)
        self.classe = 'Guerreiro'

        self.get_data(name,MaxHp,Hp,MaxMp,Mp,Defense,Speed)
        
        if not p2:
            self.image = SPRITES['guerreiro']['costas']
            self.rect = self.image.get_frect(bottomleft = (300,WINDOW_HEIGHT-100))
        else:
            self.image = SPRITES['guerreiro']['frente']
            self.rect = self.image.get_frect(midbottom = (WINDOW_WIDTH-100, 300))



        self.skills = {}
        for nome, detalhe in skills.items():
            if detalhe['Classe'] == 'Guerreiro':
                self.skills[nome] = detalhe
        
    def ataque(self):
        if self.Mp >= 10:
            self.dmg = 20
            self.Mp -= 10
        else:
            print("Lhe falta Vigor!")
            self.dmg = super().ataque() 
        return int(self.dmg)
        
class Arqueiro(pygame.sprite.Sprite, Personagem) :
    def __init__ (self ,name, groups, p2, MaxHp = 200 ,Hp = 200 ,MaxMp = 150 ,Mp = 150 ,Defense = 25 ,Speed = 16 ,skills = Ataques) :
        super().__init__(groups)
        self.classe = 'Arqueiro'

        self.get_data(name,MaxHp,Hp,MaxMp,Mp,Defense,Speed)
        
        if not p2:
            self.image = SPRITES['arqueiro']['costas']
            self.rect = self.image.get_frect(bottomleft = (100,WINDOW_HEIGHT))
        else:
            self.image = SPRITES['arqueiro']['frente']
            self.rect = self.image.get_frect(midbottom = (WINDOW_WIDTH-250, 300))
        
        self.skills = {}
        for nome ,detalhe in skills.items():
            if detalhe ['Classe'] == 'Arqueiro' :
                self.skills[nome] = detalhe
                    
    def ataque (self ):
        if self.Mp >= 12:
            self.dmg = 26
            self.Mp -= 12
        else:
            print("Perdeu o foco! Um simples arranhão ")
            self.dmg = super().ataque()
        return int(self.dmg)
