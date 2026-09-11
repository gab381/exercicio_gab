def calcular_area_circulo(raio):
    pi=3.14
    area= pi * (raio**2)
    return area
raio_do_usuario=2
resultado=calcular_area_circulo (raio_do_usuario)
print(f"a area do usuario {raio_do_usuario} é :{resultado}")

def calcular_circulo(raio):
    pi=3.14
    area=pi *(raio**2)
    return area
raio_usuario=5
igual=calcular_circulo (raio_usuario)
print(f"a area do usuario {raio_usuario} é: {igual}")