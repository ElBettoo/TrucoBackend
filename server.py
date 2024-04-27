from aiohttp import web
import socketio
import tracemalloc
import random


sio = socketio.AsyncServer(cors_allowed_origins="*",)
app = web.Application()
sio.attach(app)

tracemalloc.start()


@sio.event
def connect(sid, environ):
    print("el socket:  ", sid, 'se conecto')

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    web.run_app(app)



