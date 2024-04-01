from Mazo import mazo
import random

class Ronda:
    def __init__(self) -> None:
        self.mazo = mazo.Mazo()
        self.banned_cards = []
        self.cartas_jugadas = []
        self.numero_subronda = 1
    
    def set_banned_cards(self, banned_cards) -> list:
        for i in banned_cards:
            self.banned_cards.append(i)

    def reset_banned_cards(self) -> None:
        self.banned_cards = []

    def repartir_cartas(self) -> list : 
        cards_quantity = 0 
        player_cards = []
        while cards_quantity < 3:
            current_random_card = random.choice(self.mazo.mazo)
            if current_random_card not in self.banned_cards:
                player_cards.append(current_random_card)
                self.banned_cards.append(current_random_card) 
                cards_quantity += 1
        return player_cards
    
    def get_winner(self, total_round_cards: dict)->list:
        win_card = ""
        empate = []

        for card in total_round_cards:
            if card > win_card:
                win_card = card
                empate = []
            elif card == win_card:
                empate.append(win_card, card)

        return win_card if len(empate) == 0 else empate


        
