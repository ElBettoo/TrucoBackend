from Mazo.Mazo import Mazo

class Sala:
    def __init__(self, codigo_sala) :

        self.codigo_sala = codigo_sala
        self.usuarios = []
        self.mazo = Mazo()
        self.__cartas_tiradas = []
    
    def add_carta_tirada(self,cartaByUser):
        self.__cartas_tiradas.append(cartaByUser)

    @property
    def cartas_tiradas(self):
        return self.__cartas_tiradas

    def add_user(self, jugador):
        self.usuarios.append(jugador)

    def reset_mazo(self):
        self.mazo = Mazo()

    def get_users(self):
        return self.usuarios
    
    def get_usernames(self):
        lista = []
        for user in self.get_users():
            lista.append(user.username)
        return lista
    
    def get_sala_code(self):
        return self.codigo_sala
    
    def __str__(self) -> str:
        return self.codigo_sala