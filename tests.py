from Sala import sala
from Usuario import usuario 
import random

user = usuario.Usuario("Porky")

sala = sala.Sala("porky123", 2, False, 30, ["porky 123", "joacocucho 45"] )

print(user.get_role())

user.set_jugador()

print(user.get_role())

