import time
import board
import digitalio

photo = digitalio.DigitalInOut(board.D8)
photo.direction = digitalio.Direction.INPUT
photo.pull = digitalio.Pull.UP

photoCounter = 0
lastbutton = True
initial = time.monotonic()
#lasttime = 0
#now = 0

while True:
    now = time.monotonic()
    if now > initial + 4:
    #if clock is greater than last time + 4
        print("The number of interrupts is:")
        print(photoCounter)
        initial = now
    if photo.value and not lastbutton:
        photoCounter = photoCounter + 1

#    else:
 #       initial = now

    lastbutton = photo.value