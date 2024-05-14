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
        self.socket.on_event('mostrar_carta_tirada', self.on_mostrar_carta_tirada)
    


    # EVENTOS
    async def on_connect(self, sid, environ):
        print("El socket:", sid, 'se conectó')

    async def on_disconnect(self, sid):
        for sala in self.socket.get_active_rooms():
            for usuario in sala.users:
                if usuario.socket_id == sid:
                    sala.remove_user(usuario)
                    await self.socket.emit_to_sala(sala.codigo_sala, 'recibir_jugadores', sala.get_usernames())
                    
                    break

    async def on_mostrar_carta_tirada(self,sid, SalaId, carta):
        current_sala = self.socket.get_sala(SalaId)
        for user in current_sala.users:
            if user.socket_id == sid:
                break

        #current_sala.add_carta_tirada({username: carta})
        current_sala.add_carta_tirada([user.username, carta, user.team.id])
        
        cartas_tiradas = (current_sala.cartas_tiradas)

        print('NIGGA PORKY KILL YOUR SELF')
        print(cartas_tiradas)
        
        await self.socket.emit_to_sala( SalaId, 'mostrar_cartas_repartidas', cartas_tiradas)

    async def on_repartir_cartas(self, sid, salaId):
        await self.socket.emit_to_sala(salaId, 'repartir_cartas', ['1', 'random.choice(100)', 'random.choice(1312412)'])

    async def on_join_room(self,sid,SalaId,Username):
        #print("El usuario: ", Username, "se unio a la sala: ", SalaId)

        current_sala = self.socket.get_sala(SalaId)
        current_user = Usuario(sid, Username) # es 0 o es 1 :v
        current_sala.add_user(current_user)

        await self.socket.sio.enter_room(sid, SalaId)
        await self.socket.emit_to_player(sid, 'join_room')

        if len(current_sala.users) >= 2:
            await self.socket.emit_to_sala(SalaId, 'recibir_jugadores', current_sala.get_usernames())

            current_sala.mazo.repartir_cartas(current_sala.users)

            player1 =  current_sala.users[0]
            player2 = current_sala.users[1]

            print("Jugador 1:", player1.team, [player1.get_mano()])
            print("Jugador 2:", player2.team, [player2.get_mano()])

            await self.socket.emit_to_player(player1.get_socket_id(), 'recibir_cartas', player1.get_mano())
            await self.socket.emit_to_player(player2.get_socket_id(), 'recibir_cartas', player2.get_mano())

   

