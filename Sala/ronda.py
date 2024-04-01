from Mazo.mazo import Mazo
from .subronda import SubRonda

import random

class Ronda:
    def __init__(self, numPlayers) -> None:
        self.mazo = Mazo()
        self.sub_ronda = SubRonda(numPlayers)
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
            current_random_card = self.mazo.mazo[random.randint(0,39)]
            if current_random_card.key not in self.banned_cards:
                player_cards.append(current_random_card)
                self.banned_cards.append(current_random_card.key) 
                cards_quantity += 1
        return player_cards
    
    def get_winner():
        #sacar el winner de la ronda aca, no de las cartas, eso ya lo hacemos en subronda.
        #aca hay qeu ver quien consiguió máas piuntos en la subronda
        # aunqeu enrealidad nose si importa mucho pq tambien hay qeu ahcer el TRUCO QUE DE AHÍ SACAS PUNTOS TMB
        
        pass

    def get_sub_ronda(self):
        return self.sub_ronda
        
