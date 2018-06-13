from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit
import time
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)

@app.route('/socketio_simple')
def index():
    return render_template('socketio_simple.html')

@socketio.on('client_event',namespace='/socketio_simple/test1')
def client_msg(msg):
    if msg['data'] == 'qytang':
        for i in range(9):
            emit('server_response', {'data': i})
            socketio.sleep(1)

    else:
        emit('server_response', {'data': msg['data']})
    
@socketio.on('connect_event',namespace='/socketio_simple/test1')
def connected_msg(msg):
    emit('server_response', {'data': msg['data']})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')