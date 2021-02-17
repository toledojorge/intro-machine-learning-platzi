import random
import math

def media(numeros):
    return sum(numeros) / len(numeros)
    
def varianza(numeros):
    lamedia = media(numeros)

    acumulador = 0
    for x in numeros:
        acumulador += (x - lamedia)**2

    return acumulador / len(numeros)

def desviacion_estandar(numeros):
    return math.sqrt(varianza(numeros))

if __name__ == '__main__':
    numeros = [random.randint(1,30) for i in range(20)]
    lamedia = media(numeros)
    lavariancia = varianza(numeros)
    ladesviacion = desviacion_estandar(numeros)

    print(f'Numeros= {numeros}')
    print(f'La media es= {lamedia}')
    print(f'La varianza es= {lavariancia}')
    print(f'La desviacion estandar es= {ladesviacion}')