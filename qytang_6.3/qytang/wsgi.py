from qytang import application
from qytang import socketio


if __name__ == "__main__":
    socketio.run(application,host = '0.0.0.0')
