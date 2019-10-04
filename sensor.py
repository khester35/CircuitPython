import time
import board
import adafruit_hcsr04
import board
import neopixel
from simpleio import map_range

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

while True:
    try:
        distance = sonar.distance
        if distance <= 20:
            r = map_range(distance,0,20,255,0)
            b = map_range(distance,0,20,0,255)
            print(r)
            dot.fill((int(r),0 ,int(b)))

#elif distance <= 35:
 #           r = map_range(distance,10,35,255,0)
  #          print(r)
   #         dot.fill((0,int(r),0))

        else:
            b = map_range(distance,20,35,255,0)
            g = map_range(distance,20,35,0,255)
            print(g)
            dot.fill((0,int(g),int(b)))

    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)