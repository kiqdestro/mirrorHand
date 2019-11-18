import time
import RPi.GPIO as GPIO
import serialinput as si
import numpy as np
import matplotlib.pyplot as plt
from adafruit_servokit import ServoKit

class ServoControl():
	def __init__(self):
        
        # EXAMPLES:
        # kit.servo[0].angle = 180
        # kit.servo[0].actuation_range = 160
        # kit.servo[0].set_pulse_width_range(1000, 2000)

		kit = ServoKit(channels = 16)
		kit.servo[0].set_pulse_width_range(625, 2580)
		kit.servo[1].set_pulse_width_range(500, 2620)
		kit.servo[2].set_pulse_width_range(500, 2620)
		kit.servo[3].set_pulse_width_range(540, 2600)
		kit.servo[4].set_pulse_width_range(540, 2650)
		kit.servo[5].set_pulse_width_range(540, 2650) #A
		kit.servo[6].set_pulse_width_range(520, 2600) #B
		kit.servo[7].set_pulse_width_range(520, 2600) #C *this one is turning only something around 120 degrees
		kit.servo[8].set_pulse_width_range(520, 2600) #D
		kit.servo[9].set_pulse_width_range(520, 2650) #E
		kit.servo[10].set_pulse_width_range(500, 2650) #F

	def setPos(self, servoID, position):
		kit.servo[servoID].angle = (position * 180)

serial = si.InitSerial()
maximum = [0]*10
minimum = [0]*10
values = [0]*10
value = 0
ctrl = ServoControl()

# GPIO.setmode(GPIO.BOARD) # RPi

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
        #print("Sensor", i, Values[i], sep=' - ')                       #Print sensor values
        normalized_value = (1-((value[1]- minimum[value[0]])/(maximum[value[0]]-minimum[value[0]]))) # Normalizing
        if (normalized_value > 1):
            normalized_value = 1
        if (normalized_value < 0):
            normalized_value = 0

        ctrl.setPos(value[0], normalized_value)

if __name__ == "__main__":
    main()