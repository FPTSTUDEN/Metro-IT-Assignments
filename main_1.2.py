"""
Hardware project simulator
First year hardware project
School of ICT
Metropolia University of Applied Sciences
28.8.2025, Sakari Lukkarinen
"""

import machine
from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import utime

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled = SSD1306_I2C(100, 40, i2c) 
max_lines = 6 

lines = []
while True: 
    text = input("enter your text: ")
    lines.append(text)

    if len(lines) > max_lines:
        del lines[0]
    
    oled.fill(0)
    for i in range(len(lines)): 
        print(i, lines[i])
        oled.text(lines[i], 0, i * 8)
    oled.show()
