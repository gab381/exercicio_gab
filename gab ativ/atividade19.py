def maior_elemento(lista):
    if not lista:
        return None
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior
print(maior_elemento([3, 7, 2, 9, 4]))
print(maior_elemento([-5,-1,-10]))