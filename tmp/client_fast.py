import json
from fastapi import FastAPI
import socket

# Define the required host, port and control protocol
HOST = '127.0.0.1'
PORT = 8000
CONTROL_PROTOCOL = {'on': 'ON', 'off': 'OFF'}

# Connect to the specified host, port and protocol
s = socket.socket()
s.connect((HOST, PORT))

# Construct and initialize the app
app = FastAPI()


# Handle requests from the server
@app.on_event("startup")
async def startup_event():
    while True:
        data = s.recv(1024)
        data = json.loads(data)
        command = data.get('command')

        # Parse the command
        if command in CONTROL_PROTOCOL.keys():
            if command == 'on':
                print('ON')
            else:
                print('OFF')


# Handle graceful shutdown
@app.on_event("shutdown")
async def shutdown_event():
    s.close()

