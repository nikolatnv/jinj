import uvicorn
from fastapi import FastAPI
import json


# Creating the application
app = FastAPI()


@app.get("/")
async def main():
    return {"message": "Welcome to our server!"}


@app.get("/send")
async def send_command():
    # This is where the commands can  be sent in json format
    return {"command": "on"}

if __name__ == "__main__":
    uvicorn.run("serv_fast:app", host="127.0.0.1", port=8000)
