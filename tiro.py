import pygame
from configs.config import ConfigGerais

class Tiro():
    
    def __init__(self, x, y, angulo, velocidade=10, player=None):
        self.player = player
        self.x = x
        self.y = y
        self.angulo = angulo
        self.velocidade = velocidade
        
    def draw(self, screen):
        pygame.draw.rect(screen, ConfigGerais.BLACK, (self.x, self.y, 10, 10))
       
    def define_localizacao0(self):
        self.x += 30
        self.y += 10
    def define_localizacao45(self):
        self.x += 30
    def define_localizacao90(self):
        self.x += 10
        self.y -= 10
    def define_localizacao135(self):
        pass
    def define_localizacao180(self):
        self.x -= 10
        self.y += 10      
    def define_localizacao225(self):
        self.y += 30 
    def define_localizacao270(self):
        self.x += 10
        self.y += 30
    def define_localizacao315(self):
        self.x += 30
        self.y += 30
        
        
    shot = {
        0: define_localizacao0,
        45: define_localizacao45,
        90: define_localizacao90,
        135: define_localizacao135,
        180: define_localizacao180,
        225: define_localizacao225,
        270: define_localizacao270,
        315: define_localizacao315,
    }
