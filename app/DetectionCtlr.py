# Robert Solomon
# College: Waterford Institute of Technology
# Final Year (Year 4)
# Email: robertsolomon12@outlook.com

import RPi.GPIO as gpio

# initializing motors and sensors
def init():
    # turning off warning messages
    gpio.setwarnings(False)
    gpio.setmode(gpio.BOARD)
    
    # initializing motors
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    
    # initializing sensors
    gpio.setup(29,gpio.IN) # left sensor
    gpio.setup(31,gpio.IN) # right sensor
    
    
# turn on front left and rear left motors
def leftMotorPairsOn():
    gpio.output(7,1)
    gpio.output(13,1)

# turn off front left and rear left motors
def leftMotorPairsOff():
    gpio.output(7,0)
    gpio.output(13,0)
    
    
# turn on right front right and rear right motors
def rightMotorPairsOn():
    gpio.output(11,1)
    gpio.output(15,1)


#turn off right front right and rear right motors
def rightMotorPairsOff():
     gpio.output(11,0)
     gpio.output(15,0)


# turn off all motors
def stopAllMotors():
    gpio.output(7,0)
    gpio.output(11,0)
    gpio.output(13,0)
    gpio.output(15,0)
    
# function initially called immidiately to stop all motors 
stopAllMotors()
