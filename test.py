import random
from Mazo import mazo, carta

mazo = mazo.Mazo()

rnd_card = random.choice(mazo.mazo)

carta = carta.Carta(rnd_card)

print(carta.__dict__)