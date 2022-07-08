from socket import *
from threading import Thread
from time import sleep
from mapa import Mapa
from jogo import Jogo
from struct import pack


class Servidor(socket):

    def __init__(self):
        super().__init__(AF_INET, SOCK_STREAM)
        self.clients = []
        self.jogo = None
    
    def bind(self, porta):
        super().bind(('',int(porta)))
    
    def listen(self):
        super().listen(1)

    def cliente1(self, client):
        client.send('Esperando Player2'.encode())
        while True:
            comando = client.recv(1).decode()
            try:
                acao = self.jogo.tanques['1'].comandos[comando]
                acao()
                self.send_server()
            except KeyError:
                pass
            finally:
                comando = ''

    def cliente2(self, client2):
        client2.send('Voce eh o player 2'.encode())
        while True:
            comando = client2.recv(1).decode()
            try:
                acao = self.jogo.tanques['2'].comandos[comando]
                acao()
                self.send_server()
            except KeyError:
                pass
            finally:
                comando = ''
    
    def send_server(self):
            # t1 = []
            # t2 = []
            # t1.append(self.jogo.tanques[f'1'].x)
            # t1.append(self.jogo.tanques[f'1'].y)
            # t1.append(self.jogo.tanques[f'1'].velocidade)
            # t1.append(self.jogo.tanques[f'1'].angulo_atual)
            # t1.append(self.jogo.tanques[f'1'].vida)
            # t1.append(len(self.jogo.tanques[f'1'].tiros))
        
            # t2.append(self.jogo.tanques[f'2'].x)
            # t2.append(self.jogo.tanques[f'2'].y)
            # t2.append(self.jogo.tanques[f'2'].velocidade)
            # t2.append(self.jogo.tanques[f'2'].angulo_atual)
            # t2.append(self.jogo.tanques[f'2'].vida)
            # t2.append(len(self.jogo.tanques[f'2'].tiros))
            # ###### Não está passando o tiro ainda #####
            
            # t1 = pack('!6i', int(t1[0]),int(t1[1]),int(t1[2]),int(t1[3]),int(t1[4]),int(t1[5]))
            # t2 = pack('!6i', int(t2[0]),int(t2[1]),int(t2[2]),int(t2[3]),int(t2[4]),int(t2[5]))
            x1 = self.jogo.tanques[f'1'].x
            y1 = self.jogo.tanques[f'1'].y
            v1 = self.jogo.tanques[f'1'].velocidade
            a1 = self.jogo.tanques[f'1'].angulo_atual
            h1 = self.jogo.tanques[f'1'].vida
            t1 = len(self.jogo.tanques[f'1'].tiros)
            tk1 = pack('!6i', int(x1),int(y1),int(v1),int(a1),int(h1),int(t1))
            
            x2 = self.jogo.tanques[f'2'].x
            y2 = self.jogo.tanques[f'2'].y
            v2 = self.jogo.tanques[f'2'].velocidade
            a2 = self.jogo.tanques[f'2'].angulo_atual
            h2 = self.jogo.tanques[f'2'].vida
            t2 = len(self.jogo.tanques[f'2'].tiros)
            tk2 = pack('!6i', int(x2),int(y2),int(v2),int(a2),int(h2),int(t2))
            
            self.clients[0].send(tk1)
            self.clients[1].send(tk1)

            self.clients[0].send(tk2)
            self.clients[1].send(tk2)


    def conexao(self):
        client, addr = self.accept()
        self.clients.append(client)
        th = Thread(target=self.cliente1, args=(client,))
        th.start()

        client2, addr2 = self.accept()
        self.clients.append(client2)
        tr = Thread(target=self.cliente2, args=(client2,))
        tr.start()
 
        mapa = Mapa()
        self.jogo = Jogo(mapa)
        
        for client_ in self.clients:
            client_.send('A partida vai começar'.encode())
            sleep(1)
        for i in range(3,0,-1):
            client.send(f'{str(i)}'.encode())
            client2.send(f'{str(i)}'.encode())
            sleep(1)

        self.jogo.loop_server()
        
            
if __name__ == '__main__':
    server = Servidor()
    server.bind(8888)
    server.listen()
    server.conexao()