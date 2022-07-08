import pygame
from tanque import Tank
from configs.config import ConfigGerais
from colisoes.colisao_tiro import ColisaoTiro
from random import randint
from time import time
from mapa import Mapa


class Jogo():
    def __init__(self, mapa):
        self.mapa = mapa

        self.tanque1 = Tank(player=1)
        self.tanque2 = Tank(player=2)
        self.receber = time()
        self.tanques = {
            '1': self.tanque1,
            '2': self.tanque2,
        }
           
    def loop_cliente(self):
        font = pygame.font.SysFont(None, 50)
        while True:
            self.mapa.clock.tick(ConfigGerais.FPS)
            
            text = font.render(f'Vidas: {str(self.tanque1.vida)}', True, ConfigGerais.WHITE)
            text2 = font.render(f'Vidas: {str(self.tanque2.vida)}', True, ConfigGerais.WHITE)
            
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                break
            
            self.mapa.screen.fill(ConfigGerais.BEJE)
            self.mapa.screen.blit(text, [40, 0])
            self.mapa.screen.blit(text2, [640, 0])
            try:
                for ob in self.mapa.obst:
                    pygame.draw.rect(self.mapa.screen, ConfigGerais.WHITE, ob)
            except TypeError:
                pass
            for parede in self.mapa.cantos:
                pygame.draw.rect(self.mapa.screen, ConfigGerais.WHITE, parede) 
            self.tanque1.draw(self.mapa.screen)
            self.tanque2.draw(self.mapa.screen)
            for index in self.tanques: 
                for tiro in self.tanques[index].tiros:

                    colisaoShot = ColisaoTiro.iscoliding[tiro.angulo]
                    if colisaoShot(tiro) == False:
                        if index == '1':
                            if ColisaoTiro.colisao_tanque(tiro, self.tanque2) == True:
                                try:
                                    self.tanque1.tiros.remove(tiro)
                                except ValueError:
                                    pass

                        else:          
                            if ColisaoTiro.colisao_tanque(tiro, self.tanque1) == True:
                                try:
                                    self.tanque2.tiros.remove(tiro)
                                except ValueError:
                                    pass

                                
                        tiro.draw(self.mapa.screen)
                        tiro.movimento()
                    else:
                        self.tanques[index].tiros.remove(tiro)
        
            pygame.display.flip()
           

    def loop_server(self):
        
        #font = pygame.font.SysFont(None, 50)
        
        while True:
            self.mapa.clock.tick(ConfigGerais.FPS)
            #text = font.render(f'Vidas: {str(self.tanque1.vida)}', True, ConfigGerais.WHITE)
            #text2 = font.render(f'Vidas: {str(self.tanque2.vida)}', True, ConfigGerais.WHITE)
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                break
             
            self.mapa.screen.fill(ConfigGerais.BEJE)
            #self.mapa.screen.blit(text, [40, 0])
            #self.mapa.screen.blit(text2, [670, 0])
            # try:
            #     for ob in self.mapa.obst:
            #         pygame.draw.rect(self.mapa.screen, ConfigGerais.WHITE, ob)
            # except TypeError:
            #     pass
            # for parede in self.mapa.cantos:
            #     pygame.draw.rect(self.mapa.screen, ConfigGerais.WHITE, parede) 
            self.tanque1.draw(self.mapa.screen)
            self.tanque2.draw(self.mapa.screen)
            for index in self.tanques: 
                for tiro in self.tanques[index].tiros:

                    colisaoShot = ColisaoTiro.iscoliding[tiro.angulo]
                    if colisaoShot(tiro) == False:
                        if index == '1':
                            if ColisaoTiro.colisao_tanque(tiro, self.tanque2) == True:
                                self.tanque2.vida -= 1
                                self.tanque2.x = randint(40,730)
                                self.tanque2.y = randint(50,530)
                                try:
                                    self.tanque1.tiros.remove(tiro)
                                except ValueError:
                                    pass
                        else:                        
                            if ColisaoTiro.colisao_tanque(tiro, self.tanque1) == True:
                                self.tanque1.vida -= 1
                                self.tanque1.x = randint(40,730)
                                self.tanque1.y = randint(50,530)
                                try:
                                    self.tanque2.tiros.remove(tiro)
                                except ValueError:
                                    pass

                                
                        tiro.draw(self.mapa.screen)
                        tiro.movimento()
                    else:
                        self.tanques[index].tiros.remove(tiro)
        
            pygame.display.flip()
    
    

        
if __name__ == '__main__':
    mapa = Mapa()
    jogo = Jogo(mapa)
    jogo.lup()