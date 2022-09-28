# Rain mode

import display
import point
import ledcube
from random import randrange

# empty list of drops
drops = []

def rain():
    # goes through a list of drops shows them and drops them
    for drop in drops:
        if drop.z == 0:
            drops.remove(drop)
        ledcube.show(str(drop))
        drop.rain() # Moves drop down

def new_drop():
    # Creates a new random drop
    drops.append(point.Point(randrange(1,9), randrange(1,9), 8))
    
def run():
    new_drop() # Creates a first drop
    count = 1
  
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
        if count == 4:
            new_drop()      
            count = 1
        
    return 1

# For testing display control
if __name__ == '__main__':
    run()
