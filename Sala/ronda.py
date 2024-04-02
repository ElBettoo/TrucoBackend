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
    
    def get_winner(self, equipo1, equipo2):

        if (equipo1.puntos_subronda == 2) and  equipo1.puntos_subronda != equipo2.puntos_subronda:
            print("Gano el equipo: ", equipo1.nombre, "Puntos:", equipo1.puntos_subronda)
            return {"TerminoRonda": True, "EquipoGanador": equipo1}
        elif (equipo2.puntos_subronda == 2) and  equipo2.puntos_subronda != equipo1.puntos_subronda:
            print("Gano el equipo: ", equipo2.nombre, "Puntos:", equipo2.puntos_subronda)
            return {"TerminoRonda": True, "EquipoGanador": equipo2}
        elif equipo1.puntos_subronda == 3 and equipo2.puntos_subronda == 3:
            print("EMPATE")
            return equipo1, equipo2

        return {"TerminoRonda": False, "EquipoGanador": ""}
        
        


    def get_sub_ronda(self):
        return self.sub_ronda
        
