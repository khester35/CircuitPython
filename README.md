# CircuitPython
My CircuitPython assignments


### LED Fade

##### Objective 
The objective of this assignment was to make the LED fade in and out. 

##### Lessons
We learned how to use CircuitPython/Metro and Mu. 

##### Code 
'''

import pulseio
import board
import analogio

#pwm = pulseio.PWMOut(board.D13)     # output on D13
#pwm.duty_cycle = 2 ** 15            # Cycles the pin with 50% duty cycle (half of 2 ** 16) at the default 500hz

led = analogio.AnalogOut(board.A0)
brightness = 40000
fadeAmount = 10

import time

while True:
    led.value = brightness
    brightness = brightness + fadeAmount

    if brightness <= 40000 or brightness >= 65000:

        fadeAmount = -fadeAmount
'''

### CircuitPython Servo

##### Objective 
The objective of this assignment was to make a servo consistently sweep back and forth between 0 and 180°.

##### Lessons
We learned how to use capacitive touch, an entirely new concept this year. To make the servo move, you had to be touching one of two wires. The direction that the servo went in hinged on which of the wires you were touching (ex. if you touch the left wire, it will move clockwise and if you touch the right wire, it will move counterclockwise). 

##### Code 

### CircuitPython LCD

##### Objective 
The objective of this assignment was to make an LCD show the number of times a button had been pressed. We used a switch to determine whether it would count up or down. 

##### Lessons
We learned how to make an LCD count button presses and use a switch to alter the direction. I personally had trouble making the counter go up/down by ONLY 1. 

##### Code 

### Photointerrupter 

##### Objective
The objective of this assignment was to make the Serial Monitor count how many times a photointerrupter has been interrupted. It is to output an updated number every four seconds.

##### Lessons
One of my biggest struggles was making the Serial Monitor print every four seconds without using the sleep function. I ended up learning how to do that with a timer instead of a looped function. 

##### Code 

### CircuitPython Distance Sensor

##### Objective 
The objective of this assignment was to coordinate the distance sensor to the onboard LED. 

##### Lessons
In this assignment, we learned how to really work the onboard LED. I had never worked with RGB values before, so that was a valuable experience for later assignments. 

##### Code 

### Classes, Objects, and Modules

##### Objective 
The objective of this assignment was to learn how to make classes, objects, and modules. 

##### Lessons
This assignment gave insight into what makes the things we regularly use in our code work; it also introduced vital information for later assignments. I feel that my biggest struggle was the rainbow function because it was a lot less straightforward than  the colors (which were fiarly self explanatory). I also became familiar with RGB LEDs and the required wiring.

##### Code 

### Hello VS Code

##### Objective 
The objective of this assignment was to learn how to navigate CircuitPython by having a random message print to the Serial Monitor. 

##### Lessons
This assignment was more introductory than anything else, but it was a really good stepping stone to using the program for complicated assignments. It effectively worked through things that I would have had a lot of questions about later. 

##### Code 

### FancyLED

##### Objective 
The objective of this assignment was to use classes, objects, and modules. We were to make a code that had a 6 LEDs go through three functions: sparkle, chase, blink, and alternate. 

##### Lessons
The Classes, Objects, and Modules assignment was extremely helpful here because the setup (if not the code) was very similar. Creating chase, blink, and alternate were fairly simple, but sparkle was a little more complicated. I got some help from Philip and Camden and added some comments on my final code to help future confusion. 

##### Code 

