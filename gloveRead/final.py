#! /usr/bin/python

from adafruit_servokit import ServoKit
import serialinput as si
import itsAlive
import serial
import time

kit = ServoKit(channels = 16)

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

bluetoothSerial = serial.Serial("/dev/rfcomm0", baudrate=9600)
maximum = [0]*10
minimum = [0]*10
values = [0]*10
value = 0
ctrl = ServoControl()

def main():
    itsAlive.firstMovement()

    print("Estique os dedos e espere para calibrar")

    time.sleep(5)
    # input("Estique os dedos e pressione espaco para calibrar")

    start_time = time.time()
    elapsed_time = 0

    while(elapsed_time < 2):
    #while(True):
        sensor_max = (bluetoothSerial.readline()).decode("utf-8")[:-2].split(",")
        print(sensor_max)
        #input("Enter to continue")

        try:
            print("sensor_max[0]: " + sensor_max[0])
            print("sensor_max[1]: " + sensor_max[1])
            maximum[int(sensor_max[0])] = int(sensor_max[1])
        except:
            continue

        elapsed_time = time.time() - start_time

    itsAlive.closeHand()

    print("Dobre os dedos e espere para calibrar")

    time.sleep(5)
    
    # input("Dobre os dedos e pressione espaco para calibrar")
    start_time = time.time()
    elapsed_time = 0

    while(elapsed_time < 2):
        sensor_min = (bluetoothSerial.readline()).decode("utf-8")[:-2].split(",")
        print(sensor_min)

        try:
            print("sensor_min[0]: " + sensor_min[0])
            print("sensor_min[1]: " + sensor_min[1])
        except:
            minimum[sensor_min[0]] = sensor_min[1]
            continue

        elapsed_time = time.time() - start_time

    # print(maximum)
    # print(minimum)

    # input("Aperte enter para iniciar")
    print("inicio")

    while(True):

        value = (bluetoothSerial.readline()).decode("utf-8")[:-2].split(",")
        # value = si.ReadSerial(serial)                                   #Loop
        #print("Sensor", i, Values[i], sep=' - ')                       #Print sensor values  
        print(value)
        try:
            normalized_value = (1-((int(value[1])- minimum[int(value[0])])/(maximum[int(value[0])]-minimum[int(value[0])]))) # Normalizing
            if (normalized_value > 1):
                normalized_value = 1
            if (normalized_value < 0):
                normalized_value = 0

            print("hehehe")

            print("[{}, {}]".format(value[0], float(normalized_value)*180))

            ctrl.setPos(int(value[0]), normalized_value)
            
        except (IndexError, ValueError):
            print("erro")
            continue

if __name__ == "__main__":
    main()
 
# count = 5
 
 
# bluetoothSerial.write( str(count).encode('ascii') )
# print(bluetoothSerial.readline())
