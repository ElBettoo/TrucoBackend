import aiohttp.web
import socketio
import tracemalloc

from Sala.Sala import Sala as SalaClass
from Usuario.Usuario import Usuario


class SocketIOApp:
    def __init__(self):

        self.active_rooms = []
        
        self.sio = socketio.AsyncServer(cors_allowed_origins="*")
        self.app = aiohttp.web.Application()
        self.sio.attach(self.app)
        
    async def ping(self,sid):
        print("ping from: ", sid)
        await self.sio.emit("ping")

    async def run(self):
        tracemalloc.start()
        runner = aiohttp.web.AppRunner(self.app)
        await runner.setup()
        site = aiohttp.web.TCPSite(runner, 'localhost', 8080)
        await site.start()

    def on_event(self, *args):
        self.sio.on(*args)

    async def emit(self, *args):
        await self.sio.emit(*args)
    
    async def emit_to_sala(self, salaId, *args):
        await self.sio.emit(*args, to=salaId)

    # salas
    def get_active_rooms(self):
        return self.active_rooms

    def get_sala(self, SalaId):
        for sala_i in self.get_active_rooms():
            if sala_i.get_sala_code() == SalaId:
                return sala_i

        nueva_sala = SalaClass(SalaId)
        self.add_active_room(nueva_sala)
        return nueva_sala
                
    def add_active_room(self,sala)-> SalaClass:
        self.active_rooms.append(sala)