import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 
AN1 = 2
AN2 = 3
DIG2 = 23
DIG1 = 18
GPIO.setup(AN2, GPIO.OUT)
GPIO.setup(AN1, GPIO.OUT)
GPIO.setup(DIG2, GPIO.OUT)
GPIO.setup(DIG1, GPIO.OUT)
GPIO.setup(5, GPIO.IN)    #Sensor O1
GPIO.setup(6, GPIO.IN)     #Sensor O2
GPIO.setup(16, GPIO.IN)     #Sensor O3
sleep(1)
p1 = GPIO.PWM(AN1, 60)
p2 = GPIO.PWM(AN2, 60)

#on = black, off = white

try:
  while True:
    s1=GPIO.input(5)
    s2=GPIO.input(6)
    s3=GPIO.input(16)
    def forward():
      GPIO.output(DIG1, GPIO.HIGH)
      GPIO.output(DIG2, GPIO.HIGH)
# # #000
# #     if (s1==0)and(s2==0)and(s3==0):
# #       print("No Lines Detected...")
# #       forward()
# #       p1.start(20)
# #       p2.start(0)
# #       sleep(0.5)
#100
    if (s1==1)and(s2==0)and(s3==0):
      print("Left Sensor Detected Black Lines")
      forward()
      p1.start(20)
      p2.start(5)
      sleep(0.5)
#010
    elif (s1==0)and(s2==1)and(s3==0):
      print("Middle Sensor Detected Black Lines")
      forward()
      p1.start(20)

#001
    elif (s1==0)and(s2==0)and(s3==1):
      print("Right Sensor Detected Black Lines")
      forward()
      p1.start(20)
      p2.start(20)
      sleep(0.5)
    else:
      print("stop")
      GPIO.output(AN1, GPIO.LOW)
      GPIO.output(AN2, GPIO.LOW)
except:
  p1.start(0)
  p2.start(0)