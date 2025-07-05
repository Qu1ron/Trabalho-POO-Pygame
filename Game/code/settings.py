import pygame
from os.path import join 
from os import walk
from random import choice, randint

WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720 

COLORS = {
    'black': '#000000',
    'red': '#ee1a0f',
    'gray': 'gray',
    'white': '#ffffff',
}


Ataques = {
    'Fireball': {'Damage': 45, 'Mp': 20, 'Classe': 'Mago', 'Efeito': 'burn'},
    'Ice Spike': {'Damage': 55, 'Mp': 30, 'Classe': 'Mago', 'Efeito': 'freeze'},
    'Thunderbolt': {'Damage': 65, 'Mp': 40, 'Classe': 'Mago', 'Efeito': 'shocked'},
    'Hydro Pump': {'Damage': 70, 'Mp': 45, 'Classe': 'Mago', 'Efeito': 'soaked'},
    
    'Slash': {'Damage': 40, 'Mp': 15, 'Classe': 'Guerreiro', 'Efeito': 'bleed'},
    'Last Bastion': {'Damage': 50, 'Mp': 25, 'Classe': 'Guerreiro', 'Efeito': 'Não sei'},
    'Blade of Fate': {'Damage': 60, 'Mp': 35, 'Classe': 'Guerreiro', 'Efeito': 'Não sei'},
    'Golpe Demolidor': {'Damage': 75, 'Mp': 50, 'Classe': 'Guerreiro', 'Efeito': 'Vulnerable'}, 

    'Double Shot' : { 'Damage': 38 ,'Mp': 15 , 'Classe' : 'Arqueiro' , 'Efeito' : ' ? ' },
    'Smoke Arrow' : { 'Damage': 48 ,'Mp': 22 , 'Classe' : 'Arqueiro' , 'Efeito' : ' Blinded ' },
    'Poison Arrow' : { 'Damage': 58 ,'Mp': 30 , 'Classe' : 'Arqueiro' , 'Efeito' : ' Poisoned ' },
    'Tiro Penetrante' : { 'Damage': 70, 'Mp': 40, 'Classe': 'Arqueiro', 'Efeito': 'Armor Break'}, 
}