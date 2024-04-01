class Equipo:
    def __init__(self, nombre) -> None:
        self.nombre =  nombre
        self.jugadores = []
        self.puntos_ronda = 0
        self.puntos_partida = 0

    def add_jugador(self, jugador):
        self.jugadores.append(jugador)

    def get_jugadores(self):
        return self.jugadores
    
    def sumar_punto_ronda(self):
        self.puntos_ronda +=1 
    
    def sumar_puntos_partida(self):
        self.puntos_partida += 1

    def get_puntos_ronda(self):
        return self.puntos_ronda

    def restart_puntos_ronda(self):
        self.puntos_ronda = 0

    def get_puntos_partida(self):
        return self.puntos_partida
    
    def get_nombre(self):
        return self.nombre