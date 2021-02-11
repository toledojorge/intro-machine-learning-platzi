def sumar(a,b):
    return a + b

def multiplicar(a,b):
    return a * b
    
def aplicar_operaciones(a,b):
    operaciones = [sumar, multiplicar]

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(a,b))

    return resultado

print(aplicar_operaciones(5,4))