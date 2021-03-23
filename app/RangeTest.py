import RPi.GPIO as gpio
import time


def distance(measure='cm'):
    gpio.setmode(gpio.BOARD)
    gpio.setup(12, gpio.OUT)
    gpio.setup(16, gpio.IN)
    
    gpio.output(12, False)
    while gpio.input(16) == 0:
        nosignal = time.time()
        
    while gpio.input(16) == 1:
        sig = time.time()
        
    t1 = sig - nosig
    
    
    if measure == 'cm':
        distance = t1 / 0.000058 # returns distance in centimetres
        
    elif measure == 'inch':
        distance = t1 / 0.000148 # returns distance in inches
    else:
        print('not a valid choice of measurement: inch or cm')
        distance = None
        
    gpio.cleanup()
    return distance

print(distance('cm'))
        