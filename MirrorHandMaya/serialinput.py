#Serial read module for MirrorHand software
#Joao Carlos Cardoso - 2019

import serial
import numpy as np

ARDUINO = "COM3"

#Read multiple inputs from serial port


def InitSerial():
    SerialInput = serial.Serial(ARDUINO, 115200)
    return SerialInput

def ReadSerial(SerialInput):
    #PreviousValue = None
    # Read the serial value
    #SerialInput.flushInput()
    try:
        return SerialInput.readline().strip()
    except ValueError:
        pass
    # Catch any bad serial data:
    #try:
        #if SerialValue != PreviousValue:
            # Print the value if it differs from the prevVal:
        #    print(SerialValue)
            #maya.send(serialValue)
        #    PreviousValue = SerialValue
    #except ValueError:
        #pass

SensorValues = [0] * 10

def ReadSensors(SerialLine):
    try:                            #Tratamento de excecao e de erro caso a serial receba uma string errada
        index = int(SerialLine[3:4]) #safe cast para int
    except ValueError:
        return SensorValues         #Retorna valores antigos
    try:
        if (len(SerialLine) == 8):
            value = int(float(SerialLine[5:8])) 
    except ValueError:
        pass
    try:
        if (len(SerialLine) == 7):
            value = int(float(SerialLine[5:7])) #Se nao der certo para 3 algarismos tenta para 2, senao retorna o valor antigo
    except ValueError:
        return SensorValues
    print (SerialLine)
    SensorValues[index] = value
    return SensorValues