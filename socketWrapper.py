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
        
    
        @self.sio.event
        def connect(socket_id, _):
            print('connected', socket_id)

        @self.sio.event
        def disconnect(sid):
            print('disconnected ', sid)

        print('[SERVER] INITIALIZED')
            


objetoSocket = SocketWrapper()
app = objetoSocket.get_app()
sio = objetoSocket.get_sio()
sio.attach(app)

if __name__ == '__main__':
    web.run_app(app)