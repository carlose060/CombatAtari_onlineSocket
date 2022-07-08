from mapa import Mapa
from jogo import Jogo




if __name__ == '__main__':
    mapa = Mapa()
    jogo = Jogo(mapa)
    jogo.rede()
    jogo.loop()


# if __name__ == '__main__':
#     cliente = Cliente()
#     cliente.conexao('localhost',8888)