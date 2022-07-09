from socket import *
from threading import Thread
from time import sleep
from mapa import Mapa
from jogo import Jogo
from struct import pack, unpack


class Servidor(socket):

    def __init__(self):
        super().__init__(AF_INET, SOCK_STREAM)
        self.clients = []
        self.jogo = None
    
    def bind(self, porta):
        super().bind(('',int(porta)))
    
    def listen(self):
        super().listen(1)

    def cliente(self, client, idx_tank: str):
        print(f'Cliente {idx_tank} conectado')
        client.send(f'{idx_tank}'.encode())
        while True:
            comando = client.recv(1).decode()
            try:
                if self.jogo.tanques[idx_tank].vida <= 0:
                    client.close()
                    return
                    
                acao = self.jogo.tanques[idx_tank].comandos[comando]
                acao(self.no_mapa)
                self.send_server()
            except KeyError:
                pass
            finally:
                comando = ''
    
    def send_server(self):
        for tanque_idx in range(len(self.jogo.tanques)):
            tanque = self.jogo.tanques[str(tanque_idx + 1)]

            x = tanque.x
            y = tanque.y
            v = tanque.velocidade
            a = tanque.angulo_atual
            h = tanque.vida
            t = len(tanque.tiros)
            tk = pack('!6i', int(x),int(y),int(v),int(a),int(h),int(t))

            for client_ in self.clients:
                try: client_.send(tk)
                except: pass

    def conexao(self):
        client, addr = self.accept()
        self.clients.append(client)

        self.no_clientes, self.no_mapa = unpack('!2i', client.recv(8))
        client.send(pack('!2i', self.no_clientes, self.no_mapa))

        th = Thread(target=self.cliente, args=(client, str(len(self.clients))), daemon=True)
        th.start()

        for i in range(1, self.no_clientes):
            client, addr = self.accept()
            self.clients.append(client)

            # Ignora caso o jogador 2 ou maior tente mandar mapa etc
            client.recv(8)
            client.send(pack('!2i', self.no_clientes, self.no_mapa))

            th = Thread(target=self.cliente, args=(client, str(len(self.clients))), daemon=True)
            th.start()

        mapa = Mapa(self.no_mapa)
        self.jogo = Jogo(self.no_clientes, mapa)
        
        for client_ in self.clients:
            client_.send('A partida vai começar'.encode())
            sleep(1)

        for i in range(3,0,-1):
            for client_ in self.clients:
                client_.send(str(i).encode())

            sleep(1)

        self.jogo.loop_server()
        
            
if __name__ == '__main__':
    server = Servidor()
    server.bind(8888)
    server.listen()
    server.conexao()