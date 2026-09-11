def valor_com_desconto(preço,desconto):
    valor_final=preço*(1-desconto/100)
    return valor_final
resultado=valor_com_desconto(100.0,10.0)
igual=valor_com_desconto(250.0,20.0)
print(resultado)
print(igual)