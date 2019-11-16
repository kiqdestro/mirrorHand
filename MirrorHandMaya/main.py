# Arquivo principal software MirrorHand + Maya
# Necessário - Arduino, Autodesk Maya
# Joao Carlos Cardoso - 2019

# import maya as Maya
import time
import serialinput as SerialInput
import numpy as np 
import matplotlib.pyplot as plt
#from scipy import signal

Serial = SerialInput.InitSerial()
Max = [0]*10
Min = [0]*10
Values = [0]*10
Value = 0

def main():
    #ResetJoints()
        
    #Values = SerialInput.ReadSensors(SerialData)    #Get sensor list from serial
    #for i in range(len(Values)):
    input("Estique os dedos e pressione espaco para calibrar")
    ElapsedTime = 0
    StartTime = time.time()
    while(ElapsedTime < 1):
        SensorMax = SerialInput.ReadSerial(Serial)
        Max[SensorMax[0]] = SensorMax[1]
        ElapsedTime = time.time() - StartTime
        
    input("Dobre os dedos e pressione espaco para calibrar")
    ElapsedTime = 0
    StartTime = time.time()
    while(ElapsedTime < 1):
        SensorMin = SerialInput.ReadSerial(Serial)
        Min[SensorMin[0]] = SensorMin[1]
        ElapsedTime = time.time() - StartTime

    print(Max)
    print(Min)

    input("Aperte enter para iniciar")

    while(1): #MainLoop
        Value = SerialInput.ReadSerial(Serial)                                   #Loop
        #print("Sensor", i, Values[i], sep=' - ')                        #Print sensor values
        NormalizedValue = (1-((Value[1]- Min[Value[0]])/(Max[Value[0]]-Min[Value[0]]))) #Convert Input to a rotation value between 0 and 90 deg
        if (NormalizedValue > 1):
            NormalizedValue = 1
        if (NormalizedValue < 0):
            NormalizedValue = 0
        print(Value[1], Min[Value[0]], Max[Value[0]], Min[Value[0]], sep=' - ')                               
        CommandString = "setAttr(\"joint" + str(Value[0]+1) + ".rotateZ\"," + str(NormalizedValue*90) + ");"     #Build MEL CommandString
        print(CommandString)
        # Maya.SendCommand(CommandString)                                 #Send MEL Commando to MAYA
        #time.sleep(.1)                                                     #Delay

if __name__=="__main__":
    main()