#!/usr/bin/env python
from sense_hat import SenseHat
import time 
import random
sense = SenseHat()

x = random.randint(0, 7)
y = random.randint(0, 7)
color = random.randint (0, 255)
a = (color, 0, 0)
b =(0, color, 0)
c =(0, color, 0)

sense.set_pixel(x, y, a)
sense.set_pixel(x, y, b)
sense.set_pixel(x, y, c)

time.sleep(1)
sense.clear()



