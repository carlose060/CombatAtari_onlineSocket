import pygame
from configs.config import ConfigGerais, ConfigAmbiente
from colisoes.colisao_tanque import Colisao
from tiro import Tiro
import time


class Tank(pygame.sprite.Sprite):
    
    def __init__(self,x=70, y=300, player=0):
        super().__init__()
        local = ConfigAmbiente.localizacao['Player'+str(player)]
        self.x = local['x']
        self.y = local['y']
        self.velocidade = 4
        # PNG tamanho 30x30
        self.image = pygame.image.load(f'{ConfigGerais.DIR_PATH}{str(player)}.png')
        #self.image = pygame.transform.rotate(self.image,local['angulo'])
        self.image = pygame.transform.rotate(self.image,270)
        self.angulo_atual = 0
        self.tempo = time.time()
        self.tempo_tiro = time.time()
        self.player = player
        self.tiros = []
        self.vida = 3
        self.score = 0
        self.comandos = {
            '1': self.comando1,  # UP -- ANDAR
            '2': self.comando2,  # ESQUERDA
            '3': self.comando3,  # DIREITA
            '4': self.comando4   # ESPAÇO -- TIRO
        } 
     
    def draw(self,screen):    
        screen.blit(pygame.transform.rotate(self.image,self.angulo_atual),(self.x, self.y))
    
    def comando1(self):
        colisao = Colisao.iscoliding[self.angulo_atual]
        colisao(self)
    
    def comando2(self):
        if time.time() - self.tempo > 0.2:
            self.angulo_atual += 45
            self.tempo = time.time()
            if self.angulo_atual == 360:
                self.angulo_atual = 0
    
    def comando3(self):
        if time.time() - self.tempo > 0.2:
            self.angulo_atual -= 45
            self.tempo = time.time()
            if self.angulo_atual < 0:
                self.angulo_atual = 360 + self.angulo_atual

    def comando4(self):
        possui_tiro = 0
        for tiro in self.tiros:
            if tiro.player == self.player:
                possui_tiro += 1
                
        if  possui_tiro < 6 and time.time() - self.tempo_tiro > 0.3:
            tiro = Tiro(self.x, self.y, self.angulo_atual, player= self.player)
            tiro.shot[tiro.angulo](tiro)
            self.tiros.append(tiro)
            self.tempo_tiro = time.time()
          

    
           
    
    