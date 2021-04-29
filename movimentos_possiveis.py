from extrai_valor import extrai_valor as ev
from extrai_naipe import extrai_naipe as en
from lista_movimentos_possiveis import lista_movimentos_possiveis as lmp
def possui_movimentos_possiveis(lista):
    lista1 = []
    for x in range(len(lista)-1):
        y = lmp(lista,x)
        if y != []:
            lista1.append(y)      
    if len(lista1) != 0:
        return True
    else:
        return False                


