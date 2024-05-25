from Mazo.Mazo import Mazo
from Usuario.Team import Team
from Ronda.Ronda import Ronda

class Sala:
    def __init__(self, codigo_sala) :

        self.__codigo_sala = codigo_sala
        self.__users = []
        self.__mazo = Mazo()
        self.__cartas_tiradas = []
        self.__teams = [Team(1), Team(2)]
        self.__cantidad_jugadores = 0
        self.__tamaño_sala = 4
        self.__users_ready = 0
        self.__ronda = Ronda(self.mazo, self.users, self.teams)
        self.__started = False

    def start(self):
    
        if self.__tamaño_sala == len(self.users):
            self.create_new_round()
            self.started = True
            

    def add_user(self, jugador):
        if self.cantidad_jugadores + 1 > self.__tamaño_sala:
            return

        team_index = (len(self.users)+1) % 2
        jugador.team =  self.teams[team_index]

        self.users.append(jugador)
        self.teams[team_index].add_player(jugador)
        self.cantidad_jugadores += 1

        print(self.teams[team_index].players)

    def remove_user(self, User): # remove_user(sid=234234)
        self.users.remove(User)
        self.cantidad_jugadores -= 1

    def get_usernames(self):
        lista = []
        for user in self.users:
            lista.append(user.username)
        return lista

    def create_new_round(self):
        if self.started:
            self.mazo.reset()
            self.cartas_tiradas = []
            self.__ronda = Ronda(self.mazo, self.users, self.teams)
            self.ronda.repartir_cartas()

    @property
    def cantidad_jugadores(self):
        return self.__cantidad_jugadores
    
    @cantidad_jugadores.setter
    def cantidad_jugadores(self, nueva_cantidad):
        self.__cantidad_jugadores = nueva_cantidad


    @property
    def ronda(self):
        return self.__ronda

    @property
    def cartas_tiradas(self):
        return self.__cartas_tiradas
    
    @cartas_tiradas.setter
    def cartas_tiradas(self, new_value):
        self.__cartas_tiradas = new_value

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

    @property
    def users_ready(self):
        return self.__users_ready
    
    @users_ready.setter
    def users_ready(self, nuevo_valor):
        self.__users_ready = nuevo_valor

    @property
    def started(self):
        return self.__started
    
    @started.setter
    def started(self, newState):
        self.__started = newState

    @property
    def tamaño_sala(self):
        return self.__tamaño_sala