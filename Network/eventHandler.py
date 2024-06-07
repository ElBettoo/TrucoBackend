import asyncio
from Network.socketWrapper import WRAPPER
from Usuario.Usuario import Usuario
from Mazo.Mazo import Mazo
from Usuario.UserSocket import UserSocket
from Game.Game import Game

class EventHandler:
    def __init__(self, game) -> None:
        self.__socket = WRAPPER
        self.__game = game

    @property
    def game(self):
        return self.__game

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



    async def on_disconnect(self, sid):
        self.socket.sockets_connected_wrapper.remove_user_socket(sid)
        await self.on_leave_room(sid)

    async def on_tirar_carta(self,sid, SalaId, carta):
        args = self.game.tirar_carta(sid, SalaId, carta)
        
        await self.socket.emit_to_sala( SalaId, 'mostrar_cartas_repartidas', args['cartas_tiradas'])

    async def on_update_points(self,sid,team_id, num):

        args = self.game.update_points(sid,team_id, num)
        await self.socket.emit_to_sala(args['current_sala'].codigo_sala, 'update_points', team_id, args['total_points'])
            
    async def on_leave_room(self, sid):
        self.game.leave_room(sid)

    async def on_switch_round(self, sid):
        args = self.game.switch_round(sid)

        for user in args['current_sala'].users:
                await self.socket.emit_to_player(user.get_socket_id(), 'recibir_cartas', user.get_mano())

    async def on_join_room(self,sid,SalaId,Username):

        args = self.game.join_room(sid, SalaId, Username)

        await self.socket.sio.enter_room(sid, SalaId)
        await self.socket.emit_to_player(sid, 'join_room')
        await self.socket.emit_to_sala(SalaId, 'recibir_jugadores', args["current_sala"].get_usernames())

    async def on_start_game(self, sid, state):
        args = self.game.start_game(sid, state)

        if args['game_ready']:
            for user in args['current_sala'].users:
                await self.socket.emit_to_player(user.get_socket_id(), 'recibir_cartas', user.get_mano())

    @property
    def socket(self):
        return self.__socket