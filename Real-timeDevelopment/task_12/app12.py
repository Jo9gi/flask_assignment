'''12. Build a Flask app that updates data in real-time using WebSocket connections.'''

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Function to generate random data and emit it through the WebSocket connection
def generate_data():
    while True:
        temperature = random.uniform(20, 30)
        humidity = random.uniform(40, 60)
        socketio.emit('data_update', {'temperature': temperature, 'humidity': humidity}, namespace='/test')
        time.sleep(1)

# SocketIO event handler for client connections
@socketio.on('connect', namespace='/test')
def test_connect():
    print('Client connected')
    emit('data_update', {'message': 'Connected'})

if __name__ == '__main__':
    # Start the WebSocket data generation in a separate thread
    socketio.start_background_task(target=generate_data)
    socketio.run(app)
