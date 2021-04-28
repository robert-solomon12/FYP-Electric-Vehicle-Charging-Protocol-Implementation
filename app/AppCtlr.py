import time
from tkinter import *
from tkinter import ttk

import socket
import ChargingSession as cs

import MotionCtlr as mtc
import USense as us

import threading
from threading import Thread


root = Tk()
root.geometry("600x500")
root.title("Vehicle Dashboard") # Window Title
root.configure(bg='grey')



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
        
    
def chargeThread():
    Thread(target = batteryLvlCounter).start()
    Thread(target = cs.startSequence).start()


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
        us.activateObstacleAvoidance()
    else:
        mtc.brake(sleep_timer)



percent = StringVar()
finalText = StringVar()

# Progress Bar
batteryLvlChargeBar = ttk.Progressbar(root, orient=HORIZONTAL, length=600, mode='determinate')
batteryLvlChargeBar.pack(pady=20)

# Charge Progress Label
percentLabel = Label(root,textvariable=percent).pack()
statusLabel = Label(root,textvariable=finalText).pack(pady=20)



# before calling the loop below, write function to initiate a TCP Connection and get status .....

charge_Btn = Button(root, text="Start Charge", font="Railway", command=chargeThread)
charge_Btn.pack(side=BOTTOM,pady=20)
charge_Btn.configure(bg='#BD4D35')


keyBoard_Hint_label = Label(root, text='Please use Keyboard keys to control Vehicle options!')
keyBoard_Hint_label.pack(pady=10)
keyBoard_Hint_label.configure(bg='grey')


keyBoard_W_Key_label = Label(root, text=' "W" Key = Accelerate')
keyBoard_W_Key_label.pack(pady=10)
keyBoard_W_Key_label.configure(bg='grey')


keyBoard_A_Key_label = Label(root, text=' "A" Key = Steer Left')
keyBoard_A_Key_label.pack(pady=10)
keyBoard_A_Key_label.configure(bg='grey')


keyBoard_S_Key_label = Label(root, text=' "S" Key = Reverse')
keyBoard_S_Key_label.pack(pady=10)
keyBoard_S_Key_label.configure(bg='grey')


keyBoard_D_Key_label = Label(root, text=' "D" Key = Steer Right')
keyBoard_D_Key_label.pack(pady=10)
keyBoard_D_Key_label.configure(bg='grey')


keyBoard_X_Key_label = Label(root, text=' "X" Key = Brake')
keyBoard_X_Key_label.pack(pady=10)
keyBoard_X_Key_label.configure(bg='grey')


keyBoard_O_Key_label = Label(root, text=' "O" Key = Activate Obstacle Avoidance')
keyBoard_O_Key_label.pack(pady=10)
keyBoard_O_Key_label.configure(bg='grey')

root.bind('<KeyPress>', key_input)
root.mainloop()




