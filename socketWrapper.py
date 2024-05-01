from aiohttp import web
import socketio
import tracemalloc

class SocketWrapper():
    sio = socketio.AsyncServer(cors_allowed_origins="*")
    app = web.Application()

    
    def __init__(self):
        self.initialize_server()
       
    def get_app(self):
        return self.app

    def get_sio(self):
        return self.sio


    # NECESESARIOOO
    def initialize_server(self):
        self.sio.attach(app)
        tracemalloc.start()

        
        @self.sio.event
        def connect(socket_id, _):
            print('connected', socket_id)

        @self.sio.event
        def disconnect(sid):
            print('disconnected ', sid)

        @self.sio.event
        def repartir_cartas(sid):  
            self.sio.emit(('repartir_cartas', ['011', '012', '123']))          
            


objetoSocket = SocketWrapper()
app = objetoSocket.get_app()

if __name__ == '__main__':
    web.run_app(app)