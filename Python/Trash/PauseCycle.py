import time, threading
from Tkinter import *

paused = False
root = Tk()
#root.withdraw()

def printer():
    global paused
    while True:
        if paused == False:
            print 'Tesssst!!!'
        time.sleep(1)

def keyWaiter(event):
    global paused
    if event.char == ' ':
        if paused == False:
            paused = True
            print 'PAUSED'
        elif paused == True:
            paused = False
            print 'UNPAUSED'
    else:
        pass

def mainThread():
    root.bind('<Key>', keyWaiter)
    root.mainloop()
    
t1 = threading.Thread(target=printer)
t2 = threading.Thread(target=mainThread)

t1.start()
t2.start()