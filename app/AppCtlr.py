import time
from tkinter import *
from tkinter import ttk
#from Socket import Socket as skt
import MotionCtlr as mtc
from ChargingSession import ChargingSession as cs
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
       mtc.accelerate(sleep_timer)
    elif key_press.lower() == 'a':
       mtc.leftTurn(sleep_timer)
    elif key_press.lower() == 's':
       mtc.reverse(sleep_timer)
    elif key_press.lower() == 'd':
       mtc.rightTurn(sleep_timer)
    elif key_press.lower() == 'q':
       mtc.leftPivot(sleep_timer)
    elif key_press.lower() == 'e':
       mtc.rightPivot(sleep_timer)
    elif key_press.lower() == 'x':
       mtc.brake(sleep_timer)
    else:
       pass
   #elif key_press.lower() == 'v':
       #cs.ChargingSession.startSequence()
       #batteryLvlCounter()


percent = StringVar()
finalText = StringVar()


# Progress Bar
batteryLvlChargeBar = ttk.Progressbar(root, orient=HORIZONTAL, length=600, mode='determinate')
batteryLvlChargeBar.pack(pady=20)

# Charge Progress Label
percentLabel = Label(root,textvariable=percent).pack()
statusLabel = Label(root,textvariable=finalText).pack(pady=20)

# Accelerate Button
acc_Btn = Button(root, text="Accelerate", font="Railway", command=mtc.accelerate)
acc_Btn.pack(pady=20)


# Reverse Button
rev_Btn = Button(root, text="Reverse", font="Railway", command=mtc.reverse)
rev_Btn.pack(side=BOTTOM, pady=20)


# Steer Right Button
right_Btn = Button(root, text="Steer Right", font="Railway", command=mtc.rightTurn)
right_Btn.pack(side=RIGHT,pady=20)


# Steer Left Button
left_Btn = Button(root, text="Steer Left", font="Railway", command=mtc.leftTurn)
left_Btn.pack(side=LEFT,pady=20)


# Brake Button
brake_Btn = Button(root, text="Brake", font="Railway", command=mtc.brake)
brake_Btn.pack(side=LEFT,pady=20)


# Start Charge Btn

# before calling the loop below, write function to initiate a TCP Connection and get status .....

charge_Btn = Button(root, text="Start Charge", font="Railway", command=batteryLvlCounter)
charge_Btn.pack(side=BOTTOM,pady=20)


root.bind('<KeyPress>', key_input)
root.mainloop()
