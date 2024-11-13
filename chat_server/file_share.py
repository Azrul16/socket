from flask import Flask, render_template, request, send_from_directory
from flask_socketio import SocketIO, send
import socket
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
socketio = SocketIO(app)

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Get local IP address
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        file_url = f"http://{local_ip}:5000/uploads/{file.filename}"
        socketio.emit('file_uploaded', file_url)
        print(f"File saved to {file_path}, accessible at {file_url}")
        return '', 204
    print("No file found in the request")
    return 'File not found', 400

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    try:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(f"Attempting to serve file from {file_path}")
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except Exception as e:
        print(f"Error serving file {filename}: {str(e)}")
        return 'File not found', 404

@socketio.on('message')
def handle_message(msg):
    client_ip = request.remote_addr
    message_with_ip = f"{client_ip}: {msg}"
    print(f"Message: {message_with_ip}")
    send(message_with_ip, broadcast=True)

if __name__ == '__main__':
    print(f"Server is running on http://{local_ip}:5000")
    socketio.run(app, host='0.0.0.0', port=5000)
