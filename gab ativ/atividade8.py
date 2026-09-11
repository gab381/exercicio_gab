def conta_ocorrencias(lista, valor):
    """Retorna a quantidade de vezes que 'valor' aparece na 'lista'."""
    return lista.count(valor)
resultado = conta_ocorrencias([1, 2, 3, 2, 4, 2], 2)
igual= conta_ocorrencias([5,6,7],1)
print(resultado)
print(igual)