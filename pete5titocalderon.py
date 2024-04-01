from Sala import sala
from Usuario import usuario 
import random
import time


start_time = time.time()
def play_game():
    
    user = usuario.Usuario("Porky")
    user2 = usuario.Usuario("Joaquin Caca En El Crebo")
    user3 = usuario.Usuario("JUANI NIGGEER")
    user4 = usuario.Usuario("GALOFA INSANO")

    sala_jugando = sala.Sala("porky123", 2, False, 300, [user, user2])

    user.set_jugador()
    user2.set_jugador()
    user3.set_jugador()
    user4.set_jugador()

    user.obtener_cartas(sala_jugando.ronda.repartir_cartas())
    user2.obtener_cartas(sala_jugando.ronda.repartir_cartas())
    user3.obtener_cartas(sala_jugando.ronda.repartir_cartas())
    user4.obtener_cartas(sala_jugando.ronda.repartir_cartas())

    sala_jugando.agregar_jugador_equipo(user, 1)
    sala_jugando.agregar_jugador_equipo(user3, 1)
    sala_jugando.agregar_jugador_equipo(user2, 0)
    sala_jugando.agregar_jugador_equipo(user4, 0)

    idx = 0
    while sala_jugando.get_equipo(0).puntos_partida < sala_jugando.points_to_win and sala_jugando.get_equipo(1).puntos_partida < sala_jugando.points_to_win:
        

        while  sala_jugando.get_equipo(0).puntos_subronda < 2 and  sala_jugando.get_equipo(1).puntos_subronda < 2:
            
            sala_jugando.recibir_cartas( (user, user.perform_tirar_carta(idx)) )
            sala_jugando.recibir_cartas( (user2, user2.perform_tirar_carta(idx)) )
            sala_jugando.recibir_cartas( (user3, user3.perform_tirar_carta(idx)) )
            sala_jugando.recibir_cartas( (user4, user4.perform_tirar_carta(idx)) )

            ganador, carta_ganadora = sala_jugando.get_ronda().get_sub_ronda().get_winner_sub_round()

            sala_jugando.get_equipo(ganador.perform_get_num_equipo()).add_puntos_subronda()

    

            sala_jugando.get_ronda().get_sub_ronda().restore_cartas_jugadas_subronda()

            idx += 1


            #print("TESTOSTERONA: ", sala_jugando.get_equipo(0).get_puntos_ronda())
            #print("TESTOSTERONA: ", sala_jugando.get_equipo(1).get_puntos_ronda())

        if sala_jugando.get_equipo(0).puntos_subronda > sala_jugando.get_equipo(1).puntos_subronda:
            sala_jugando.get_equipo(0).add_puntos_ronda(1)
        elif sala_jugando.get_equipo(1).puntos_subronda > sala_jugando.get_equipo(0).puntos_subronda:
            sala_jugando.get_equipo(1).add_puntos_ronda(1)
        

        sala_jugando.get_equipo(0).reset_puntos_ronda()
        sala_jugando.get_equipo(1).reset_puntos_ronda()
        idx = 0

        sala_jugando.ronda.banned_cards = []
        user.obtener_cartas(sala_jugando.ronda.repartir_cartas()) 
        user2.obtener_cartas(sala_jugando.ronda.repartir_cartas())
        user3.obtener_cartas(sala_jugando.ronda.repartir_cartas())
        user4.obtener_cartas(sala_jugando.ronda.repartir_cartas())

    if sala_jugando.get_equipo(0).puntos_partida > sala_jugando.get_equipo(1).puntos_partida:
        return 0
    elif sala_jugando.get_equipo(1).puntos_partida > sala_jugando.get_equipo(0).puntos_partida:
        return 1
    else:
        return -1

# Play 100 games
results = {0: 0, 1: 0, -1: 0}
for _ in range(1000):
    winner = play_game()
    results[winner] += 1

end_time = time.time()
total_time = end_time - start_time

print("Results after 100 games:")
print("Team 0 wins:", results[0])
print("Team 1 wins:", results[1])
print("Draws:", results[-1])
print("Total time taken: {:.2f} seconds".format(total_time))