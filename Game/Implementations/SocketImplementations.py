from .GameImplementations import GameImplementation

class SocketImplementation(GameImplementation):
    def __init__(self, socket, sala_wrapper, sockets_connected_wrapper) -> None:
        
        self.__socket = socket
        self.__sala_wrapper = sala_wrapper
        self.__sockets_connected_wrapper = sockets_connected_wrapper

    def join_room(self, *args): 
        
        sid, SalaId, Username = args[0]
        current_sala = self.sala_wrapper.get_sala(SalaId)      
        user_socket = self.sockets_connected_wrapper.get_user_socket_by_socket_id(sid) 


        new_user = self.socket.users_connected_wrapper.add_connected_user(user_socket, Username)
        current_sala.add_user(new_user)
        
        return {"current_sala": current_sala}

    def start_game(self, *args):
        sid, ready_status = args[0]
        current_sala = self.sala_wrapper.get_room_by_sid(sid)
        current_sala.users_ready += 1 if ready_status == True else -1
        

        if current_sala.users_ready == current_sala.tamaño_sala:
            current_sala.start()

        return {'current_sala': current_sala, 'game_ready': current_sala.started}

    def switch_round(self, *args):
        print("ARGS DEL TOILET SID: ", args)
        sid = args[0]
        sala = self.sala_wrapper.get_room_by_sid(sid)
        sala.create_new_round()

        return {'current_sala': sala}

    def tirar_carta(self, *args):
        sid, SalaId, carta = args[0]
        current_sala = self.sala_wrapper.get_sala(SalaId)
        for user in current_sala.users:
            if user.socket_id == sid: #Bien jugado sid 😀
                break
        
        #MODIFICAR ESTOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
        #current_sala.add_carta_tirada({username: carta})
        current_sala.add_carta_tirada(carta, user.username, user.team.id)

        cartas_tiradas = current_sala.ronda.get_all_cartas_tiradas()[0]

        print("cartas tiradas : ",  cartas_tiradas)

        return {'cartas_tiradas': cartas_tiradas}

    def leave_room(self, *args):
        sid = args[0]
        current_sala = self.sala_wrapper.get_room_by_sid(sid)

        if current_sala != None:
            user_socket = self.socket.sockets_connected_wrapper.get_user_socket_by_socket_id(sid)
            current_sala.remove_user(user_socket.user)

            print("user_socket", user_socket)

            self.socket.users_connected_wrapper.remove_connected_user(sid)

    def update_points(self, *args):
        sid,team_id, num = args[0]
        current_sala = self.sala_wrapper.get_room_by_sid(sid)
        current_sala.teams[team_id-1].points+=num

        return {'current_sala': current_sala, "total_points":current_sala.teams[team_id-1].points}

    def add_user_socket(self, *args):
        new_user_socket = args[0][0]
        self.sockets_connected_wrapper.add_user_socket(new_user_socket)


    @property
    def sockets_connected_wrapper(self):
        return self.__sockets_connected_wrapper 
    
    @property
    def socket(self):
        return self.__socket

    @property
    def sala_wrapper(self):
        return self.__sala_wrapper