import asyncio


class EchoServerProtocol(asyncio.Protocol):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.line = ""

    def connection_made(self, transport):
        self.transport = transport
        client = transport.get_extra_info("peername")
        self.client = client
        print(f"Connection with client: {client} established.")
        self.transport.write(f"Hello {self.client}. I can see you.".encode())

    def connection_lost(self, exc):
        super().connection_lost(exc=exc)
        print(f"Connection with client: {self.client} is closed.")

    def data_received(self, data):
        decoded = data.decode()
        if self.line == "disconnect":
            self.transport.close()

        if data == "\r\n".encode():
            print(f"Message from {self.client}: \n"
                  f"{self.line}")
            if "hui" in self.line:
                self.transport.write("Server says: Ebi se".encode())
            self.line = ""

        else:
            self.line += decoded

    def eof_received(self):
        return False

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    future = loop.create_server(EchoServerProtocol, "127.0.0.1", 8888) #Only initiates the process of server creation
    server = loop.run_until_complete(future=future) #Finalizes the server creation process and returns a future
    try:
        print("Server starting...")
        loop.run_forever() #Starts the server
    except KeyboardInterrupt:
        print("Server is shutting down...")
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
