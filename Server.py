import socket
import sys
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 2004))
s.listen(10)

socket_list = {}
client_list = {}

name_header = 3
msg_header = 8

def new_connections():
    while True:
        client_socket, address = s.accept()
        new_thread = threading.Thread(target=accept_msgs, args=[client_socket])
        
        socket_list[client_socket] = new_thread
        socket_list[client_socket].start()
        print(f"connected {address}")

def accept_msgs(client_socket):
    while True:
        msg = client_socket.recv(1024).decode("utf-8")
        print(msg)
        #print(msg[3:8+name_header])
        if msg[:8] == 'username':  # identify new users
            username_length = msg[8:8+name_header]
            client_list[msg[8+name_header:8+name_header+int(username_length)]] = client_socket
            #print(client_list[client_socket])
        else:
            #sender length, msg length, sender, msg
            recipient_length = int(msg[0:name_header])
            recipient = msg[name_header:name_header+recipient_length]
            
            msg_length = int(msg[name_header:name_header+msg_header]) # msg length
            msg_strip = msg[name_header + msg_header + recipient_length: name_header + msg_header + recipient_length + msg_length]  # pure msg

            for x, y in client_list.items():
                if y == client_socket:
                    sender = x
            
            #adjusted_msg = f'{len(sender)<:{name_header}}' + f'{msg_length<:{msg_header}}' + sender + msg_strip #SOMETHING WRONG HERE
            adjusted_msg = sender + msg_strip

            print(adjusted_msg)

            if recipient in client_list:
                try:
                    client_list[recipient].send(bytes(adjusted_msg))
                except:
                    message_list
            else:
                #send "doesn't exist"
                client_socket.send(bytes("no such user found"))

t1 = threading.Thread(target=new_connections)
t1.start()

t1.join()

for x in client_list.key():
    socket_list[x].start()
