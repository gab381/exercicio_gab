import math
def calcular_o_volume(raio):
     volume=(4/3)* math.pi*(raio**3)
     return volume
raio_exemplo=3
volume_resultado=calcular_o_volume(raio_exemplo)
print(f"o volume com a esfera com o raio {raio_exemplo} é igual a: {volume_resultado:.2f}")
def calcular_igual(raio):
     igual=(4/3)* math.pi*(raio**3)
     return igual
raio_equivalente=1
igual_resultado=calcular_igual(raio_equivalente)
print(f"o volume com a esfera com o raio {raio_equivalente} é igual a: {igual_resultado:.2f}")
