class SubRonda:
    def __init__(self, players) -> None:
        self.__players_sorted = players
        self.__registro_cartas_tiradas = []

    def add_carta_tirada(self, card, user, team_id):
        self.registro_cartas_tiradas.append({"card": card, "user": user, "team_id": team_id})

    def next_turn(self):
        pass

    def get_winner(self):

        max = self.registro_cartas_tiradas[0]
        for card in self.registro_cartas_tiradas:
            if card['card'].valor < max['card'].valor:
                max = card

        return max
        


    @property
    def registro_cartas_tiradas(self):
        return self.__registro_cartas_tiradas