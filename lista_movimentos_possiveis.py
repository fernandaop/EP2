from extrai_valor import extrai_valor as ev
from extrai_naipe import extrai_naipe as en
def lista_movimentos_possiveis(lista, x):
    lista1 = []
    if x == 0:
        return lista1
    elif 0 < x < 3:
        if ev(lista[x]) == ev(lista[x-1]) or en(lista[x]) == en(lista[x-1]):
            lista1.append(1)
        return lista1
    else:
        if ev(lista[x]) == ev(lista[x-1]) or en(lista[x]) == en(lista[x-1]):
            lista1.append(1)
        if ev(lista[x]) == ev(lista[x-3]) or en(lista[x]) ==en(lista[x-3]):
            lista1.append(3)
        return lista1