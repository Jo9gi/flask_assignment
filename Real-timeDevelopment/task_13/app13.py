'''13. Implement notifications in a Flask app using websockets to notify users of updates.'''

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    socketio.emit('message', msg, broadcast=True)
    socketio.emit('notification', 'New message: ' + msg)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0",port=5051)