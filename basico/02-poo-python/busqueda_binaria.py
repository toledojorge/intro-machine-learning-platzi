import random

def busqueda_binaria(lista,comienzo,final,objetivo,contador):
    contador = contador + 1
    if comienzo > final:
        return (False,contador)

    mitad = (comienzo + final) // 2

    if lista[mitad] == objetivo:
        return (True,contador)
    elif lista[mitad] < objetivo:
        return busqueda_binaria(lista,mitad +1, final, objetivo,contador)
    else:
        return busqueda_binaria(lista,comienzo, mitad -1, objetivo,contador)

if __name__ == '__main__':
    tamano_lista = int(input('De que tamaño es la lista: '))
    objetivo = int(input('Cual es el numero objetivo: '))

    lista = sorted([random.randint(0,100) for i in range(tamano_lista)])

    (se_encontro,contador) = busqueda_binaria(lista,0,len(lista)-1,objetivo,0)
    print(f'Numero iteracciones: {contador}')
    print(f'El elemento {objetivo} {"está" if se_encontro else "no está"} en la lista')