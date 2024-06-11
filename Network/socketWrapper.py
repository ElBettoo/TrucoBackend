import aiohttp.web
import socketio
import tracemalloc

from Network.SalaWrapper import SalaWrapper
from Network.SocketsConnectedWrapper import SocketsConnectedWrapper
from Network.UsersConnectedWrapper import UsersConnectedWrapper              
class SocketIOApp:
    def __init__(self):

        self.__sala_wrapper = SalaWrapper()
        self.__sockets_connected_wrapper = SocketsConnectedWrapper()
        self.__users_connected_wrapper = UsersConnectedWrapper()

        self.sio = socketio.AsyncServer(cors_allowed_origins="*")
        self.app = aiohttp.web.Application()
        self.sio.attach(self.app)

    async def run(self):
            tracemalloc.start()
            runner = aiohttp.web.AppRunner(self.app)
            await runner.setup()
            site = aiohttp.web.TCPSite(runner, 'localhost', 8080)
            await site.start()


    #Metodos De la composion

    def add_user_socket(self, new_user_socket):
        self.sockets_connected_wrapper.add_user_socket(new_user_socket)
        
    def remove_user_socket(self, sid):
        self.sockets_connected_wrapper.remove_user_socket(sid)


    
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

    @property
    def sala_wrapper(self):
        return self.__sala_wrapper
    
    @property
    def sockets_connected_wrapper(self):
        return self.__sockets_connected_wrapper
    
    @property
    def users_connected_wrapper(self):
        return self.__users_connected_wrapper

WRAPPER = SocketIOApp()