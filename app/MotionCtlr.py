import RPi.GPIO as gpio

import time

#class MotionCtlr:
       
    
def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)


def accelerate():
    init()
    print("Accelerating!")
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(1)
    gpio.cleanup()

#acceleration test
#accelerate(3)      

def reverse():
    init()
    print("Reversing!")
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(1)
    gpio.cleanup()

#reverse testing
#reverse(3)

def rightTurn():
    init()
    print("Right Turn!")
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, False)
    time.sleep(1)

    gpio.cleanup()

# right turn test
#rightTurn(2)

def leftTurn():
    init()
    print("Left Turn!")
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(1)
    gpio.cleanup()

#left turning test
#leftTurn(2)


def pivotRight():
    init()
    print("Right Turn!")
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(1)

    gpio.cleanup()

#pivotting right test
#pivotRight(2)
    
def pivotLeft():
    init()
    print("Right Turn!")
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(1)
    gpio.cleanup()

#pivotting left test
#pivotLeft(2)
   
