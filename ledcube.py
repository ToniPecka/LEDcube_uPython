# LedCube - uPython
# Left, bottom front corner is CS0.
# Front to rear line numbers, Bottom to top layers, Rotated for input.
# pattern("Layer"+"Line_8"+...+"Line_1")
# Layer = 87654321     # Line_X = 87654321

from utime import sleep
from machine import Pin
from random import randrange

# GPIO Definition
serial = Pin(0, Pin.OUT)  # SER Data input                   -GP0--Orange--Serial-
enabler = Pin(1, Pin.OUT)  # OE| LowVolt = allows outputs    -GP1--Gray--Enabler-
store = Pin(4, Pin.OUT)  # RCLK Storage clock show stored    -GP4--Violet--Store-
clock = Pin(5, Pin.OUT)  # SRCLK Shift reg clock             -GP5--Green--Clock-
clear = Pin(6, Pin.OUT)  # SRCLR| Reset LowVolt = clear      -GP6--Brown--Clear-

# Awake The Cube
serial.value(0)
enabler.value(0)
store.value(0)
clock.value(0)
clear.value(1)

# function for turning on LEDs
def show(pattern):
    clear.value(0)
    clear.value(1)
    for i in range(72):
        if pattern[i] == "1":
            serial.value(1)
        if pattern[i] == "0":
            serial.value(0)

        clock.value(1)
        clock.value(0)
        serial.value(0)
        
    store.value(1)
    store.value(0)


# function for darkness
def dimmer(pause_dark):
    enabler.value(1)
    sleep(pause_dark)
    enabler.value(0)