from Sala.sala import Sala
from Usuario.usuario import Usuario

import random

user = Usuario("Porky")
user2 = Usuario("Joaquin Caca En El Crebo")
user3 = Usuario("JUANI NIGGEER")
user4 = Usuario("GALOFA INSANO")


sala_jugando = Sala("porky123", 2, False, 400, [user, user2, user3, user4] )


user.set_jugador()
user2.set_jugador()

user.obtener_cartas(sala_jugando.ronda.repartir_cartas())
user2.obtener_cartas(sala_jugando.ronda.repartir_cartas())

sala_jugando.agregar_jugador_equipo(user, 1)
sala_jugando.agregar_jugador_equipo(user2, 1)


print("CARTAS: ", user._username)
for x , idx in enumerate(user.perform_get_mano()):
    print(x , idx)

print("CARTAS: ", user2._username)
for x, idx in enumerate(user2.perform_get_mano()):
    
    print(x, idx)

for i in range (0,3):

    p = int(input("poko: \t"))
    j = int(input("DESCEREBRADO \t"))

    sala_jugando.recibir_cartas( (user, user.perform_tirar_carta(p)) )
    sala_jugando.recibir_cartas((user2, user2.perform_tirar_carta(j)))

    result = sala_jugando.get_ronda().get_sub_ronda().get_winner_sub_round()

    if type(result) == tuple:
        print("GANO 1 SOLO :", result[0]._username)
        sala_jugando.get_equipo(result[0].perform_get_num_equipo()).add_punto_subronda()
    else:
        print("EMPATE :V")
        sala_jugando.get_equipo(0).add_punto_subronda()
        sala_jugando.get_equipo(1).add_punto_subronda()

    print(sala_jugando.get_ronda().get_winner(sala_jugando.get_equipo(0), sala_jugando.get_equipo(1)))


