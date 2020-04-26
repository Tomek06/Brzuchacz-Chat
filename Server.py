s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 2004))
s.listen(10)
while True:
    clientsocket, address = s.accept()
    print(f"connected {address}")
    clientsocket.send(bytes("you are in", "utf-8"))
    while True:
        msg = clientsocket.recv(clientsocket.getsockname()[1])
        print(msg.decode("utf-8"))
