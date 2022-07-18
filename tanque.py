import pygame
from configs.config import ConfigGerais, ConfigAmbiente
from colisoes.colisao_tanque import Colisao, ColisaoMapa
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
        self.image = pygame.transform.rotate(self.image,270)
        self.angulo_atual = 0
        self.tempo = time.time()
        self.tempo_tiro = time.time()
        self.player = player
        self.tiros = []
        self.vida = 3
        self.buff = 0
        self.time_buff = 9999999999999999999999
        self.intervalo_tiro = 0.3
        self.comandos = {
            '1': self.comando1,  # UP -- ANDAR
            '2': self.comando2,  # ESQUERDA -- +45 angulo
            '3': self.comando3,  # DIREITA -- -45 angulo
            '4': self.comando4   # ESPAÇO -- TIRO
        }
        self.BUFFS ={ 
            1 : 'Armadura Extra', 
            2 : 'Tiros mais rapidos',
            3 : 'Invunerabilidade',
            4 : 'Mais velocidade',
            5 : 'Invisivel',
            6 : 'Tiro enfraquecedor',
            7 : 'Tiro poderoso', # nao implementado
            8 : 'Tiro Varios Angulos', # nao implementado
        }

    def invisivel(self):
        self.image = pygame.image.load(f'{ConfigGerais.DIR_PATH}invisivel.png')
        self.image = pygame.transform.rotate(self.image,270)
        self.angulo_atual = 0
    
    def cor_atual(self):
        self.image = pygame.image.load(f'{ConfigGerais.DIR_PATH}{str(self.player)}.png')
        self.image = pygame.transform.rotate(self.image,270)
        self.angulo_atual = 0

    def checa_tempo_buff(self):
        if self.buff == 5:
            if time.time() - self.time_buff >= 20:
                self.buff = 0
                self.cor_atual()
        elif self.buff == 1 or self.buff == 3:
            if time.time() - self.time_buff >= 20:
                self.buff = 0
    
    def checa_tempo_buff2(self):
        if self.buff == 4:
            if time.time() - self.time_buff >= 20:
                self.buff = 0
                self.velocidade = 4
    
    def checa_tempo_buff3(self):
        if time.time() - self.time_buff >= 20:
            if self.buff == 2:
                self.intervalo_tiro = 0.3
                self.buff = 0
            elif self.buff == 6:
                self.buff = 0
            elif self.buff == 8:
                self.buff = 0
                
    def atirar(self):
        tiro = Tiro(self.x, self.y, self.angulo_atual, player= self.player)
        tiro.shot[tiro.angulo](tiro)
        self.tiros.append(tiro)
        self.tempo_tiro = time.time()
            
    def draw(self,screen):         
        screen.blit(pygame.transform.rotate(self.image,self.angulo_atual),(self.x, self.y))
   
    def comando1(self, mapa):
        self.checa_tempo_buff2()
        colisao = ColisaoMapa.iscoliding[self.angulo_atual]
        if not colisao(self, mapa): 
            colisao = Colisao.iscoliding[self.angulo_atual]
            colisao(self)
        
    def comando2(self, mapa):
        if time.time() - self.tempo > 0.2:
            self.angulo_atual += 45
            self.tempo = time.time()
            if self.angulo_atual == 360:
                self.angulo_atual = 0
    
    def comando3(self, mapa):
        if time.time() - self.tempo > 0.2:
            self.angulo_atual -= 45
            self.tempo = time.time()
            if self.angulo_atual < 0:
                self.angulo_atual = 360 + self.angulo_atual

    def comando4(self, mapa):
        self.checa_tempo_buff3()
        if self.buff == 2:         
            self.atirar()

        elif len(self.tiros) < 6 and time.time() - self.tempo_tiro > self.intervalo_tiro :
            self.atirar()
          

    
           
    
    