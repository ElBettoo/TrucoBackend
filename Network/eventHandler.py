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
    


    # EVENTOS
    async def on_connect(self, sid, environ):
        new_user_socket = UserSocket(sid)
        self.socket.add_user_socket(new_user_socket)

        print("El socket:", sid, 'se conectó')

    async def on_disconnect(self, sid):

        for sala in self.socket.get_active_rooms():
            for usuario in sala.users:
                if usuario.socket_id == sid:
                    sala.remove_user(usuario)
                    await self.socket.emit_to_sala(sala.codigo_sala, 'recibir_jugadores', sala.get_usernames())
                    
                    break

    async def on_tirar_carta(self,sid, SalaId, carta):
        current_sala = self.socket.get_sala(SalaId)
        for user in current_sala.users:
            if user.socket_id == sid: #Bien jugado sid 😀
                break

        #current_sala.add_carta_tirada({username: carta})
        current_sala.add_carta_tirada([user.username, carta, user.team.id])
        
        cartas_tiradas = (current_sala.cartas_tiradas)

        print('NIGGA PORKY KILL YOUR SELF')
        print(cartas_tiradas)
        
        await self.socket.emit_to_sala( SalaId, 'mostrar_cartas_repartidas', cartas_tiradas)


    async def on_join_room(self,sid,SalaId,Username):

        current_sala = self.socket.get_sala(SalaId)
        user_socket = self.socket.get_user_socket_by_socket_id(sid)
        current_user = Usuario(user_socket, Username)
        current_sala.add_user(current_user)


        await self.socket.sio.enter_room(sid, SalaId)
        await self.socket.emit_to_player(sid, 'join_room')

        if len(current_sala.users) >= 2:
            await self.socket.emit_to_sala(SalaId, 'recibir_jugadores', current_sala.get_usernames())

            current_sala.ronda.repartir_cartas()

            for user in current_sala.users:
                await self.socket.emit_to_player(user.get_socket_id(), 'recibir_cartas', user.get_mano())


   

