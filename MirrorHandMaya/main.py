# Arquivo principal software MirrorHand + Maya
# Necessário - Arduino, Autodesk Maya
# Joao Carlos Cardoso - 2019

import socket
import time
import serialinput as SerialInput
import numpy as np 
import matplotlib.pyplot as plt
#from scipy import signal



Serial = SerialInput.InitSerial()
Values = [0]*10
while(1): #MainLoop  
    Values = SerialInput.ReadSensors(SerialInput.ReadSerial(Serial))
    for i in range(len(Values)):
        print("Sensor", i, Values[i], sep=' - ')
    time.sleep(.2)
    
    #maya = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #maya.connect(("127.0.0.1", 7777))
    #ser =  serial.Serial(ARDUINO, timeout=1)


#if __name__ == '__main__':
