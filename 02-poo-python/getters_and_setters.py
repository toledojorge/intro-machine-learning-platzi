class Persona:

    def __init__(self):
        pass

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = f'{nombre} - Platzi'
        
if __name__ == '__main__':
    persona = Persona()
    persona.nombre = 'Jorge'
    print(persona.nombre)