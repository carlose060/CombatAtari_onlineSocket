import pygame
from tanque import Tank
from configs.config import ConfigGerais
from colisoes.colisao_tiro import ColisaoTiro, ColisaoTiroMapa
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
        font = pygame.font.SysFont(None, 30)
        
        #pygame.mixer.Sound('sounds/theme.wav').play()
        while True:
            self.mapa.clock.tick(ConfigGerais.FPS)
            
            vidas_players = []
            for i in range(1,len(self.tanques)+1):
                vida = font.render(f"Vida P{i}: {str(self.tanques[str(i)].vida)}", True, ConfigGerais.BLACK)
                vidas_players.append(vida)
                
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                break
            
            self.mapa.screen.fill(ConfigGerais.BEJE)
            
            x, y= 40, 0 
            for vida in vidas_players:
                self.mapa.screen.blit(vida, [x, y])
                if x == 640: x = 40
                else: x += 600;continue   

                if y == 580: y = 0
                else: y += 580

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
                    colisaoShot = ColisaoTiroMapa.iscoliding[tiro.angulo]
                    if not colisaoShot(tiro, self.mapa.no_mapa):
                        ## Ta bugando as vezes sai mais de um tiro quando 
                        # Colide WTTFFF
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
    
    

