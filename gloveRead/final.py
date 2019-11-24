#! /usr/bin/python

from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
import serial
import time

bluetoothSerial = serial.Serial( "/dev/rfcomm0", baudrate=9600 )
 
bluetoothSerial.write('5'.toBytes())
print(bluetoothSerial.readline())
