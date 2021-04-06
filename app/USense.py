import RPi.GPIO as GPIO


def distance(measure='cm'):
    
    TRIG=12
    ECHO=16
    GPIO.setmode(GPIO.BOARD)
    print("distance measurement in progress")
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG,False)
    print("waiting for Sensor to settle...")
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

print(distance('cm'))
        