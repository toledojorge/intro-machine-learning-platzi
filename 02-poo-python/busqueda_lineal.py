import random

def busqueda_lineal(lista,objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    
    return match

if __name__ == '__main__':
    tamano_lista = int(input('De que tamaño es la lista: '))
    objetivo = int(input('Cual es el numero objetivo: '))

    lista = [random.randint(0,100) for i in range(tamano_lista)]

    se_encontro = busqueda_lineal(lista,objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"está" if se_encontro else "no está"} en la lista')