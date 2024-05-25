class SubRonda:
    def __init__(self, players) -> None:
        self.__players_sorted = players
        self.__cartas_tiradas = []

    def add_carta_tirada(self, new_card):
        self.cartas_tiradas.append(new_card)

    def next_turn(self):
        pass

    def get_winner(self):
        pass










    @property
    def cartas_tiradas(self):
        return self.__cartas_tiradas