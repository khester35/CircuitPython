import time
import board
import pulseio
from adafruit_motor import servo
import touchio

touch_pin1 = touchio.TouchIn(board.A4)
print(touch_pin1.value)
touch_pin2 = touchio.TouchIn(board.A5)
print(touch_pin2.value)

# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

my_servo.angle = 90

while True:
    if touch_pin1.value:
      #   for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
            if my_servo.angle >= 2:
                my_servo.angle -= 1
            time.sleep(0.01)

    if touch_pin2.value:
     #    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
            if my_servo.angle <= 179:
                my_servo.angle += 1
            time.sleep(0.01)