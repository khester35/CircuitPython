import board
import neopixel
import digitalio

led = digitalio.DigitalInOut(board.A1)
led.direction = digitalio.Direction.OUTPUT

led.value = True
led.value = False

import time

while True:
     led.value = True
     time.sleep(0.5)
     led.value = False
     time.sleep(0.5)