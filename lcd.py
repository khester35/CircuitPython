import time
import board
import digitalio

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

button_a = digitalio.DigitalInOut(board.D2)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.UP

switch = digitalio.DigitalInOut(board.D8)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

from lcd.lcd import CursorMode

lcd = LCD(I2CPCF8574Interface(0x3F), num_rows=4, num_cols=20)

lcd.clear()

lcd.set_cursor_pos(0, 0)
lcd.print("Button Presses:")

lcd.set_cursor_mode(CursorMode.LINE)
presses = 0
lastbutton = True
while True:

    if not button_a.value and switch.value and lastbutton:
        lcd.set_cursor_pos(1,0)
        presses = presses + 1
        lcd.print(str(presses))
        lcd.print("    ")

    if not button_a.value and not switch.value and lastbutton:
        lcd.set_cursor_pos(1,0)
        presses = presses - 1
        lcd.print(str(presses))
        lcd.print("    ")
    lastbutton = button_a.value