import random

def media(numeros):
    return sum(numeros) / len(numeros)
    
if __name__ == '__main__':
    numeros = [random.randint(1,30) for i in range(20)]
    resultado = media(numeros)

    print(numeros)
    print(resultado)