def suma(a,b):
    total = a + b
    return total

print(suma(2,3))


def nombre_completo(nombre,apellido,inverso=False):
    if inverso:
        return f'{apellido} {nombre}'
    else:
        return f'{nombre} {apellido}'

print(nombre_completo('Jorge','Toledo'))
print(nombre_completo('Jorge','Toledo',True))
print(nombre_completo(apellido = 'Jorge',nombre='Toledo'))