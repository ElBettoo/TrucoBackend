from Mazo import mazo
import random

class Ronda:
    def __init__(self) -> None:
        self.mazo = mazo.Mazo()
        self.banned_cards = []
    
    def set_banned_cards(self, banned_cards) -> list:
        for i in banned_cards:
            self.banned_cards.append(i)

    def repartir_cartas(self) -> list : 
        i = 0 
        player_cards = []
        while i < 3:
            current_card = random.choice(self.mazo.mazo).__dict__
            if current_card not in self.banned_cards:
                player_cards.append(current_card)
                self.banned_cards.append(current_card) 
                i += 1
        return player_cards
    
    def who_wins(self, player_cards)->list:

        win_card = {'cartaNumero': '000', 'numero': '00', 'palo': '0', 'nombre': 'prueba', 'valor': 999999999}
        empate = []

        for card in player_cards:
            if card["valor"] < win_card["valor"]:
                win_card = card
                empate = []
            elif card["valor"] == win_card["valor"]:
                empate.append(win_card)
                empate.append(card)

        print(len(empate))

        if len(empate) > 0:
            return empate
        else: 
            return win_card


        
