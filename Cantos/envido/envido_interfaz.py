from abc import ABC, abstractmethod

class EnvidoInterfaz(ABC):

    def __init__(self, puntosPrevios):
        self._puntosPrevios = puntosPrevios