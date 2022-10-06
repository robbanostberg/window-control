import time
from pynput.keyboard import Key, Controller
from pywinauto import Desktop


"""-------- static variables --------"""
debug = True  # set to True to get printouts and deactivate the F11 presses
wait = 1  # seconds
startup = 1  # seconds
interval = 10  # seconds
windows2skip = 4  # amount of detected windows that aren't actual windows 


"""-------- helper functions --------"""
def pressKey(controller, key):
    controller.press(key)
    time.sleep(wait)

def tapKey(controller, key):
    controller.tap(key)
    time.sleep(wait)

def releaseKey(controller, key):
    controller.release(key)
    time.sleep(wait)

def startDelay():
    for i in range(0, startup, interval):
        print(startup - interval * i)
        time.sleep(interval)


"""-------- to be executed --------"""
if not debug:
    startDelay()  # delayes execution of script for 3 minutes (to be evaluated)

windows = Desktop(backend="uia").windows()  # creates a list of windows (and 4 other things)
if debug:
    for w in windows:
        print(w.window_text())  # prints name of every window if debug is True
    print(len(windows),'\n')  # prints the size of the list of windows if debug is True

k = Controller()  # creates a controller instance to send key strokes

for e in range(len(windows)-windows2skip):  # does *see below* for size of windows list - 4 
    if not debug:
        tapKey(k, Key.f11)  # taps the F11 key twice with 0.5 s between, if debug is False
        tapKey(k, Key.f11)
    pressKey(k, Key.alt)  # holds the ALT key down
    for i in range(e):  # presses the TAB key an increasing amount of times to iterate through each window
        tapKey(k, Key.tab)
    releaseKey(k, Key.alt)  # releases the ALT key
