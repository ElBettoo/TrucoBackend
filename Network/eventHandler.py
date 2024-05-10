import asyncio
from Network.socketWrapper import SocketIOApp
from Usuario.Usuario import Usuario
from Mazo.Mazo import Mazo

class EventHandler:
    def __init__(self) -> None:
        self.socket = SocketIOApp()


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
        self.socket.on_event('repartir_cartas', self.on_repartir_cartas)
    


    # EVENTOS
    async def on_connect(self, sid, environ):
        print("El socket:", sid, 'se conectó')

    async def on_disconnect(self, sid):
        print('Desconexión de', sid)

    async def on_repartir_cartas(self, sid, salaId):
        await self.socket.emit_to_sala(salaId, 'repartir_cartas', ['1', 'random.choice(100)', 'random.choice(1312412)'])

    async def on_join_room(self,sid,SalaId,Username):
        print("El usuario: ", Username, "se unio a la sala: ", SalaId)

        current_sala = self.socket.get_sala(SalaId)
        current_user = Usuario(sid, Username)
        current_sala.add_user(current_user)

        await self.socket.sio.enter_room(sid, SalaId)
        await self.socket.emit('joined_room')

        if len(current_sala.get_users()) >= 2:
            await self.socket.emit_to_sala(SalaId, 'recibir_jugadores', current_sala.get_usernames())

            print('Repartiendo cartas para jugadores', current_sala.get_usernames())
            current_sala.mazo.repartir_cartas(current_sala.get_users())

            player1 =  current_sala.get_users()[0]
            player2 = current_sala.get_users()[1]
    
            print("Jugador 1:", [player1.get_mano()])
            print("Jugador 2:", [player2.get_mano()])

            await self.socket.emit_to_player(player1.get_socket_id(), 'recibir_cartas', player1.get_mano())
            await self.socket.emit_to_player(player2.get_socket_id(), 'recibir_cartas', player2.get_mano())


          


    
