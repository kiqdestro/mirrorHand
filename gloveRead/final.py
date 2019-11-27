#! /usr/bin/python

from adafruit_servokit import ServoKit
import serialinput as si
import maya as maya
import itsAlive
import serial
import time
import os

kit = ServoKit(channels = 16)

dedos = [0.0, 0.0, 0.0, 0.0, 0.0] # ordem: polegar, indicador, medio, anelar, minimo (desativado , [0, 1], [2, 3], [4, 5], [6, 7])

class ServoControl():
    def __init__(self):
        
        # EXAMPLES:
        # kit.servo[0].angle = 180
        # kit.servo[0].actuation_range = 160
        # kit.servo[0].set_pulse_width_range(1000, 2000)


        # kit = ServoKit(channels = 16)
       
        kit.servo[4].set_pulse_width_range(520, 2650) # minimo
        kit.servo[3].set_pulse_width_range(500, 2650) # anelar
        kit.servo[2].set_pulse_width_range(520, 2600) # médio
        kit.servo[1].set_pulse_width_range(520, 2600) # indicador
        kit.servo[0].set_pulse_width_range(540, 2650) # polegar


        # kit.servo[0].set_pulse_width_range(625, 2580)
        # kit.servo[1].set_pulse_width_range(500, 2620)
        # kit.servo[2].set_pulse_width_range(500, 2620)
        # kit.servo[3].set_pulse_width_range(540, 2600)
        # kit.servo[4].set_pulse_width_range(540, 2650)
        # kit.servo[5].set_pulse_width_range(540, 2650) #A
        # kit.servo[6].set_pulse_width_range(520, 2600) #B
        # kit.servo[7].set_pulse_width_range(520, 2600) #C *this one is turning only something around 120 degrees
        # kit.servo[8].set_pulse_width_range(520, 2600) #D
        # kit.servo[9].set_pulse_width_range(520, 2650) #E
        # kit.servo[10].set_pulse_width_range(500, 2650) #F

    def setPos(self, servoID, position):
        kit.servo[servoID].angle = (position * 180)

bluetoothSerial = si.InitSerial()
maximum = [0]*13
minimum = [0]*13
values = [0]*13
oldvalues = [0]*13
sensor_max = [0]*13
sensor_min = [0]*13
value = [0]*13
ctrl = ServoControl()

def main():

    print ("Trying to connect to Maya, ^C to cancel")
    maya_connect = maya.OpenConnection()    
    if(maya_connect):
        print("Connected to maya")
    else: print("Maya connection not present")
    
    itsAlive.firstMovement()

    print("Estique os dedos e espere para calibrar")

    time.sleep(5)
    # input("Estique os dedos e pressione espaco para calibrar")

    start_time = time.time()
    elapsed_time = 0

    while(elapsed_time < 2):
    #while(True):
        sensor_max = si.ReadSerial(bluetoothSerial)
        #print("sensor_max " + str(sensor_max))
        #input("Enter to continue")

        try:
            # print("sensor_max[0]: " + sensor_max[0])
            # print("sensor_max[1]: " + sensor_max[1])
            maximum = sensor_max[:]
        except:
            elapsed_time = time.time() - start_time
            continue

        elapsed_time = time.time() - start_time
        
    itsAlive.closeHand()

    print("Dobre os dedos e espere para calibrar")

    time.sleep(5)
    
    # input("Dobre os dedos e pressione espaco para calibrar")
    start_time = time.time()
    elapsed_time = 0

    while(elapsed_time < 2):
        sensor_min = si.ReadSerial(bluetoothSerial)
#        print(sensor_min)

        try:
            # print("sensor_min[0]: " + sensor_min[0])
            # print("sensor_min[1]: " + sensor_min[1])
            minimum = sensor_min[:]
        except:
            elapsed_time = time.time() - start_time
            continue

        elapsed_time = time.time() - start_time

    # print(maximum)
    # print(minimum)

    # input("Aperte enter para iniciar")
    print("inicio")

    input()

    while(True):
        value = si.ReadSerial(bluetoothSerial)
        #value = si.ReadSerial(serial)                                   #Loop
        #print("Sensor", i, Values[i], sep=' - ')                       #Print sensor values  
        print("value: " + str(value))
        try:
            for i in range(len(value)):
                try:

                    #os.system("clear")
                    print(value[i], minimum[i], maximum[i], minimum[i], sep=' - ')
                    normalized_value = (1-((value[i]- minimum[i])/(maximum[i]-minimum[i]))) # Normalizing
                    if (normalized_value > 1):
                        normalized_value = 1
                    if (normalized_value < 0):
                        normalized_value = 0
                    old_normalized_value = normalized_value

                    # print("[{}, {}]".format(i, float(normalized_value)*180))

                    # ordem: polegar, indicador, medio, anelar, minimo (desativado , [0, 1], [2, 3], [4, 5], [6, 7])

                    if(i == 0 or i == 1):
                        dedos[1] += old_normalized_value / 2
                    
                    elif(i == 2 or i == 3):
                        dedos[2] += old_normalized_value / 2

                    elif(i == 4 or i == 5):
                        dedos[3] += old_normalized_value / 2

                    elif(i == 6 or i == 7):
                        dedos[4] += old_normalized_value / 2 

                    

                    # for i in range(1,5):
                        # print("dedo: {}, resultado: {}, valores individuais: [{}, {}]\n", format(i, sum(dedos[i])/2, dedos[i][0], dedos[i][1])),
                        # pos_value = sum(dedos[i][0], dedos[i][1])
                        # ctrl.setPos(i, (sum(dedos[i])/2))


                    # ctrl.setPos(i, normalized_value)
                    if(maya_connect):
                        CommandString = "setAttr(\"joint" + str(i+1) + ".rotateZ\"," + str(normalized_value*90) + ");"     #Build MEL CommandString
                        maya.SendCommand(CommandString)                                 #Send MEL Commando to MAYA
                
                except IndexError as index:
                    print("erro index: ")
                    print(index)
                    # input()
                    continue

                except ValueError as value:
                    print("erro value: ")
                    print(value)
                    # input()
                    continue

                except ZeroDivisionError as zero:
                    print(zero)
                    # input()
                    normalized_value = old_normalized_value
                    continue

            for i in range(1, 5):
                print("dedos[i]: " + str(dedos[i]))
                ctrl.setPos(i, dedos[i])
                dedos[i] == 0.0

            if(maya_connect):
                try:
                    CommandString = "setAttr(\"b.rotateX\"," + str(value[10]*-1) + ");"     #Build MEL CommandString
                    maya.SendCommand(CommandString)                                 #Send MEL Commando to MAYA
                    CommandString = "setAttr(\"b.rotateY\"," + str(value[11]*-1) + ");"     #Build MEL CommandString
                    maya.SendCommand(CommandString)                                 #Send MEL Commando to MAYA
                    CommandString = "setAttr(\"b.rotateZ\"," + str(value[12]) + ");"     #Build MEL CommandString
                    maya.SendCommand(CommandString)                                 #Send MEL Commando to MAYA
                except TypeError:
                    print("TypeError IMU")
                    pass
        except TypeError:
            continue

if __name__ == "__main__":
    main()
 
# count = 5
 
 
# bluetoothSerial.write( str(count).encode('ascii') )
# print(bluetoothSerial.readline())
