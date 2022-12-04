# Rain mode

import display
import point
import ledcube
from random import randrange
from utime import sleep

# Pauses for sleep function
light = 0.012
# dark = 0.04

# empty list of drops
drops = []
iterable_drops = drops

def rain():
    # goes through a list of drops shows them and drops them
    for drop in iterable_drops:
        if drop.z == 1:
            drops.remove(drop)
        ledcube.show(str(drop))
        sleep(light)
#         ledcube.dimmer(dark)
        drop.rain() # Moves drop down
# ledcube.show(str(drop), light)

def new_drop():
    # Creates a new random drop
    drops.append(point.Point(randrange(1,9), randrange(1,9), 8))
    
def run():
    new_drop() # Creates a first drop
    count = 1
    iterable_drops = drops

  
    while (1):
        # Button A Mode change
        if display.keyA.value() == 0:
            display.LCD.fill_rect(208, 15, 30, 30, display.LCD.red)
            sleep(0.25)
            break # stops this mode and moves to another
        else:
            display.LCD.fill_rect(208, 15, 30, 30, display.LCD.white)
            display.LCD.rect(208, 15, 30, 30, display.LCD.red)   
        display.LCD.show()

        # Displays drops on LEDcube
        rain()
        count += 1
        
        # Creates a next drop every 6th layer
        if count == 9:
            new_drop()      
            count = 1
            iterable_drops = drops
        
    return 1

# For testing display control
if __name__ == '__main__':
    run()