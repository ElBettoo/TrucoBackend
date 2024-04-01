from Sala import sala, ronda
from Usuario import usuario 
import random

user = usuario.Usuario("Porky")

sala = sala.Sala("porky123", 2, False, 30, ["porky 123", "joacocucho 45"] )

mano = sala.ronda.repartir_cartas()

for card in mano:
    print(card)
print(sala.ronda.get_winner(mano))