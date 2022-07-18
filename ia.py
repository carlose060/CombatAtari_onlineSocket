from random import randint
from cliente import Cliente
from time import sleep


class IA(Cliente):
    def send_server(self):
        sleep(5)
        while True:
            x = randint(1,4)
            m = str(x)
            mov = f'{m}'.encode()
            self.send(mov)
            mov = ''
            sleep(0.1)



if __name__ == '__main__':
    
    cliente = IA(1, 1, 'localhost')
    cliente.game()