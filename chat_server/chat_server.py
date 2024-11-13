from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
import socket

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Get local IP address
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(msg):
    try:
        client_ip = request.remote_addr
        message_with_ip = f"{client_ip}: {msg}"
        print(f"Message: {message_with_ip}")
        send(message_with_ip, broadcast=True)
    except Exception as e:
        print(f"Error handling message: {str(e)}")

if __name__ == '__main__':
    print(f"Server is running on http://{local_ip}:5000")
    socketio.run(app, host='0.0.0.0', port=5000)
