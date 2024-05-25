import aiohttp.web
import socketio
import tracemalloc

from Sala.Sala import Sala as SalaClass
from Usuario.Usuario import Usuario


class SocketIOApp:
    def __init__(self):

        self.active_rooms = []
        self.connected_users = []
        self.__connected_sockets = []
        
        self.sio = socketio.AsyncServer(cors_allowed_origins="*")
        self.app = aiohttp.web.Application()
        self.sio.attach(self.app)

    async def run(self):
        tracemalloc.start()
        runner = aiohttp.web.AppRunner(self.app)
        await runner.setup()
        site = aiohttp.web.TCPSite(runner, 'localhost', 8080)
        await site.start()

    def get_room_by_sid(self, sid): # Los juguetes lo ven todo
        for sala in self.get_active_rooms():
            for usuario in sala.users:
                if usuario.socket_id == sid:
                    # print("RTX ASMKDKASKDMASMK: ", sala.codigo_sala, sala.users)
                    return sala

    def on_event(self, *args):
        self.sio.on(*args)

    async def emit(self, *args):
        await self.sio.emit(*args)
    
    async def emit_to_sala(self, salaId, *args):
        event = args[0]
        event_data = []

        for x in args:
            if x == event:
                continue
            
            event_data.append(x)

        await self.sio.emit(to=salaId, event=event, data=event_data)
    
    async def emit_to_player(self, socketId, *args):
        event = args[0]
        event_data = []

        for x in args:
            if x == event:
                continue
            
            event_data.append(x)

        await self.sio.emit(to=socketId, event=event, data=event_data)

    # sockets
    @property
    def connected_sockets(self):
        return self.__connected_sockets
    
    def add_user_socket(self, user):
        self.connected_sockets.append(user)

    def get_user_socket_by_socket_id(self, sid):
        for user_socket in self.connected_sockets:
            if user_socket.socket_id == sid:
                return user_socket


    def remove_user_socket(self, user):
        self.connected_sockets.remove(user)

    # usuarios
    def add_connected_user(self, sid):
        user_object = Usuario(sid)
        self.connected_users.append(user_object)
        
    def remove_connected_user(self, user):
        self.connected_users.remove(user)

    # salas
    def get_active_rooms(self) -> SalaClass:
        return self.active_rooms

    def get_sala(self, SalaId):
        for sala_i in self.get_active_rooms():
            print("sala ID ACA: ", SalaId)
            if sala_i.codigo_sala == SalaId:
                return sala_i

        nueva_sala = SalaClass(SalaId)
        self.add_active_room(nueva_sala)
        return nueva_sala
                
    def add_active_room(self,sala)-> SalaClass:
        self.active_rooms.append(sala)

WRAPPER = SocketIOApp()