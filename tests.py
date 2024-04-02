from Sala.sala import Sala
from Usuario.usuario import Usuario

import random

user1 = Usuario("Porky")
user2 = Usuario("Joaquin Caca En El Crebo")
user3 = Usuario("JUANI NIGGEER")
user4 = Usuario("GALOFA INSANO")


sala_jugando = Sala("porky123", 2, False, 400, [user1, user2] )


user1.set_jugador()
user2.set_jugador()

user1.obtener_cartas(sala_jugando.ronda.repartir_cartas())
user2.obtener_cartas(sala_jugando.ronda.repartir_cartas())

sala_jugando.agregar_jugador_equipo(user1, 1)
sala_jugando.agregar_jugador_equipo(user2, 0)


print("CARTAS: ", user1._username)
for idx, carta in enumerate(user1.perform_get_mano()):
    print(idx , carta)

print("CARTAS: ", user2._username)
for idx, carta in enumerate(user2.perform_get_mano()):
    print(idx, carta)

SomeoneWon = False
while not SomeoneWon:

    p = int(input("poko: \t"))
    j = int(input("ABBUUSSOOO: \t"))


    sala_jugando.recibir_cartas( user1, user1.perform_tirar_carta(p))
    sala_jugando.recibir_cartas( user2, user2.perform_tirar_carta(j))

    result = sala_jugando.get_ronda().get_sub_ronda().get_winner_sub_round()
    sala_jugando.get_ronda().get_sub_ronda().restore_cartas_jugadas_subronda()

    if type(result) == tuple:
        print("GANO 1 SOLO :", result[0]._username)
        sala_jugando.get_equipo(result[0].perform_get_num_equipo()).add_punto_subronda()
    else:
        print("EMPATE :V")
        sala_jugando.get_equipo(0).add_punto_subronda()
        sala_jugando.get_equipo(1).add_punto_subronda()

    RondaResultado = sala_jugando.get_ronda().get_winner(sala_jugando.get_equipo(0), sala_jugando.get_equipo(1))
    SomeoneWon = RondaResultado["TerminoRonda"]

EquipoGanador = RondaResultado["EquipoGanador"]
print(f"Gano: {EquipoGanador.nombre}  User: {EquipoGanador.players[0]}")


