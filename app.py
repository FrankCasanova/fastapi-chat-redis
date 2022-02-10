import asyncio

from broadcaster import Broadcast
from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
from starlette.websockets import WebSocketDisconnect

app = FastAPI

#You must run a docker container with Redis image.
broadcast = Broadcast('redis:localhost:6379')
#This will be the name of the channel to publish
#and subscribe to messages. (You could have more thant one)
CHANNEL = 'CHAT'

async def receive_messages(




