import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),2004))

name_header = 3
msg_header = 8

while True:
    username = input('your name:')
    s.send(bytes('username' + f'{len(username):<{name_header}}' + username, "utf-8"))
    break

def send_msg():
    while True:
        #recipient length, msg length, recipient, msg
        recipient = input("your recipient:")
        msg = input("the message:")
        out_msg = f'{len(recipient):<{name_header}}' + f'{len(msg):<{msg_header}}' + recipient + msg
    
        s.send(bytes(out_msg, "utf-8"))

def recv_msg():
    while True:
        in_msg = s.recv(1024)
        print(in_msg.decode("utf-8"))

t1 = threading.Thread(target=send_msg)
t2 = threading.Thread(target=recv_msg)

t1.start()
t2.start()

t1.join()
t2.join()
