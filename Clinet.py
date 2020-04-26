s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),2004))
while True:
    msg = s.recv(2004)
    print(msg.decode("utf-8"))
    while True:
        s.send(bytes(input(), "utf-8"))
