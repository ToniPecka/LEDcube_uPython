# Rain mode

import display
import point
import ledcube
from random import randrange
from time import sleep

# rain time period
# rain_time = 0.03
# rain_gap = 0.03

#lists of drops
drops = []

def rain():
    for drop in drops:
        if drop.z == 0:
            drops.remove(drop)
            drop.delete()
        ledcube.show(str(drop))
        # sleep(rain_gap)
        drop.rain()

def new_drops():
    # vytvoření 4 kapek ve 4 různých kvadrantech
    drops.append(point.Point(randrange(1,9), randrange(1,9), 8))
    '''
    drops.append(point.Point(randrange(4,9), randrange(1,4), 8))
    drops.append(point.Point(randrange(1,4), randrange(4,9), 8))
    drops.append(point.Point(randrange(4,9), randrange(4,9), 8))
    '''
    
def run():
    #počáteční 4 kapky
    new_drops()

    while (1):
        # Button A
        if display.keyA.value() == 0:
            display.LCD.fill_rect(208, 15, 30, 30, display.LCD.red)
            sleep(0.25)
            break #vyskočení z modu
        else:
            display.LCD.fill_rect(208, 15, 30, 30, display.LCD.white)
            display.LCD.rect(208, 15, 30, 30, display.LCD.red)   
        display.LCD.show()

        # vykresleni kapek na LED kostce
        rain()

        # tvorba dalších kapek
        new_drops()
        
        # sleep(rain_time)

    return 1
