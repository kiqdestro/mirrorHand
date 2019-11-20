#Serial read module for MirrorHand software
#Joao Carlos Cardoso - 2019

import serial
import numpy as np

ARDUINO = "COM3"

Sensor = [0] * 13

#Read multiple inputs from serial port


def InitSerial():
    #SerialInput = serial.Serial(ARDUINO, 9600)
    SerialInput = serial.Serial(ARDUINO, 115200, timeout=10)
    return SerialInput

def ReadSerial(SerialInput):
    try:
        SensorNumber = 0
        SensorValue = ""
        #SerialInput.reset_input_buffer()
        #SerialInput.write(bytes(1))
        String = SerialInput.readline().decode()
        #print(String)
        i = 0
        while (String[i] != "\n"):
            SensorValue = ""
            CurrentSensor = ""
            if(String[i] == ">"):
                i = i+1
                while(String[i] != "$"):
                    CurrentSensor = CurrentSensor + String[i]
                    i = i+1
                #print(CurrentSensor)
            if(String[i] == "$"):
                i = i+1
                while(String[i] != "<"):
                    SensorValue = SensorValue + String[i]
                    i = i+1
            i = i+1
            Sensor[int(CurrentSensor)] = int(float(SensorValue))
            #print (CurrentSensor, SensorValue, sep = " - ")
        #print(String[i])
        return Sensor
    except ValueError:
        pass        
        """ SerialData = SerialInput.read(1).decode("utf-8")
        print (SerialData)
        while (SerialData != '>'):
            SerialData = SerialInput.read(1).decode()
            print(SerialData)
        SensorNumber = int(SerialInput.read(1))
        print(SerialData)
        if(SerialInput.read(1).decode("utf-8") == '-'):
            while (SerialData != '<'):
                SerialData = SerialInput.read(1).decode("utf-8")
                print(SerialData)
                if(SerialData != '<'):
                    SensorValue = SensorValue + SerialData
        Sensor = (SensorNumber, int(SensorValue))
        print (Sensor)
        return Sensor """


"""def ReadSensors(SerialLine):
    value = 0
    Sensors = [0] * 10"""

"""    try:
        if (SerialLine =)
    except ValueError:
        return Sensors"""


"""    try:                            #Tratamento de excecao e de erro caso a serial receba uma string errada
        index = int(SerialLine[3:4]) #safe cast para int
    except ValueError:
        return Sensors         #Retorna valores antigos
    try:
        if (len(SerialLine) == 8):
            value = int(float(SerialLine[5:8])) 
    except ValueError:
        pass
    try:
        if (len(SerialLine) == 7):
            value = int(float(SerialLine[5:7])) #Se nao der certo para 3 algarismos tenta para 2, senao retorna o valor antigo
    except ValueError:
        return Sensors
    try:
        Sensors[index] = value
    except ValueError:
        return Sensors
    return Sensors"""