from cria_baralho import cria_baralho as cb
from extrai_valor import extrai_valor as ev
from extrai_naipe import extrai_naipe as en
from lista_movimentos_possiveis import lista_movimentos_possiveis as lmp
from empilha import empilha as emp
from movimentos_possiveis import possui_movimentos_possiveis as pmp
from cor import cor

def loop(lista):
    cartas = ''
    print('O estado atual das cartas é: ')
    for i in lista:
        cartas += '{}. {}\n'.format(lista.index(i)+1, i)
    print(cartas)
    
def teste(x):
    try:
        int(x)
        return True
    except:
        return False
def start():
    start = 'x'
    while start != '':
        start = input('Aperte [Enter] para iniciar o jogo...')
    cartas = cb()
    x = ''
    for i in cartas:
        x += '{}. {} \n'.format(cartas.index(i) + 1, i)
    print(x)
def prog(cartas):
    if pmp(cartas):
        y = input('Escolha uma carta (digite um número entre 1 e {}):'.format(len(cartas)))
        if teste(y) and int(y) <= len(cartas):
            y = int(y) - 1
            movpossiveis = (lmp(cartas,y))
            if len(movpossiveis) == 1:
                cartas = emp(cartas, y, y - movpossiveis[0])
                loop(cartas)
                prog(cartas)
            elif len(movpossiveis) == 2:  
                z = int(input('Digite em qual carta você quer empilhar o {}. \n 1. {}\n 2. {}\nDigite o número da sua escolha:'.format(cartas[y], cartas[y-1],cartas[y-3])))
                if z == 1:
                    cartas = emp(cartas, y, y-1)
                    loop(cartas)
                    prog(cartas)
                elif z == 2:
                    cartas = emp(cartas, y, y-3)
                    loop(cartas)
                    prog(cartas)
            elif len(movpossiveis) == 0:
                print('Não tem movimentos possíveis para {}'.format(cartas[y]))
                prog(cartas)
        else:
            print('Posição inválida')
            prog(cartas)
    else:
        if len(cartas) == 1:
            print('Parabéns! Você venceu!')
        else:
            print('Não há mais nenhum movimento possível. Você perdeu :(')
    nov = input('Deseja jogar novamente? (sim/não)')
    if nov == 'sim':
        start()

print('Paciência Acordeão\n==================\nSeja bem-vindo(a) ao jogo de Paciência Acordeão!\nO objetivo deste jogo é colocar todas as cartas em uma mesma pilha.\n\nExistem apenas dois movimentos possíveis:\n\n1. Empilhar uma carta sobre a carta imediatamente anterior; \n2. Empilhar uma carta sobre a terceira carta anterior.\n\nDesde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.')
start()
prog(cb())
