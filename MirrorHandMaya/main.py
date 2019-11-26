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
    while(ElapsedTime < 1):
        Values = SerialInput.ReadSerial(Serial)
        #print(ElapsedTime)
        try:
            Max = Values[:]
        except:
            pass
        ElapsedTime = time.time() - StartTime
        

    input("Dobre os dedos e pressione espaco para calibrar")
    ElapsedTime = 0
    StartTime = time.time()
    while(ElapsedTime < 1):
        Values = SerialInput.ReadSerial(Serial)
        try:
            Min = Values[:]
        except:
            pass
        ElapsedTime = time.time() - StartTime

    print(Max)
    print(Min)

    Maya.OpenConnection

    input("Aperte enter para iniciar")

    while(1): #MainLoop
        
        Values = SerialInput.ReadSerial(Serial)                                   #Loop
        print (Values)
        for i in range (8):
            try:
                print(Values[i], Min[i], Max[i], Min[i], sep=' - ')
                if(Max[i] - Min[i] != 0):
                    NormalizedValue = (1-((Values[i]- Min[i])/(Max[i]-Min[i]))) #Convert Input to a rotation value between 0 and 90 deg
                    if (NormalizedValue > 1):
                        NormalizedValue = 1
                    if (NormalizedValue < 0):
                        NormalizedValue = 0    
                else: NormalizedValue = 0                
                CommandString = "setAttr(\"joint" + str(i+1) + ".rotateZ\"," + str(NormalizedValue*90) + ");"     #Build MEL CommandString
                Maya.SendCommand(CommandString)                                 #Send MEL Commando to MAYA
            except TypeError:
                print("Joints error")
                pass
        try:
            CommandString = "setAttr(\"b.rotateX\"," + str(Values[10]*-1) + ");"     #Build MEL CommandString
            Maya.SendCommand(CommandString)                                 #Send MEL Commando to MAYA
            CommandString = "setAttr(\"b.rotateY\"," + str(Values[11]*-1) + ");"     #Build MEL CommandString
            Maya.SendCommand(CommandString)                                 #Send MEL Commando to MAYA
            CommandString = "setAttr(\"b.rotateZ\"," + str(Values[12]) + ");"     #Build MEL CommandString
            Maya.SendCommand(CommandString)                                 #Send MEL Commando to MAYA
        except TypeError:
            pass
#>>>>>>> IMU

if __name__=="__main__":
    main()