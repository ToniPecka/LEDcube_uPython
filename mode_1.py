# Creates a Drop which you can move freely in the cube
import display
import point
import ledcube
from time import sleep

# Creates Object called drop
kapka = point.Point()
# Time gap to easy button control
button_pause = 0.25

def run():
    while (1):
        ledcube.show(str(kapka))

        # Button A breaks to next mode
        if display.keyA.value() == 0:
            display.LCD.fill_rect(208, 15, 30, 30, display.LCD.red)
            sleep(button_pause)
            break 
        else:
            display.LCD.fill_rect(208, 15, 30, 30, display.LCD.white)
            display.LCD.rect(208, 15, 30, 30, display.LCD.red)

        # Button B
        if (display.keyB.value() == 0):
            display.LCD.fill_rect(208, 75, 30, 30, display.LCD.red)
            sleep(button_pause)
        else:
            display.LCD.fill_rect(208, 75, 30, 30, display.LCD.white)
            display.LCD.rect(208, 75, 30, 30, display.LCD.red)

        # Button X Moves up
        if (display.keyX.value() == 0):
            display.LCD.fill_rect(208, 135, 30, 30, display.LCD.red)
            sleep(button_pause)
            kapka.move(0, 0, 1)
        else:
            display.LCD.fill_rect(208, 135, 30, 30, display.LCD.white)
            display.LCD.rect(208, 135, 30, 30, display.LCD.red)

        # Button Y Moves Down
        if (display.keyY.value() == 0):
            display.LCD.fill_rect(208, 195, 30, 30, display.LCD.red)
            sleep(button_pause)
            kapka.move(0, 0, -1)
        else:
            display.LCD.fill_rect(208, 195, 30, 30, display.LCD.white)
            display.LCD.rect(208, 195, 30, 30, display.LCD.red)

        # Button UP Moves Back
        if (display.up.value() == 0):
            display.LCD.fill_rect(60, 60, 30, 30, display.LCD.red)
            sleep(button_pause)
            kapka.move(0, 1, 0)
        else:
            display.LCD.fill_rect(60, 60, 30, 30, display.LCD.white)
            display.LCD.rect(60, 60, 30, 30, display.LCD.red)

        # Button Down Moves Front
        if (display.dowm.value() == 0):
            display.LCD.fill_rect(60, 150, 30, 30, display.LCD.red)
            sleep(button_pause)
            kapka.move(0, -1, 0)
        else:
            display.LCD.fill_rect(60, 150, 30, 30, display.LCD.white)
            display.LCD.rect(60, 150, 30, 30, display.LCD.red)

        # Button Left Moves to Left
        if (display.left.value() == 0):
            display.LCD.fill_rect(15, 105, 30, 30, display.LCD.red)
            sleep(button_pause)
            kapka.move(-1, 0, 0)
        else:
            display.LCD.fill_rect(15, 105, 30, 30, display.LCD.white)
            display.LCD.rect(15, 105, 30, 30, display.LCD.red)

        # Button Right Moves to Right
        if (display.right.value() == 0):
            display.LCD.fill_rect(105, 105, 30, 30, display.LCD.red)
            sleep(button_pause)
            kapka.move(1, 0, 0)
        else:
            display.LCD.fill_rect(105, 105, 30, 30, display.LCD.white)
            display.LCD.rect(105, 105, 30, 30, display.LCD.red)

        # Button CTRL Jumps to random position
        if (display.ctrl.value() == 0):
            display.LCD.fill_rect(60, 105, 30, 30, display.LCD.red)
            sleep(button_pause)
            kapka.jump()
        else:
            display.LCD.fill_rect(60, 105, 30, 30, display.LCD.white)
            display.LCD.rect(60, 105, 30, 30, display.LCD.red)
        
        display.LCD.show()
    return 1