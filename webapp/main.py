from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()


class ConnectionManager:

    def __init__(self):

        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):

        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):

        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):

    await manager.connect(websocket)
    try:
        await manager.broadcast(f"{username} has enter the chat")

        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"{username}: {data}")
    except WebSocketDisconnect:
        
        manager.disconnect(websocket)
        await manager.broadcast(f"{username} has left the chat")