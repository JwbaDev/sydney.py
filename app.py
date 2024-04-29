from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import asyncio
from sydney import SydneyClient
from dotenv import load_dotenv
import time

app = Flask(__name__,template_folder='./')
socketio = SocketIO(app)
load_dotenv()

async def ask_sydney(prompt, style="creative"):
    try:
        async with SydneyClient(style=style) as sydney:
            print(style)
            print(prompt)
            if prompt == "!reset":
                await sydney.reset_conversation()
                return "Conversation reset."
            responses = []
            start_time = time.time()
            async for response in sydney.ask_stream(prompt):
                responses.append(response)
            elapsed_time = time.time() - start_time
            return ''.join(responses), elapsed_time
    except Exception as e:
        return str(e), 0

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send_message')
def handle_message(data):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    message, elapsed_time = loop.run_until_complete(ask_sydney(data['message'], data['style']))
    print(message)
    emit('receive_message', {'message': message, 'elapsed_time': elapsed_time})

if __name__ == '__main__':
    socketio.run(app, debug=True)
