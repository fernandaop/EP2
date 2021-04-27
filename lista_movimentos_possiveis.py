def lista_movimentos_possiveis(lista, x):
    lista1 = []
    if x == 0:
        return lista1
    elif lista[x][0] == lista[x-1][0] or lista[x][-1] == lista[x-1][-1]:
        lista1.append(1)
        if lista[x][0] == lista[x-3][0] and x > 2 or lista[x][-1] == lista[x-3][-1] and x > 2:
            lista1.append(3)
    return lista1