from Usuario.Usuario import Usuario
from Mazo.Mazo import Mazo
from Usuario.UserSocket import UserSocket
from .UserHandler import UserHandler
from Network.socketWrapper import WRAPPER




class GameService:
    def __init__(self, socket, user_handler, sala_wrapper, sockets_connected_wrapper, game_implementation) -> None:
        
        self.__socket = socket
        self.__user_handler = user_handler
        self.__sala_wrapper = sala_wrapper
        self.__sockets_connected_wrapper = sockets_connected_wrapper
        self.__game_implementation = game_implementation
    
    @property
    def game_implementation(self):
        return self.__game_implementation

    @property
    def sockets_connected_wrapper(self):
        return self.__sockets_connected_wrapper

    def join_room(self,*args):

        return self.game_implementation.join_room(args)
        
    def start_game(self, sid, ready_status):
        current_sala = self.sala_wrapper.get_room_by_sid(sid)
        current_sala.users_ready += 1 if ready_status == True else -1
        
        print("users ready: ", current_sala.users_ready)

        if current_sala.users_ready == current_sala.tamaño_sala:
            current_sala.start()

        return {'current_sala': current_sala, 'game_ready': current_sala.started}
            
    def switch_round(self, sid):
        sala = self.sala_wrapper.get_room_by_sid(sid)
        sala.create_new_round()

        return {'current_sala': sala}
    
    def tirar_carta(self, sid, SalaId, carta):
        current_sala = self.sala_wrapper.get_sala(SalaId)
        for user in current_sala.users:
            if user.socket_id == sid: #Bien jugado sid 😀
                break

        #current_sala.add_carta_tirada({username: carta})
        current_sala.ronda.subronda.add_carta_tirada(carta, user.username, user.team.id)

        cartas_tiradas = current_sala.ronda.get_all_cartas_tiradas()[0]

        print("cartas tiradas : ",  cartas_tiradas)

        return {'cartas_tiradas': cartas_tiradas}

    def leave_room(self, sid):
        current_sala = self.sala_wrapper.get_room_by_sid(sid)

        if current_sala != None:
            user_socket = self.socket.sockets_connected_wrapper.get_user_socket_by_socket_id(sid)
            current_sala.remove_user(user_socket.user)

            print("user_socket", user_socket)

            self.socket.users_connected_wrapper.remove_connected_user(sid)

    def update_points(self, sid,team_id, num):
        current_sala = self.sala_wrapper.get_room_by_sid(sid)
        current_sala.teams[team_id-1].points+=num

        return {'current_sala': current_sala, "total_points":current_sala.teams[team_id-1].points}

    @property
    def sockets_connected_wrapper(self):
        return self.__sockets_connected_wrapper

    @property
    def socket(self):
        return self.__socket
    @property
    def user_handler(self):
        return self.__user_handler

    @property
    def sala_wrapper(self):
        return self.__sala_wrapper