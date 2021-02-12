class Persona:

    def __init__(self,nombre):
        self.nombre = nombre
    
    def avanzar(self):
        print('Estoy caminando')


class Ciclista(Persona):

    def __init__(self,nombre):
        super().__init__(nombre)

    def avanzar(self):
        print('Estoy pedaleando')

def main():
    persona = Persona("Jorge")
    persona.avanzar()

    ciclista = Ciclista("Pedro")
    ciclista.avanzar()
    
if __name__ == '__main__':
    main()