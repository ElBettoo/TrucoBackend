class Carta:
    def __init__(self, cartaNumeroYPalo, cartaNombre, cartaValor):
        self._primaryKey  = cartaNumeroYPalo
        self._numero = cartaNumeroYPalo[:2]
        self._palo = cartaNumeroYPalo[-1]
        self._nombre = cartaNombre
        self._valor = cartaValor

    def __str__(self):
        return self._nombre
    
    def __gt__(self, other_card_object):
        if isinstance(other_card_object, Carta):
            return self._valor < other_card_object.valor
        else:
            return True
        
    def __eq__(self, other_card_object):
        if isinstance(other_card_object, Carta):
            return self._valor == other_card_object.valor
        else: 
            return False
    
    @property
    def nombre(self):
        return self._nombre

    @property
    def valor(self):
        return self._valor
    
    @property
    def palo(self):
        return self._palo
    
    @property
    def numero(self):
        return self._numero

        
#joaquin tenes caca en el crebo