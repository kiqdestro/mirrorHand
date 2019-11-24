#! /usr/bin/python

from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
import serial
import time

bluetoothSerial = serial.Serial( "/dev/rfcomm0", baudrate=9600 )
 
<<<<<<< HEAD
bluetoothSerial.write('5'.toBytes())
print(bluetoothSerial.readline())
=======
count = None
while count == None:
    try:
        count = input( "Please enter the number of times to blink the LED: ")
    except:
        pass    # Ignore any errors that may occur and try again
 
 
bluetoothSerial.write( str(count) )
print(bluetoothSerial.readline())
>>>>>>> 737fb1c8a9022f07506d3bc8a541ee71600d18ff
