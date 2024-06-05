import asyncio
from Network.socketWrapper import WRAPPER
from Usuario.Usuario import Usuario
from Mazo.Mazo import Mazo
from Usuario.UserSocket import UserSocket

class EventHandler:
    def __init__(self) -> None:
        self.socket = WRAPPER

    def get_socket(self):
        return self.socket

    # METODOS
    def run_game(self):
        self.assign_events()

        print('[SERVER] Started')
        asyncio.get_event_loop().run_until_complete(self.socket.run())
        asyncio.get_event_loop().run_forever()

    def assign_events(self):
        self.socket.on_event('connect', self.on_connect)
        self.socket.on_event('disconnect', self.on_disconnect)
        self.socket.on_event('join_room', self.on_join_room)
        self.socket.on_event('tirar_carta', self.on_tirar_carta)
        self.socket.on_event('leave_room', self.on_leave_room)
        self.socket.on_event('update_points', self.on_update_points)
        self.socket.on_event('switch_round', self.on_switch_round)
        self.socket.on_event('start_game', self.on_start_game)
    
    # EVENTOS
    async def on_connect(self, sid, environ):
        new_user_socket = UserSocket(sid)
        self.socket.sockets_connected_wrapper.add_user_socket(new_user_socket)
        
        print("Conected users: ", self.socket.users_connected_wrapper.connected_users)
        print("Connected sockets: ", self.socket.sockets_connected_wrapper.connected_sockets)
        print("El socket:", sid, 'se conectó')

    async def on_disconnect(self, sid):
        self.socket.sockets_connected_wrapper.remove_user_socket(sid)
        await self.on_leave_room(sid)

    async def on_tirar_carta(self,sid, SalaId, carta):
        current_sala = self.socket.sala_wrapper.get_sala(SalaId)
        for user in current_sala.users:
            if user.socket_id == sid: #Bien jugado sid 😀
                break

        #current_sala.add_carta_tirada({username: carta})
        current_sala.ronda.subronda.add_carta_tirada(carta, user.username, user.team.id)

        cartas_tiradas = current_sala.ronda.get_all_cartas_tiradas()[0]

        print("cartas turadas : ",  cartas_tiradas)
        
        await self.socket.emit_to_sala( SalaId, 'mostrar_cartas_repartidas', cartas_tiradas)

    async def on_update_points(self,sid,team_id, type):

        current_sala = self.socket.sala_wrapper.get_room_by_sid(sid)
        await self.socket.emit_to_sala(current_sala.codigo_sala, 'update_points', team_id, type)
            
    
    async def on_leave_room(self, sid):
        current_sala = self.socket.sala_wrapper.get_room_by_sid(sid)

        if current_sala != None:
            user_socket = self.socket.sockets_connected_wrapper.get_user_socket_by_socket_id(sid)
            current_sala.remove_user(user_socket.user)

            print("user_socket", user_socket)

            self.socket.users_connected_wrapper.remove_connected_user(sid) 
        
        print("current_sala: ", current_sala)


        #print(f"USER: [{user_socket.user.username}] SOCKET: [{user_socket.socket_id}] se desconecto. Bien jugado sid")

    async def on_switch_round(self, sid):
        sala = self.socket.sala_wrapper.get_room_by_sid(sid)
        sala.create_new_round()
        

        for user in sala.users:
                await self.socket.emit_to_player(user.get_socket_id(), 'recibir_cartas', user.get_mano())


    async def on_join_room(self,sid,SalaId,Username):

        current_sala = self.socket.sala_wrapper.get_sala(SalaId)

        user_socket = self.socket.sockets_connected_wrapper.get_user_socket_by_socket_id(sid)
        
        self.socket.users_connected_wrapper.add_connected_user(user_socket, Username) # Esto no existia y no podias ver los usuarios conectados :V

        current_user = Usuario(user_socket, Username)
        user_socket.assign_user(current_user)
        current_sala.add_user(current_user)

        await self.socket.sio.enter_room(sid, SalaId)
        await self.socket.emit_to_player(sid, 'join_room')
        await self.socket.emit_to_sala(SalaId, 'recibir_jugadores', current_sala.get_usernames())

    async def on_start_game(self, sid, state):
        current_sala = self.socket.sala_wrapper.get_room_by_sid(sid)
        current_sala.users_ready += 1 if state else -1
        
        print("users ready: ", current_sala.users_ready)

        if current_sala.users_ready == current_sala.tamaño_sala:
            current_sala.start()
            
            for user in current_sala.users:
                    await self.socket.emit_to_player(user.get_socket_id(), 'recibir_cartas', user.get_mano())

