import pygame
from tanque import Tank
from configs.config import ConfigGerais
from colisoes.colisao_tiro import ColisaoTiro
from random import randint
from time import time
from mapa import Mapa


class Jogo():
    def __init__(self, no_tanques, mapa):
        self.mapa = mapa

        self.receber = time()
        self.tanques = {
            str(i): Tank(player=i)
            for i in range(1, no_tanques+1)
        }
           
    def loop_cliente(self):
        font = pygame.font.SysFont(None, 50)
        while True:
            self.mapa.clock.tick(ConfigGerais.FPS)
            
            text = font.render(f"Vidas: {str(self.tanques['1'].vida)}", True, ConfigGerais.WHITE)
            text2 = font.render(f"Vidas: {str(self.tanques['2'].vida)}", True, ConfigGerais.WHITE)
            
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

            for index, tanque in self.tanques.items(): 
                tanque.draw(self.mapa.screen)

                for tiro in tanque.tiros:
                    colisaoShot = ColisaoTiro.iscoliding[tiro.angulo]
                    if not colisaoShot(tiro):
                        for outro_index, outro_tanque in self.tanques.items():
                            if index == outro_index: continue

                            if ColisaoTiro.colisao_tanque(tiro, outro_tanque):
                                try:
                                    tanque.tiros.remove(tiro)
                                except ValueError:
                                    pass

                        tiro.draw(self.mapa.screen)
                        tiro.movimento()
                    else:
                        tanque.tiros.remove(tiro)
        
            pygame.display.flip()
           

    def loop_server(self):
        
        while True:
            self.mapa.clock.tick(ConfigGerais.FPS)
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                break
             
            self.mapa.screen.fill(ConfigGerais.BEJE)

            for index, tanque in self.tanques.items(): 
                tanque.draw(self.mapa.screen)

                for tiro in tanque.tiros:
                    colisaoShot = ColisaoTiro.iscoliding[tiro.angulo]
                    if not colisaoShot(tiro):
                        for outro_index, outro_tanque in self.tanques.items():
                            if index == outro_index: continue

                            if ColisaoTiro.colisao_tanque(tiro, outro_tanque):
                                
                                outro_tanque.vida -= 1

                                if outro_tanque.vida <= 0:
                                    outro_tanque.x = outro_tanque.y = 1000

                                else:
                                    outro_tanque.x = randint(40,730)
                                    outro_tanque.y = randint(50,530)
                                
                                try:
                                    tanque.tiros.remove(tiro)
                                except ValueError:
                                    pass

                        tiro.draw(self.mapa.screen)
                        tiro.movimento()
                    else:
                        tanque.tiros.remove(tiro)

            pygame.display.flip()
    
    

        
if __name__ == '__main__':
    mapa = Mapa()
    jogo = Jogo(mapa)
    jogo.lup()