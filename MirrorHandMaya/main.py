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
Max = [0]*13
Min = [0]*13
Values = [0]*13
Value = 0

def main():
    #ResetJoints()
        
    #Values = SerialInput.ReadSensors(SerialData)    #Get sensor list from serial
    #for i in range(len(Values)):
    input("Estique os dedos e pressione espaco para calibrar")
    ElapsedTime = 0
    StartTime = time.time()
    Values = SerialInput.ReadSerial(Serial)
    for i in range (len(Values)):
        Values = SerialInput.ReadSerial(Serial)
        Max[i] = Values[i]
        ElapsedTime = time.time() - StartTime
        
    input("Dobre os dedos e pressione espaco para calibrar")
    ElapsedTime = 0
    StartTime = time.time()
    for i in range (len(Values)):
        Values = SerialInput.ReadSerial(Serial)
        Min[i] = Values[i]
        ElapsedTime = time.time() - StartTime

    print(Max)
    print(Min)

    input("Aperte enter para iniciar")

    while(1): #MainLoop
# <<<<<<< HEAD
#         Value = SerialInput.ReadSerial(Serial)                                   #Loop
#         #print("Sensor", i, Values[i], sep=' - ')                        #Print sensor values
#         NormalizedValue = (1-((Value[1]- Min[Value[0]])/(Max[Value[0]]-Min[Value[0]]))) #Convert Input to a rotation value between 0 and 90 deg
#         if (NormalizedValue > 1):
#             NormalizedValue = 1
#         if (NormalizedValue < 0):
#             NormalizedValue = 0
#         print(Value[1], Min[Value[0]], Max[Value[0]], Min[Value[0]], sep=' - ')                               
#         CommandString = "setAttr(\"joint" + str(Value[0]+1) + ".rotateZ\"," + str(NormalizedValue*90) + ");"     #Build MEL CommandString
#         print(CommandString)
#         Maya.SendCommand(CommandString)                                 #Send MEL Commando to MAYA
#         #time.sleep(.1)                                                     #Delay
# =======
        
        Values = SerialInput.ReadSerial(Serial)                                   #Loop
        print (Values)
        for i in range (8):
            print(Values[i], Min[i], Max[i], Min[i], sep=' - ')
            if(Max[i] - Min[i] != 0):
                NormalizedValue = (1-((Values[i]- Min[i])/(Max[i]-Min[i]))) #Convert Input to a rotation value between 0 and 90 deg
                if (NormalizedValue > 1):
                    NormalizedValue = 1
                if (NormalizedValue < 0):
                    NormalizedValue = 0    
            else: NormalizedValue = 0                
            CommandString = "setAttr(\"joint" + str(i+1) + ".rotateZ\"," + str(NormalizedValue*90) + ");"     #Build MEL CommandString
            #Maya.SendCommand(CommandString)                                 #Send MEL Commando to MAYA

        CommandString = "setAttr(\"b.rotateX\"," + str(Values[10]*-1) + ");"     #Build MEL CommandString
        Maya.SendCommand(CommandString)                                 #Send MEL Commando to MAYA
        CommandString = "setAttr(\"b.rotateY\"," + str(Values[11]*-1) + ");"     #Build MEL CommandString
        Maya.SendCommand(CommandString)                                 #Send MEL Commando to MAYA
        CommandString = "setAttr(\"b.rotateZ\"," + str(Values[12]) + ");"     #Build MEL CommandString
        Maya.SendCommand(CommandString)                                 #Send MEL Commando to MAYA
                

        """ if Value is not None:
            #print("Sensor", i, Values[i], sep=' - ')                        #Print sensor values
            if(Value[0] <= 9):
                NormalizedValue = (1-((Value[1]- Min[Value[0]])/(Max[Value[0]]-Min[Value[0]]))) #Convert Input to a rotation value between 0 and 90 deg
                if (NormalizedValue > 1):
                    NormalizedValue = 1
                if (NormalizedValue < 0):
                    NormalizedValue = 0
                print(Value[1], Min[Value[0]], Max[Value[0]], Min[Value[0]], sep=' - ')                               
                CommandString = "setAttr(\"joint" + str(Value[0]+1) + ".rotateZ\"," + str(NormalizedValue*90) + ");"     #Build MEL CommandString
                print(CommandString)
            else:
                if(Value[0] == 10):
                    CommandString = "setAttr(\"joint" + str(0) + ".rotateX\"," + str(Value[1]) + ");"     #Build MEL CommandString
                if(Value[0] == 11):
                    CommandString = "setAttr(\"joint" + str(0) + ".rotateY\"," + str(Value[1]) + ");"     #Build MEL CommandString
                if(Value[0] == 12):
                    CommandString = "setAttr(\"joint" + str(0) + ".rotateZ\"," + str(Value[1]) + ");"     #Build MEL CommandString
            # Maya.SendCommand(CommandString)                                 #Send MEL Commando to MAYA
            #time.sleep(.1)                                                     #Delay """
#>>>>>>> IMU

if __name__=="__main__":
    main()