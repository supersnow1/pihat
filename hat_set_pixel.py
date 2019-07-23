#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
red = (255, 0, 0)
yellow = (0, 255, 0)
blue = (0, 0, 255)
import time

sense.set_pixel(2, 2, blue)
sense.set_pixel(4, 2, blue)
sense.set_pixel(3, 4, yellow)
sense.set_pixel(1, 5, red)
sense.set_pixel(2, 6, red)
sense.set_pixel(3, 6, red)
sense.set_pixel(4, 6, red)
sense.set_pixel(5, 5, red)


time.sleep(1)
sense.clear()
