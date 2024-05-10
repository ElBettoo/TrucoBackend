class Mano:
    def __init__(self, Cartas):
        self.__cartas = Cartas

    @property
    def cartas(self):
        return self.__cartas
    
    def __str__(self):
        texto = []
        for i in self.cartas:
            texto.append(str(i))

        return ', '.join(texto)