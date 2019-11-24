#! /usr/bin/python

from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
import serial
import time

bluetoothSerial = serial.Serial( "/dev/rfcomm0", baudrate=9600 )
 
count = None
while count == None:
    try:
        count = input( "Please enter the number of times to blink the LED: ")
    except:
        pass    # Ignore any errors that may occur and try again
 
 
bluetoothSerial.write( str(count) )
print(bluetoothSerial.readline())
