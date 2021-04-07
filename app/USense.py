# Robert Solomon
# College: Waterford Institute of Technology
# Final Year (Year 4)

import RPi.GPIO as GPIO
import time
import random
import MotionCtlr as mtc
import sys

def distance(measure='cm'):
    try:
        
        TRIG=12
        ECHO=16
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        #print("distance measurement in progress")
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.output(TRIG,False)
       # print("waiting for Sensor to settle...")
        time.sleep(0.2)
        GPIO.output(TRIG,True)
        time.sleep(0.00001)
        GPIO.output(TRIG,False)
        
        while GPIO.input(ECHO)==0: #waiting until Echo pin is Low
            pulse_start=time.time()
        while GPIO.input(ECHO)==1: #waiting until Echo pin is High
            
            pulse_end=time.time() # keeping a record of the last time the Echo Pin was high (seconds)
            pulse_duration=pulse_end-pulse_start
            distance=pulse_duration*17150
        
        distance=round(distance,2) # rounding the distance to 2 decimal places
        
        GPIO.cleanup()
        return distance
    except:
        distance = 100 # going to be used as a reference for when we're checking for distance equal to 100 to do something
        GPIO.cleanup()
        return distance
        
        
    # function to check the front when an object is visible
def checkFrontView():
    mtc.init()
    dis = distance()
    
    if dis < 15: # setting the distance limit to 15 cm 
        print('Detecting an object... too close! Current Distance: ', dis, 'cm')
        mtc.init()
        mtc.reverse(2)
        dis = distance()
        if dis < 15:
            print('Detecting an object... too close! Current Distance: ', dis, 'cm')
            mtc.init()
            mtc.rightTurn(3)
            mtc.init()
            mtc.reverse(2)
            dis = distance()
            if dis < 15:
                print('Repeat! Detecting an object... too close...coming to a halt! Current Distance: ', dis, 'cm')
                sys.exit()
        
        # main function routine to start the process of detection
def initiateOA():
    tf = 0.030  # setting the timer to 30 milliseconds
    i = random.randrange(0,4)
    
    if i == 0:
        
        for j in range(30):
            checkFrontView()
            mtc.init()
            mtc.accelerate(tf)
    elif i ==1:
        for j in range(30):
            checkFrontView()
            mtc.init()
            mtc.leftTurn(tf)
    elif i ==2:
        for j in range(30):
            checkFrontView()
            mtc.init()
            mtc.rightTurn(tf)
    elif i ==3:
        for j in range(30):
            checkFrontView()
            mtc.init()
            mtc.rightTurn(tf)

def activateObstacleAvoidance():
    for z in range(10):
        initiateOA()
            
activateObstacleAvoidance()     