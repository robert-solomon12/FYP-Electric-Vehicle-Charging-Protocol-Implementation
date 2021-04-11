import time
from tkinter import *
from tkinter import ttk

import MotionCtlr as mtc
import USense as us
from ChargingSession import ChargingSession as cs
import threading
root = Tk()
# root.geometry("600x500")

# Battery level counter function

def batteryLvlCounter():
    batteryLvl = 15
    x = 0
    speed = 1
    tariffCounter = 0


    while(x<batteryLvl):
        time.sleep(1)
        batteryLvlChargeBar['value'] += 10
        x+=speed

        # cast string variable as an integer
        percent.set(str(int((x/batteryLvl)*100))+"%")
        finalText.set(str(x)+"/"+str(batteryLvl)+" Charge Completed!")
        root.update_idletasks()

# Include tariff counter function and tariff pay info after charge here ....


def key_input(event):
    mtc.init()
    print('Key pressed: ', event.char)
    key_press = event.char
    sleep_timer = 0.030
       
    if key_press.lower() == 'w':
        print("Accelerating....")
        mtc.accelerate(sleep_timer)
    elif key_press.lower() == 'a':
        print("Steering Left....")
        mtc.leftTurn(sleep_timer)
    elif key_press.lower() == 's':
        print("Reversing....")
        mtc.reverse(sleep_timer)
    elif key_press.lower() == 'd':
        print("Steering Right....")
        mtc.rightTurn(sleep_timer)
    elif key_press.lower() == 'x':
        print("Braking....")
        threading.Thread(target=mtc.brake(sleep_timer).start())
    elif key_press.lower() == 'o':
        print("Activating Obstacle Avoidance....")
        threading.Thread(target=us.activateObstacleAvoidance().start())
    else:
        mtc.brake(sleep_timer)
   #elif key_press.lower() == 'v':
       #cs.ChargingSession.startSequence()
       #batteryLvlCounter()
        
        
def stopMotors():
    mtc.init()
    mtc.stopM()
    
    

percent = StringVar()
finalText = StringVar()

# Progress Bar
batteryLvlChargeBar = ttk.Progressbar(root, orient=HORIZONTAL, length=600, mode='determinate')
batteryLvlChargeBar.pack(pady=20)

# Charge Progress Label
percentLabel = Label(root,textvariable=percent).pack()
statusLabel = Label(root,textvariable=finalText).pack(pady=20)

# before calling the loop below, write function to initiate a TCP Connection and get status .....

charge_Btn = Button(root, text="Start Charge", font="Railway", command=batteryLvlCounter)
charge_Btn.pack(side=BOTTOM,pady=20)


stopMotors_Btn = Button(root, text="Stop Motors", font="Railway", command=stopMotors)
stopMotors_Btn.pack(side=LEFT,pady=20)

my_label = Label(root, text='')
my_label.pack(pady=20)


root.bind('<KeyPress>', key_input)
root.mainloop()
