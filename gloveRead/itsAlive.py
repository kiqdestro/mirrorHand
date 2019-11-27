#! /usr/bin/python

from adafruit_servokit import ServoKit
import serial
import final
import time

ctrl = final.ServoControl()

def firstMovement():
    for i in range(11):
        ctrl.setPos(i, 1)
    
    for i in range(11):
        time.sleep(0.5)
        ctrl.setPos(i, 0)
    
    time.sleep(0.1)
    
    for i in range(11):
        ctrl.setPos(i, 1)

def closeHand():
    for i in range(11):
        ctrl.setPos(i, 0)
