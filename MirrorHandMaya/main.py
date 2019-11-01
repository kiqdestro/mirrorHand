# Arquivo principal software MirrorHand + Maya
# Necessário - Arduino, Autodesk Maya
# Joao Carlos Cardoso - 2019

import maya as Maya
import time
import serialinput as SerialInput
import numpy as np 
import matplotlib.pyplot as plt
#from scipy import signal



Serial = SerialInput.InitSerial()
Values = [0]*10

def main():
    while(1): #MainLoop  
        Values = SerialInput.ReadSensors(SerialInput.ReadSerial(Serial))    #Get sensor list from serial
        for i in range(len(Values)):                                        #Loop
            print("Sensor", i, Values[i], sep=' - ')    #Print sensor values
            #Joint = 
        time.sleep(.2)

    Maya.SendCommand("rotate -r 90deg 0 0 joint2;")

if __name__=="__main__":
    main()


    
    #maya = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #maya.connect(("127.0.0.1", 7777))
    #ser =  serial.Serial(ARDUINO, timeout=1)


#if __name__ == '__main__':
