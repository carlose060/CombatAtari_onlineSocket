from socket import *
from threading import Thread
from mapa import Mapa
from jogo import Jogo
import pygame
from struct import unpack
from time import sleep


class Cliente(socket):
    def __init__(self):
        super().__init__(AF_INET,SOCK_STREAM)
        self.jogo = None

    def conexao(self, ip, porta):
        super().connect((ip,int(porta)))
        
    def collect_data(self):
        print(self.recv(25).decode())
        print(self.recv(25).decode())
        print(self.recv(1).decode())
        print(self.recv(1).decode())
        print(self.recv(1).decode())

    def recv_server(self):
        while True:
            tt = self.recv(24)
            a,b,c,d,e,f = unpack('!6i',tt)
                
            
            
            self.jogo.tanque1.x = a
            self.jogo.tanque1.y = b
            self.jogo.tanque1.velocidade = c
            self.jogo.tanque1.angulo_atual = d
            self.jogo.tanque1.vida = e
            if f > len(self.jogo.tanque1.tiros):
                self.jogo.tanque1.comando4()


            tt = self.recv(24)
            a,b,c,d,e,f = unpack('!6i', tt)
            self.jogo.tanque2.x = a
            self.jogo.tanque2.y = b
            self.jogo.tanque2.velocidade = c
            self.jogo.tanque2.angulo_atual = d
            self.jogo.tanque2.vida = e
            if f > len(self.jogo.tanque2.tiros):
                self.jogo.tanque2.comando4()


            

    def send_server(self):
        while True:
            #comandos = self.jogo.get_key()
            comandos = pygame.key.get_pressed()
            
            if comandos[pygame.K_UP]:
                mov = f'1'.encode()
                self.send(mov)
            if comandos[pygame.K_LEFT]:
                mov = f'2'.encode()
                
                self.send(mov)
            if comandos[pygame.K_RIGHT]:
                mov = f'3'.encode()
                self.send(mov)
            if comandos[pygame.K_SPACE]:
                mov = f'4'.encode()
                self.send(mov)
            mov = ''
            sleep(0.032)


    def game(self):
        mapa = Mapa()
        self.jogo = Jogo(mapa)
        self.collect_data()
        th = Thread(target=self.recv_server)
        th.start()
        tr = Thread(target=self.send_server)
        tr.start()
        self.jogo.loop_cliente()
        



if __name__ == '__main__':
    cliente = Cliente()
    cliente.conexao('localhost',8888)
    cliente.game()