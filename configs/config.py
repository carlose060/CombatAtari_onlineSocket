class ConfigGerais():
    DIR_PATH = f'./sprites/player_'
    DIR_PATH_BUFF = f'./sprites/buff.png'
    RESOLUCAO = (800,600)
    TITULO = 'Combat War'
    FPS = 30
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BEJE = (210,180,140)
    

class ConfigAmbiente:
    def parede_esquerda():
        return 20, 30, 20, 550
    def parede_direita():
        return 760, 30, 20, 550
    def parede_cima():
        return 40, 30, 720, 20
    def parede_baixo():
        return 40, 560, 720, 20
    def parede_tanque1():
        return  120, 270, 20, 90
    def parede_tanque2():
        return  660, 270, 20, 90
    localizacao = {
        'Player1': {
            'x': 70,
            'y': 300,
        },
        'Player2': {
            'x': 700,
            'y': 300
        },
        'Player3': {
            'x': 385,
            'y': 80,
        },
        'Player4': {
            'x': 385,
            'y': 500
        },
        'buff': {
            'x': 150,
            'y': 300
        },
    }

class ConfigObstaculos:
    def objeto(num):
        if num == 1:
            return 250,100,30,100
        if num == 4:
            return 510, 410, 30, 100
        if num == 5:
            return 375, 280, 50, 50
    def objeto2(num):
        return 350, 255, 100, 100

    Obstaculos = {
         'Mapa1': objeto,
         'Mapa2': objeto2
        }
    