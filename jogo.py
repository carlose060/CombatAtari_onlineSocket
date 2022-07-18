from threading import Thread
import pygame
from tanque import Tank
from configs.config import ConfigGerais
from colisoes.colisao_tiro import ColisaoTiro, ColisaoTiroMapa
from random import randint
from time import time
from time import sleep
from colisoes.colisao_buff import ColisaoBuff
from random import randint


class Jogo():
    def __init__(self, no_tanques, mapa):
        self.mapa = mapa
        self.buff_on = 0
        self.time_buff = time()
        self.receber = time()
        self.tanques = {
            str(i): Tank(player=i)
            for i in range(1, no_tanques+1)
        }
    
    def loop_musica(self):
        while True:
            pygame.mixer.Sound('sounds/theme.wav').play()
            sleep(103)

    def quit(self):
        self.mapa.clock.tick(ConfigGerais.FPS)
    
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return True

        self.mapa.screen.fill(ConfigGerais.BEJE)
        return False

    def draw_vidas(self, font):
        # Recupera as vidas para printar na tela
        vidas_players = []
        for i in range(1,len(self.tanques)+1):
            vida = font.render(f"Vida P{i}: {str(self.tanques[str(i)].vida)}", True, ConfigGerais.BLACK)
            vidas_players.append(vida)
        # Printa as vidas em cada canto
        x, y= 40, 0 
        for vida in vidas_players:
            self.mapa.screen.blit(vida, [x, y])
            if x == 640: x = 40
            else: x += 600;continue   

            if y == 580: y = 0
            else: y += 580

    def draw_objetos(self):
        # Printa as paredes e obstaculos do mapa
        try:
            for ob in self.mapa.obst:
                pygame.draw.rect(self.mapa.screen, ConfigGerais.WHITE, ob)
        except TypeError:
            pass
        for parede in self.mapa.cantos:
            pygame.draw.rect(self.mapa.screen, ConfigGerais.WHITE, parede)

    def existe_buff(self):
        if self.buff_on != 0:
            self.mapa.draw_buff()
            for idx, tanque in self.tanques.items():
                if ColisaoBuff.iscoliding(tanque):
                    self.time_buff = time()
                    tanque.time_buff = time()
                    tanque.buff = self.buff_on
                    if tanque.buff == 2:
                        tanque.intervalo_tiro = 0.05
                    if tanque.buff == 4:
                        tanque.velocidade = 8
                    if tanque.buff == 5:
                        tanque.invisivel()
                    print(f'Buff {tanque.BUFFS[tanque.buff]} ativado para o tanque {idx}')
                    return True


    def loop_cliente(self):
        font = pygame.font.SysFont(None, 30)
        th = Thread(target=self.loop_musica, daemon=True)
        th.start()
        while True:
            if self.quit():
                break
            
            self.draw_vidas(font)
            self.draw_objetos()

            # Printa os tanques e checa as colisões
            for index, tanque in self.tanques.items():
                tanque.checa_tempo_buff()
                tanque.draw(self.mapa.screen)

                for tiro in tanque.tiros:
                    colisao = ColisaoTiroMapa.iscoliding[tiro.angulo]
                    if not colisao(tiro, self.mapa.no_mapa):
                        colisaoShot = ColisaoTiro.iscoliding[tiro.angulo]
                        if not colisaoShot(tiro):
                            for outro_index, outro_tanque in self.tanques.items():
                                if index == outro_index: continue
                                if ColisaoTiro.colisao_tanque(tiro, outro_tanque):
                                        if outro_tanque.buff == 1: outro_tanque.buff = 0    
                                        try:
                                            tanque.tiros.remove(tiro)       
                                        except ValueError:
                                            pass                                      
                            if tiro in tanque.tiros: tiro.draw(self.mapa.screen)
                        else:
                            tanque.tiros.remove(tiro)
                    else:
                        tanque.tiros.remove(tiro)
            self.existe_buff()
            pygame.display.flip()
           
    def pos_colisao(self, outro_tanque,tiro,tanque):

        if outro_tanque.buff == 1: outro_tanque.buff = 0
        elif outro_tanque.buff == 3: pass # Invencivel
        else:
            # BUFF 6 ---  Tiro tira buff
            if tanque.buff == 6: outro_tanque.buff = 0  
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
        
    def loop_server(self):
        while True:
            if self.quit():
                break
        
            for index, tanque in self.tanques.items():
                tanque.checa_tempo_buff()
                # Printa os tanques
                tanque.draw(self.mapa.screen)

                for tiro in tanque.tiros:
                   
                    colisaoShot = ColisaoTiroMapa.iscoliding[tiro.angulo]
                    if not colisaoShot(tiro, self.mapa.no_mapa):
                        colisaoShot = ColisaoTiro.iscoliding[tiro.angulo]
                        if not colisaoShot(tiro):
                    #  Checa colisao do tiro com o mapa e obstaculos
                            for outro_index, outro_tanque in self.tanques.items():
                                if index == outro_index: continue
                                # Checa colisao do tiro com o tanque (menos o dono do tiro)
                                if ColisaoTiro.colisao_tanque(tiro, outro_tanque):
                                    self.pos_colisao(outro_tanque,tiro,tanque)
                            if tiro in tanque.tiros: tiro.draw(self.mapa.screen)
                        else:
                            tanque.tiros.remove(tiro)
                    else:
                        tanque.tiros.remove(tiro)      
            if time() - self.time_buff  > 20 and time() - self.time_buff < 20.03:
                self.buff_on = randint(1,6)
                print(f'Buff {self.buff_on} ativado')
            if self.existe_buff():
                sleep(0.032)
                self.buff_on = 0
            pygame.display.flip()
    
    

