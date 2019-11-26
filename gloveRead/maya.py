# Modulo de comunicacao com o Maya
# Joao Carlos Cardoso - 2019

#Rodar o seguinte código no maya
#import maya.cmds as cmds
#cmds.commandPort(n="localhost:7777")

import errno
import socket

HOST = '192.168.100.91'
PORT = 7777
ADDRESS = (HOST,PORT)

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def OpenConnection():
    try:
        connection.connect(ADDRESS)   #connect to maya
        return True
    except:
        pass
    return False

def SendCommand(Command):

    connection.send(Command.encode())    #send command to maya
