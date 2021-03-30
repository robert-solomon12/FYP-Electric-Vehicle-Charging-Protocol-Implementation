import time
import RPi.GPIO as GPIO


#infrared line tracking port definition
leftSensor = 29
rightSensor = 31

#sensor state initialisation
lf1=0
rf1=0

#Initialising  GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(leftSensor,GPIO.IN)
GPIO.setup(rightSensor,GPIO.IN)

# Read tracking senbsor data
def read_sensors():
    global lf1, rf1
    lf1 = GPIO.input(leftSensor)
    rf1 = GPIO.input(rightSensor)
    
    
    
def destroy():
    GPIO.cleanup()
   
def main():
    while True:
        read_sensors()
 
 #creating a condition for detecting white lines and black lines
        if(lf1==0):
            print("Left Sensor Detects No Lines!\n")
            time.sleep(0.5)
        if(lf1==1):
            print("Left Sensor Detects Black Lines!\n")
            time.sleep(0.5)
        if(rf1==0):
            print("Right Sensor Detects No Lines!\n")
            time.sleep(0.5)
        if(rf1==1):
            print("Right Sensor Detects Black Lines!\n")
            time.sleep(0.5)
     
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
	#robot car stop
        destroy()
