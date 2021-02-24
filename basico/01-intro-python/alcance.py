def operaciones(a,b,tipo):
    def suma(a,b):
        return a + b
    def resta(a,b):
        return a - b
    def multiplicacion(a,b):
        return a * b
    def division(a,b):
        return a / b
    
    if tipo == 'S':
        return suma(a,b)
    if tipo == 'R':
        return resta(a,b)
    if tipo == 'M':
        return multiplicacion(a,b)
    if tipo == 'D':
        return division(a,b)

print(operaciones(8,3,'S'))
print(operaciones(8,3,'R'))
print(operaciones(8,3,'M'))
print(operaciones(8,3,'D'))