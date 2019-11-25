#! /usr/bin/python

from adafruit_servokit import ServoKit
import serial
import final
import time

ctrl = final.servoControl()

def firstMovement():
    for i in range(11):
        ctrl.setPos(i, 1)
    
    for i in range(11):
        ctrl.setPos(i, 0)
        time.sleep(500)
    
    for i in range(11):
        ctrl.setPos(i, 1)

def closeHand():
    for i in range(11):
        ctrl.setPos(i, 0)