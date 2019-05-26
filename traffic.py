from gpiozero import Button, LED
from time import sleep
button = Button(21)
red = LED(2)
yellow = LED(3)
green = LED(4)

red.off()
yellow.off()
green.on()

while True:
    button.wait_for_press()
    green.off()
    sleep(0.1)
    yellow.blink(0.5,0.5)
    sleep(3)
    yellow.off()
    sleep(0.2)
    red.on()
    sleep(5)
    red.off()
    green.on()
    
