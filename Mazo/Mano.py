class Mano:
    def __init__(self, Cartas):
        self.__cartas = Cartas
        self.__cartas_in_hand = Cartas


    @property
    def cartas(self):
        return self.__cartas
    
    def __str__(self):
        texto = []
        for i in self.cartas:
            texto.append(str(i))

        return ', '.join(texto)
    
    def remove_card(self, carta_tirada):
        self.cartas_in_hand.remove(carta_tirada)

    @property
    def cartas_in_hand(self):
        return self.__cartas_in_hand
