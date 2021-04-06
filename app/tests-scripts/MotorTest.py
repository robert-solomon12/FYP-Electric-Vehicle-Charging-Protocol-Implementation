import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

# setting the output pins
gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)

gpio.output(7, False) #Motor 1
gpio.output(11, False) #Motor 2
gpio.output(13, True) #Motor 3
gpio.output(15, False) #Motor 4
time.sleep(0.5)

gpio.cleanup()
