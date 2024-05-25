from Mazo.Mazo import Mazo
from Ronda.SubRonda import SubRonda

class Ronda:
    def __init__(self, Mazo, users, teams) -> None:
        self.__mazo = Mazo
        self.__users = users
        self.__teams = teams
        self.__current_subronda = SubRonda(self.intercalate_users_by_team())
        self.__all_subrondas = [self.__current_subronda]

    def repartir_cartas(self):
        for user in self.users:
            chosen_cards = self.mazo.get_mano() 
            user.set_mano(chosen_cards)

    def add_carta_tirada(self, card):
        self.all_subrondas.append(card)
        self.subronda.add_carta_tirada(card)

    def intercalate_users_by_team(self):
        
        team1_users = self.teams[0].players
        team2_users = self.teams[1].players
        sorted_users = []

        print("team 2", team1_users)
        for user_pair_index in range(len(team1_users)):
            sorted_users.append(team1_users[user_pair_index])
            sorted_users.append(team2_users[user_pair_index])
            print("sorted", sorted_users)


        return sorted_users

    @property
    def users(self):
        return self.__users

    @property
    def mazo(self):
        return self.__mazo
    
    @property
    def teams(self):
        return self.__teams
    
    @property

    @property
    def sub_ronda(self):
        return self.__current_subronda