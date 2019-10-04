import pulseio
import board
import analogio

# pwm = pulseio.PWMOut(board.D13)     # output on D13
# pwm.duty_cycle = 2 ** 15            # Cycles the pin with 50% duty cycle (half of 2 ** 16) at the default 500hz

led = analogio.AnalogOut(board.A0)
brightness = 40000
fadeAmount = 10

import time

while True:
    led.value = brightness
    brightness = brightness + fadeAmount

    if brightness <= 40000 or brightness >= 65000:

        fadeAmount = -fadeAmount