mi_diccionario = {
    'Jorge' : 21,
    'Francisco' : 29,
    'Pedro' : 33
}

print(mi_diccionario)
print(mi_diccionario['Jorge'])

for valor in mi_diccionario.values():
    print(valor)

for clave,valor in mi_diccionario.items():
    print(clave,valor)