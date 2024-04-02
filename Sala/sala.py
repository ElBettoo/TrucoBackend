from .ronda import Ronda
from .equipo import Equipo


class Sala:
    def __init__(self, codigo_sala, cantidad_jugadores, has_flor, points_to_win, jugadores_en_sala) -> None:

        self.codigo_sala = codigo_sala
        
        self.equipos = [Equipo("Los chinchulines "), Equipo("Skibidi sigma ")]

        self.ronda = Ronda(cantidad_jugadores)
        self.cantidad_jugadores = cantidad_jugadores
        self.has_flor = has_flor
        self.points_to_win = points_to_win
        self.jugadores_en_sala = jugadores_en_sala

    def get_ronda(self):
        return self.ronda

    def recibir_cartas(self, cartaTuple):

    
        if type(cartaTuple) == tuple:
            self.get_ronda().get_sub_ronda().append_to_cartas_jugadas_subronda(cartaTuple)
        else:
            print("NO ES UNA TUPLA")
        

    def agregar_jugador_equipo(self, jugador, num_equipo):
        jugador.perform_set_num_equipo(num_equipo)
        self.equipos[num_equipo].add_jugador(jugador)

    def mostrar_jugadores_equipo(self, num_equipo):
        return self.equipos[num_equipo].players
    
    def get_equipo(self, num_equipo):
        return self.equipos[num_equipo]
    
    def perform_get_winner_ronda(self):
        return self.ronda.get_winner(self.equipos[0], self.equipos[1])









    
