class Carta:
    def __init__(self, numero, palo, valor) -> None:
        self.__numero = numero
        self.__palo = palo
        self.__valor = valor

        

    
    def __str__(self):
        return self.nombre
    
    def __gt__(self, other_card_object):
        if isinstance(other_card_object, Carta):
            return self._valor < other_card_object.valor
        else:
            return True
        
    @property
    def key(self):
        return f'{self.palo[0]}{str(self.numero).zfill(2)}'

    @property
    def nombre(self):
        return f'{self.numero} de {self.palo}'

    @property
    def valor(self):
        return self.__valor
    
    @property
    def palo(self):
        return self.__palo
    
    @property
    def numero(self):
        return self.__numero
    
