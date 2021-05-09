from random import shuffle
def cria_baralho():
    naipes = ['♠', '♥', '♦', '♣']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    lista = [v + n for n in naipes for v in valores]
    shuffle(lista)
    return lista
