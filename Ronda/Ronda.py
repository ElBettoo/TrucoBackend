from Mazo.Mazo import Mazo

class Ronda:
    def __init__(self, Mazo, users) -> None:
        self.__mazo = Mazo
        self.__users = users

    def repartir_cartas(self):
        for user in self.users:
            chosen_cards = self.mazo.get_mano() 
            user.set_mano(chosen_cards)

    @property
    def users(self):
        return self.__users

    @property
    def mazo(self):
        return self.__mazo