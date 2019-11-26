# Modulo de comunicacao com o Maya
# Joao Carlos Cardoso - 2019

#Rodar o seguinte código no maya
#import maya.cmds as cmds
#cmds.commandPort(n="localhost:7777")

import socket

HOST = '127.0.0.1'
PORT = 7777
ADDRESS = (HOST,PORT)

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(ADDRESS)

def OpenConnection():
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #open socket
        connection.connect(ADDRESS)   #connect to maya
        return True
    except ConnectionRefusedError:
        return False

def SendCommand(Command):

    connection.send(Command.encode())    #send command to maya
