#! /usr/bin/python

from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
import serial
import time

bluetoothSerial = serial.Serial( "/dev/rfcomm0", baudrate=9600 )
 
count = 5
 
 
bluetoothSerial.write( str(count) )
print(bluetoothSerial.readline())
