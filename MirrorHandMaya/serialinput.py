#Serial read module for MirrorHand software
#Joao Carlos Cardoso - 2019

import serial
import numpy as np

ARDUINO = "COM5"

Sensor = (0, 0)

#Read multiple inputs from serial port


def InitSerial():
    SerialInput = serial.Serial(ARDUINO, 9600)
    # SerialInput = serial.Serial(ARDUINO, 115200)
    return SerialInput

def ReadSerial(SerialInput):
    try:
        SensorNumber = 0
        SensorValue = ""
        SerialInput.reset_input_buffer()
        SerialData = SerialInput.read().decode("utf-8")
        while (SerialData != '>'):
            SerialData = SerialInput.read().decode()
        SensorNumber = int(SerialInput.read())
        if(SerialInput.read().decode("utf-8") == '-'):
            while (SerialData != '<'):
                SerialData = SerialInput.read().decode("utf-8")
                if(SerialData != '<'):
                    SensorValue = SensorValue + SerialData
        Sensor = (SensorNumber, int(SensorValue))
        return Sensor
    except ValueError:
        pass

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