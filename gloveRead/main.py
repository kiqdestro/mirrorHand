import time
import serialinput as si
import numpy as np
import matplotlib.pyplot as plt

serial = si.InitSerial()
maximum = [0]*10
minimum = [0]*10
values = [0]*10
value = 0

def main():

    input("Estique os dedos e pressione espaco para calibrar")
    start_time = time.time()
    elapsed_time = 0
    while(elapsed_time < 1):
        sensor_max = si.ReadSerial(serial)
        maximum[sensor_max[0]] = sensor_max[1]
        elapsed_time = time.time() - start_time
    
    input("Dobre os dedos e pressione espaco para calibrar")
    start_time = time.time()
    elapsed_time = 0
    while(elapsed_time < 1):
        sensor_min = si.ReadSerial(serial)
        minimum[sensor_min[0]] = sensor_min[1]
        elapsed_time = time.time() - start_time

    print(maximum)
    print(minimum)

    input("Aperte enter para iniciar")

    while(True):
        value = si.ReadSerial(serial)                                   #Loop
        #print("Sensor", i, Values[i], sep=' - ')                        #Print sensor values
        normalized_value = (1-((value[1]- minimum[value[0]])/(maximum[value[0]]-minimum[value[0]]))) #Convert Input to a rotation value between 0 and 90 deg
        if (normalized_value > 1):
            normalized_value = 1
        if (normalized_value < 0):
            normalized_value = 0
        print(value[1], minimum[value[0]], maximum[value[0]], minimum[value[0]], sep=' - ')                               
        command_string = "setAttr(\"joint" + str(value[0]+1) + ".rotateZ\"," + str(normalized_value*90) + ");"     #Build MEL command_string
        print(command_string)
        # Maya.SendCommand(command_string)                                 #Send MEL Commando to MAYA
        # time.sleep(.1)                                                     #Delay