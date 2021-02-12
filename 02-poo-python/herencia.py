class Animal:
    
    def __init__(self,nombre,peso,altura):
        self.nombre = nombre
        self.peso = peso
        self.altura = altura

    def caminar(self):
        print('Estamos caminando')

class Perro(Animal):

    def __init__(self,peso,altura):
        super().__init__('Perro',peso,altura)


if __name__ == '__main__':
    perro = Perro(25,130)
    print(perro.nombre)
    print(perro.peso)
    print(perro.altura)
    perro.caminar()