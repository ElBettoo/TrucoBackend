from Mazo.Carta import Carta
from Mazo.Mano import Mano
import random

palos = ['espada', 'oro', 'basto', 'copa']
especial = {'1espada':1, '1basto':2, '7espada':3, '7oro':4}

class Mazo:
    def __init__(self):
        self.mazo = []

        for num in range(1, 13):
            if num == 8 or num == 9:
                continue

            for palo in palos:
                id_carta = str(num)+palo
                valor_carta = 8-num if num < 4 else 18-num
                if id_carta in especial.keys():
                    valor_carta = especial[id_carta]

                self.mazo.append(Carta(num, palo, valor_carta))

    def repartir_cartas(self, jugadores):
        for jugador in jugadores:
            nueva_mano = Mano(self.get_mano())
            jugador.set_mano(nueva_mano)

    def get_mano(self):
        cartas = []
        for i in range(3):
            carta_elegida = random.choice(self.mazo)

            cartas.append(carta_elegida)
            self.mazo.pop(self.mazo.index(carta_elegida))

        return cartas
        