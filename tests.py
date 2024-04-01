from Sala import sala
from Usuario import usuario 
import random

user = usuario.Usuario("Porky")
user2 = usuario.Usuario("Joaquin Caca En El Crebo")

sala_jugando = sala.Sala("porky123", 2, False, 30, ["porky 123", "joacocucho 45"] )

user.set_jugador()
user.obtener_cartas(sala_jugando.ronda.repartir_cartas())
user2.set_jugador()
user2.obtener_cartas(sala_jugando.ronda.repartir_cartas())

print("\n", "Cartas de: " , user.username ,"\n")

for idx, card in enumerate(user.perform_get_mano()):
    print(idx, card)

print("\n", "Cartas de: " , user2.username ,"\n")

for idx, card in enumerate(user2.perform_get_mano()):
    print(idx, card)

print("XD:", user.perform_tirar_carta(0))

sala_jugando.ronda.cartas_jugadas.append(user.perform_tirar_carta(0))
sala_jugando.ronda.cartas_jugadas.append(user2.perform_tirar_carta(0))

print(sala_jugando.ronda.cartas_jugadas[0],sala_jugando.ronda.cartas_jugadas[1])

print("El ganador es:", sala_jugando.ronda.get_winner(sala_jugando.ronda.cartas_jugadas))
