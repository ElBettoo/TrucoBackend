from Mazo.Carta import Carta
from Mazo.Mano import Mano
import random

palos = ['espada', 'oro', 'basto', 'copa']
especial = {'1espada':1, '1basto':2, '7espada':3, '7oro':4}

class Mazo:
    def __init__(self):
        self.__mazo = []
        self.__banned_cards = []

        for num in range(1, 13):
            if num == 8 or num == 9:
                continue

            for palo in palos:
                id_carta = str(num)+palo
                valor_carta = 8-num if num < 4 else 18-num
                if id_carta in especial.keys():
                    valor_carta = especial[id_carta]

                self.mazo.append(Carta(num, palo, valor_carta))


    def get_mano(self):
        cartas = []
        for i in range(3):
            carta_elegida = random.choice(self.mazo)
            while carta_elegida in self.banned_cards:
                carta_elegida = random.choice(self.mazo)

            cartas.append(carta_elegida)
            self.banned_cards.append(carta_elegida)

        return Mano(cartas)
    
    def reset(self):
        self.banned_cards = []

    @property
    def mazo(self):
        return self.__mazo

    @property
    def banned_cards(self):
        return self.__banned_cards
    
    @banned_cards.setter
    def banned_cards(self, new_cards):
        self.__banned_cards = new_cards
        