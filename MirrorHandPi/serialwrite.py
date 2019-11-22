import serial
import time

ser = serial.Serial("COM6", baudrate=115200, timeout = 1, bytesize=8, parity='N', stopbits=1)
ser.close()
ser.open()
print("a")
while(1):
    print("writing")
    ser.write(b'1')
    time.sleep(1)