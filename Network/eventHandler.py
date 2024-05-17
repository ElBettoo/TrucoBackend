import asyncio
from Network.socketWrapper import SocketIOApp
from Usuario.Usuario import Usuario
from Mazo.Mazo import Mazo
from Usuario.UserSocket import UserSocket

class EventHandler:
    def __init__(self) -> None:
        self.socket = SocketIOApp()

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
    


    # EVENTOS
    async def on_connect(self, sid, environ):
        new_user_socket = UserSocket(sid)
        self.socket.add_user_socket(new_user_socket)

        print("El socket:", sid, 'se conectó')

    async def on_disconnect(self, sid):

        await self.on_leave_room(sid)

    async def on_tirar_carta(self,sid, SalaId, carta):
        current_sala = self.socket.get_sala(SalaId)
        for user in current_sala.users:
            if user.socket_id == sid: #Bien jugado sid 😀
                break

        #current_sala.add_carta_tirada({username: carta})
        current_sala.add_carta_tirada([user.username, carta, user.team.id])
        
        cartas_tiradas = (current_sala.cartas_tiradas)
        print(cartas_tiradas)
        
        await self.socket.emit_to_sala( SalaId, 'mostrar_cartas_repartidas', cartas_tiradas)

    async def on_update_points(self,sid, team_id, points):

        current_sala = self.socket.get_room_by_sid(sid)
        
        
        await self.socket.emit_to_sala(current_sala.codigo_sala, 'update_points',team_id, points)
            
    
    async def on_leave_room(self, sid):
        current_sala = self.socket.get_room_by_sid(sid)

        if current_sala != None:
            user_socket = self.socket.get_user_socket_by_socket_id(sid)
            current_sala.remove_user(user_socket.user)


        print(f"USER: [{user_socket.user.username}] SOCKET: [{user_socket.socket_id}] se desconecto. Bien jugado sid")



    async def on_join_room(self,sid,SalaId,Username):
        current_sala = self.socket.get_sala(SalaId)
        user_socket = self.socket.get_user_socket_by_socket_id(sid)
        current_user = Usuario(user_socket, Username)
        user_socket.assign_user(current_user)

        current_sala.add_user(current_user)


        await self.socket.sio.enter_room(sid, SalaId)
        await self.socket.emit_to_player(sid, 'join_room')

        if len(current_sala.users) >= 2:
            await self.socket.emit_to_sala(SalaId, 'recibir_jugadores', current_sala.get_usernames())

            current_sala.ronda.repartir_cartas()

            for user in current_sala.users:
                await self.socket.emit_to_player(user.get_socket_id(), 'recibir_cartas', user.get_mano())


   

