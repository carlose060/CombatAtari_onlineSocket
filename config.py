class Config():
    DIR_PATH = f'./sprites/player_'
    RESOLUCAO = (800,600)
    TITULO = 'Combat War'
    C = {
        'Player1': [70, 300,-90],
        'Player2': [700, 300, 90]
    }
    FPS = 30

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BEJE = (210,180,140)

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
    
    def objeto(num):
        if num == 1:
            return 250,100,30,100
        if num == 2:
            return 250,410,30,100
        if num == 3:
            return 510, 100, 30, 100
        if num == 4:
            return 510, 410, 30, 100
        if num == 5:
            return 375, 280, 50, 50
    
    def objeto2(num):
        pass

    O = {
         'Mapa1': [objeto],
         'Mapa2': [objeto2]
        }
    