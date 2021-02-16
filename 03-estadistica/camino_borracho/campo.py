class Campo:

    def __init__(self):
        self.coordenadas_de_borrachos = {}

    def anadir_borracho(self,borracho,coordenada):
        self.coordenadas_de_borrachos[borracho] = coordenada

    def mover_borracho(self,borracho):
        del