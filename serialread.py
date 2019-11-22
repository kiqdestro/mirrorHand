import serial

ser = serial.Serial("/dev/rfcomm0", baudrate=9600, timeout=1)

print("a")
while(1):
	print("Trying read")
	if (ser.in_waiting > 0):
		print(ser.readline())
