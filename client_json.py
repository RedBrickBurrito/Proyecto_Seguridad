import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def my_message(data):
    print('message received with ', data)
    #sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:2021')
ascp_msg = {"function": 1, "data":"Mensaje desde python"}
sio.emit('Mensaje ASCP', 'Hola desde python')
sio.wait()
