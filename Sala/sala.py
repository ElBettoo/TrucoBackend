from .ronda import Ronda

class Sala:
    def __init__(self, codigo_sala, cantidad_jugadores, has_flor, points_to_win, jugadores_en_sala) -> None:

        self.codigo_sala = codigo_sala
        self.ronda = Ronda()
        self.cantidad_jugadores = cantidad_jugadores
        self.has_flor = has_flor
        self.points_to_win = points_to_win
        self.jugadores_en_sala = jugadores_en_sala
