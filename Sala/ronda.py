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


        
