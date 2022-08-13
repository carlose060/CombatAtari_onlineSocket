# CombatAtari_onlineSocket
Trabalho pratico 2 - Redes - UFSJ 


Objetivo: O objetivo do trabalho prático é implementar o jogo Combat multiplayer utilizando a
biblioteca Sockets com conexão TCP e interface gráfica.
Descrição do Trabalho: O jogo deverá conter as seguintes características:
● Deverá ser implementado utilizando a biblioteca sockets e TCP.
● Deverá ter interface gráfica.
● O trabalho pode ser desenvolvido nas linguagens Python ou C.
● Deverá ser desenvolvido utilizando a arquitetura cliente-servidor. Primeiramente, o servidor é
iniciado. Quando dois clientes se conectarem com o servidor, o mesmo iniciará o jogo. Quando o
primeiro jogador se conecta ao servidor, ele deverá aguardar a conexão do segundo jogador.
Quando um jogo estiver em curso, não é necessário tratar novas conexões. Assim que o jogo
terminar, o servidor encerra a comunicação com os clientes. Para uma nova partida, todas as
etapas devem ser refeitas.
● Quando os dois jogadores se conectarem com o servidor, deverá aparecer na tela do jogador um
contador decrescente informando que o jogo está prestes a começar: 3.... 2.....1... READY!
● O campo deverá ter, pelo menos, duas barreiras iniciais cercando o jogador (conforme figura
abaixo).
● Quando um jogador for acertado, a rodada é encerrada e os tanques são recolocados em suas
respectivas posições iniciais.
● Cada jogador começa com três vidas e é eliminado quando atinge 0 vidas. O último jogador com
vida no campo é o vencedor.
● O placar indica a quantidade de vidas de cada jogador.
● O jogo inicia com os tanques em lados opostos da tela e atrás de uma barreira.


Pontos Extras: O aluno ganhará pontos extras para a realização de cada uma das seguintes tarefas
adicionais:
● Multiplayer com até 4 jogadores (2 pontos)
● Adicionar itens de auxílio aleatórios no mapa que podem ser pegos pelos jogadores e usados
por comando especial. Os itens podem ser acumulados em formato de pilha: o último item pego
é o primeiro a ser utilizado pelo comando especial (1 ponto para cada item).
  Armadura extra: o tanque ganha proteção contra um tiro do oponente
  Tiro rápido: o tanque aumenta a velocidade do disparo por alguns segundos
  Invulnerabilidade: o tanque fica invulnerável por alguns segundos
  Movimento rápido: o tanque aumenta a velocidade de movimento por alguns
segundos
  Invisibilidade: o tanque fica invisível na tela por alguns segundos (AS VEZES GERA BUGS)
  Tiro múltiplo: o tanque atira em várias direções por alguns segundos (NÃO IMPLEMENTADO)
  Tiro poderoso: o tiro do tanque ultrapassa barreiras por alguns segundos (NÃO IMPLEMENTADO)
  Tiro enfraquecedor: o tiro do tanque, além de matar, remove o item que estiver no
topo da pilha do oponente. Dura alguns segundos
● Efeitos sonoros: Música de fundo (1 ponto), barulhos compatíveis com eventos do jogo (1
ponto).
● Diferentes mapas para jogar (mínimo dois com layouts diferentes). O primeiro jogador escolhe
qual mapa será jogado (2 pontos)
● Adicionar um tanque controlado por uma IA que aparece aleatoriamente no cenário e cujo tiro
furta um item aleatório da pilha de itens que o jogador possuir. O jogador que matar o tanque
controlado pela IA ganha todos os itens furtados (4 pontos). (IA é uma classe herdada de cliente)
● Trocar a posição inicial de cada tanque a cada rodada (2 pontos)

Execução do programa!
Para executar o servidor, basta digitar ''python3 servidor.py'' no terminal, ele está coonfigurado pra ouvir na porta 8888
Para executar o cliente, basta digitar ''python3 cliente.py <qt_jogadores> <Num_Mapa> <Ip_do_servidor>'' valores padrão [1,1,'localhost'] 
Lembrando que, quantidade de jogadores e numero do mapa, é definido somente pelo player 1, caso outro player entre, será descartado.
