from dataclasses import dataclass

@dataclass
class Carta:
    _primaryKey: str
    _nombre: str
    _valor: int

    def __post_init__(self):
        self._numero = self._primaryKey[:2]
        self._palo = self._primaryKey[-1]

    def __str__(self):
        return self._nombre
    
    def __gt__(self, other_card_object):
        if isinstance(other_card_object, Carta):
            return self._valor < other_card_object.valor
        else:
            return True
    
    @property
    def key(self):
        return self._primaryKey

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