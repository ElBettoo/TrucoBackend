from Sala import sala
from Usuario import usuario 
import random

user = usuario.Usuario("Porky")
user2 = usuario.Usuario("Joaquin Caca En El Crebo")
user3 = usuario.Usuario("JUANI NIGGEER")
user4 = usuario.Usuario("GALOFA INSANO")


sala_jugando = sala.Sala("porky123", 2, False, 300, [user, user2] )


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


print("equipo 1:",sala_jugando.mostrar_jugadores_equipo(0))
print("equipo 2:", sala_jugando.mostrar_jugadores_equipo(1))



idx = 0
while sala_jugando.get_equipo(0).get_puntos_partida() < sala_jugando.points_to_win and sala_jugando.get_equipo(1).get_puntos_partida() < sala_jugando.points_to_win:
    
    
    while sala_jugando.get_equipo(0).get_puntos_ronda() < 2 and sala_jugando.get_equipo(1).get_puntos_ronda() < 2 :
        
        sala_jugando.recibir_cartas( (user,user.perform_tirar_carta(idx)) )
        sala_jugando.recibir_cartas( (user2,user2.perform_tirar_carta(idx)) )
        sala_jugando.recibir_cartas( (user3,user3.perform_tirar_carta(idx)) )
        sala_jugando.recibir_cartas( (user4,user4.perform_tirar_carta(idx)) )

        ganador, carta_ganadora = sala_jugando.get_ronda().get_sub_ronda().get_winner_sub_round()

        print("THE WINNER TAKES IT ALL:", ganador, "equipo n°: ", ganador.perform_get_num_equipo())
        print(carta_ganadora)

        sala_jugando.get_equipo(ganador.perform_get_num_equipo()).sumar_punto_ronda()

        print("PUNTOS DEL EQUIPO: ", sala_jugando.get_equipo(ganador.perform_get_num_equipo()).get_nombre() , sala_jugando.get_equipo(ganador.perform_get_num_equipo()).get_puntos_ronda())

        sala_jugando.get_ronda().get_sub_ronda().restore_cartas_jugadas_subronda()

        idx +=1

        print("IDX: ", idx) 

        #print("TESTOSTERONA: ", sala_jugando.get_equipo(0).get_puntos_ronda())
        #print("TESTOSTERONA: ", sala_jugando.get_equipo(1).get_puntos_ronda())

    if sala_jugando.get_equipo(0).get_puntos_ronda() > sala_jugando.get_equipo(1).get_puntos_ronda():
            print("equipo 0 +1")
            sala_jugando.get_equipo(0).sumar_puntos_partida()
    elif sala_jugando.get_equipo(1).get_puntos_ronda() > sala_jugando.get_equipo(0).get_puntos_ronda():
        print("equipo 1 +1")
        sala_jugando.get_equipo(1).sumar_puntos_partida()
    
    print("xd")
    sala_jugando.get_equipo(0).restart_puntos_ronda()
    sala_jugando.get_equipo(1).restart_puntos_ronda()
    idx = 0

    sala_jugando.ronda.banned_cards = []
    user.obtener_cartas(sala_jugando.ronda.repartir_cartas()) 
    user2.obtener_cartas(sala_jugando.ronda.repartir_cartas())
    user3.obtener_cartas(sala_jugando.ronda.repartir_cartas())
    user4.obtener_cartas(sala_jugando.ronda.repartir_cartas())
    
    print("sala_jugando.get_equipo(0).get_puntos_ronda(): ", sala_jugando.get_equipo(0).get_puntos_ronda())
    print("sala_jugando.get_equipo(1).get_puntos_ronda(): ", sala_jugando.get_equipo(1).get_puntos_ronda())



if sala_jugando.get_equipo(0).get_puntos_partida() > sala_jugando.get_equipo(1).get_puntos_partida():
    print("equipo 0 gano yipi jai jeii")
elif sala_jugando.get_equipo(1).get_puntos_partida() > sala_jugando.get_equipo(0).get_puntos_partida():
    print("equipo 1 gano wiiiii,")
    

print(sala_jugando.get_equipo(0).get_nombre()  ,sala_jugando.get_equipo(0).get_puntos_partida())
print(sala_jugando.get_equipo(1).get_nombre()  ,sala_jugando.get_equipo(1).get_puntos_partida())