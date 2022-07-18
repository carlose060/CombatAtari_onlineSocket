import pygame
from configs.config import ConfigGerais
from configs.config import ConfigObstaculos
from configs.config import ConfigAmbiente


class Mapa:
    
    def __init__(self, num=1):
        pygame.init()
       
        self.screen = pygame.display.set_mode(ConfigGerais.RESOLUCAO)
        pygame.display.set_caption(ConfigGerais.TITULO)
        self.clock = pygame.time.Clock()
        self.cantos = self.paredes()
        if not num in [1,2]:
            num = 1
        self.no_mapa = num
        self.obst = self.obstaculos(num)
        self.buff = pygame.image.load(f'{ConfigGerais.DIR_PATH_BUFF}')
       
    def paredes(self):
        # Tela do jogo x = 40-760 Y = 50-560
        # 720 x 510 resolução do jogo sem as paredes
        wall_left = pygame.Rect(ConfigAmbiente.parede_esquerda())
        wall_right = pygame.Rect(ConfigAmbiente.parede_direita())
        wall_up = pygame.Rect(ConfigAmbiente.parede_cima())
        wall_down = pygame.Rect(ConfigAmbiente.parede_baixo())

        obj6 = pygame.Rect(ConfigAmbiente.parede_tanque1())
        obj7 = pygame.Rect(ConfigAmbiente.parede_tanque2())

        return [wall_left, wall_right, wall_up, wall_down, obj6, obj7]

    def obstaculos(self, num):
        barreira = ConfigObstaculos.Obstaculos[f'Mapa{str(num)}']
        if num == 1:
            obj1 = pygame.Rect(barreira(1))
            obj4 = pygame.Rect(barreira(4))
            obj5 = pygame.Rect(barreira(5))

            return [obj1, obj4, obj5]
        else:
            return [pygame.Rect(barreira(1))]

    
    def draw_buff(self):
        local = ConfigAmbiente.localizacao['buff']
        x = local['x']
        y = local['y']
        self.screen.blit(self.buff, (x, y))

    


