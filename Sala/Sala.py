from Mazo.Mazo import Mazo
from Usuario.Team import Team
from Ronda.Ronda import Ronda

class Sala:
    def __init__(self, codigo_sala) :

        self.__codigo_sala = codigo_sala
        self.__users = []
        self.__mazo = Mazo()
        self.__cartas_tiradas = []
        self.__ronda = Ronda(self.mazo, self.users)
        self.__teams = [Team(1), Team(2)]
    
    def add_carta_tirada(self,cartaByUser):
        self.cartas_tiradas.append(cartaByUser)

    def add_user(self, jugador):
        team_index = (len(self.users)+1) % 2
        jugador.team =  self.teams[team_index]

        self.users.append(jugador)
        self.teams[team_index].add_player(jugador)

        print(self.teams[team_index].players)

    def remove_user(self, jugador):
        self.users.remove(jugador)

    def get_usernames(self):
        lista = []
        for user in self.users:
            lista.append(user.username)
        return lista

    def switch_round(self):
        self.mazo.reset()

        self.__ronda = Ronda(self.mazo)


    @property
    def ronda(self):
        return self.__ronda

    @property
    def cartas_tiradas(self):
        return self.__cartas_tiradas

    @property
    def mazo(self):
        return self.__mazo

    @property
    def users(self):
        return self.__users
    
    @property
    def teams(self):
        return self.__teams

    @property
    def codigo_sala(self):
        return self.__codigo_sala
    
    @codigo_sala.setter
    def codigo_sala(self, new_code):
        self.__codigo_sala = new_code