from adafruit_servokit import ServoKit
import time

# kit.servo[0].angle = 180
# kit.servo[0].actuation_range = 160
# kit.servo[0].set_pulse_width_range(1000, 2000)

kit = ServoKit(channels = 16)

for i in range(0, 10000):
	for j in range (0, 11):
		if(i%2 == 0):
			kit.servo[j].angle = 180
		else:
			kit.servo[j].angle = 0

	time.sleep(0.5)

