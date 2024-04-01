class Equipo:
    def __init__(self, nombre) -> None:
        self._nombre =  nombre
        self._players = []
        self._puntos_subronda = 0
        self._puntos_partida = 0
        self._puntos_ronda = 0

    def add_jugador(self, jugador):
        self._players.append(jugador)
    
    def add_puntos_subronda(self):
        self._puntos_subronda += 1 

    def add_puntos_ronda(self, cantidad_puntos):
        self._puntos_ronda += cantidad_puntos
    
    def reset_puntos_ronda(self):
        self._puntos_partida += self._puntos_ronda
        self._puntos_ronda = 0
        self._puntos_subronda = 0

    @property
    def players(self):
        return self._players
    
    @property
    def puntos_subronda(self):
        return self._puntos_subronda

    @property
    def puntos_ronda(self):
        return self._puntos_ronda
    
    @property
    def puntos_partida(self):
        return self._puntos_partida
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, otro_nombre):
        self._nombre = otro_nombre