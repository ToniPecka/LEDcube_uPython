# inicializace kostky

import ledcube
import display
from time import sleep

# Basic Pattern
# pattern=("11111111"+"11111111"+"11111111"+"11111111"+"11111111"+"11111111"+"11111111"+"11111111"+"11111111")
pattern=("00011000"+"00000000"+"00000000"+"00000000"+"00011000"+"00011000"+"00000000"+"00000000"+"00000000")

def run():
    while True:
        ledcube.show(pattern)
        
        if display.keyA.value() == 0:
            # When pushed switches the mode
            display.LCD.fill_rect(208, 15, 30, 30, display.LCD.red)
            display.LCD.show()
            sleep(0.5)
            break
        
        else:
            display.LCD.fill_rect(208, 15, 30, 30, display.LCD.white)
            display.LCD.rect(208, 15, 30, 30, display.LCD.red)
            display.LCD.show()
    return 1