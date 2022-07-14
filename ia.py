from socket import *
from threading import Thread
from mapa import Mapa
from jogo import Jogo
import pygame
from struct import pack, unpack
from time import sleep
from sys import argv
from random import randint

class Cliente(socket):
    def __init__(self, no_clientes, no_mapa):
        super().__init__(AF_INET,SOCK_STREAM)
        self.jogo = None
        self.meu_idx = 0
        self.conexao('localhost',8888)
        self.send(pack('!2i', no_clientes, no_mapa))
        self.no_clientes, self.no_mapa = unpack('!2i', self.recv(8))

    def conexao(self, ip, porta):
        super().connect((ip,int(porta)))
        
    def collect_data(self):
        aux = self.recv(1).decode()
        print(aux)
        self.meu_idx = int(aux)
        print(f'Você é o Player {self.meu_idx}/{self.no_clientes}')
        print(self.recv(25).decode())
        print(self.recv(1).decode())
        print(self.recv(1).decode())
        print(self.recv(1).decode())

    def recv_server(self):
        while True:

            for tanque_idx in range(len(self.jogo.tanques)):
                tanque = self.jogo.tanques[str(tanque_idx + 1)]

                tt = self.recv(24)
                a,b,c,d,e,f = unpack('!6i',tt)
                    
                tanque.x = a
                tanque.y = b
                tanque.velocidade = c
                tanque.angulo_atual = d
                tanque.vida = e
                if f > len(tanque.tiros):
                    tanque.comando4(self.no_mapa)
                    pygame.mixer.Sound('sounds/shot.wav').play()
            

    def send_server(self):
        sleep(5)
        while True:
            x = randint(1,4)
            m = str(x)
            mov = f'{m}'.encode()
            self.send(mov)
            mov = ''
            sleep(0.1)

    def game(self):
        mapa = Mapa(self.no_mapa)
        self.jogo = Jogo(self.no_clientes, mapa)
        self.collect_data()
        th = Thread(target=self.recv_server, daemon=True)
        th.start()
        tr = Thread(target=self.send_server, daemon=True)
        tr.start()
        
        self.jogo.loop_cliente()
        


if __name__ == '__main__':
    
    cliente = Cliente(1, 1)
    cliente.game()