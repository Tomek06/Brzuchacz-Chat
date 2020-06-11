import socket
import threading

from tkinter import *
from functools import partial

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),2004))

name_header = 3
msg_header = 8

username = input('your name:')
s.send(bytes('username' + f'{len(username):<{name_header}}' + username, "utf-8"))

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

class client_GUI:
    def __init__(self, master):
        print("instance created")
        self.master = master
        
        self.welcomeLabel = Label(master, text="welcome to the chat")
        self.welcomeLabel.pack()
        
        self.quitButton = Button(master, text='Quit', command=master.destroy)
        self.quitButton.pack()
        
        self.recipientEntry = Entry(master)
        self.recipientEntry.pack()
        
        self.recipient = ''
        
        self.submitButton = Button(master, text='Send', command=partial(self.get_input, self.recipientEntry))
        self.submitButton.pack()
        #self.master.update()
        #self.master.after(0, __init__)
        
    def get_input(self, entry_box):
        print("start")
        a = entry_box.get()
        self.recipientLabel = Label(self.master, text=a)
        self.recipientLabel.pack()
        self.recipient = a
        print("end")


t1 = threading.Thread(target=send_msg)
t2 = threading.Thread(target=recv_msg)

t1.start()
t2.start()


root = Tk()
GUI = client_GUI(root)
root.mainloop()


t1.join()
t2.join()
