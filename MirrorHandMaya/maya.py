# Modulo de comunicacao com o Maya
# Joao Carlos Cardoso - 2019

import socket

HOST = '127.0.0.1'
PORT = 7777
ADDRESS = (HOST,PORT)

def SendCommand(Command):
    maya = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #open socket
    maya.connect(ADDRESS)   #connect to maya

    maya.send(Command.encode())    #send command to maya
    data = maya.recv(1024)
    maya.close()

    print ('The Result is %s' %data)
