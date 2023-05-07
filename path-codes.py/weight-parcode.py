#! /usr/bin/python2

import time
import sys

# HOW TO CALCULATE THE REFFERENCE UNIT
# In this case, 92 is 1 gram because, with 1 as a reference unit I got numbers near 0 without any weight
# and I got numbers around 184000 when I added 2kg. So, according to the rule of thirds:
# If 2000 grams is 184000 then 1000 grams is 184000 / 2000 = 92.
referenceUnit = 113

import RPi.GPIO as GPIO
from hx711_lib import HX711  #import this from file "hx711_lib.py"  


def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()
        
    print("Bye!")
    sys.exit()

hx = HX711(5, 6)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(referenceUnit)
hx.reset()
hx.tare()

print("Tare done! Add weight now...")
val=0
while True:
    
    try:
        
        if abs(val-((abs(hx.get_weight(5))/2)*0.05+((abs(hx.get_weight(5))/2))))>5 :
          val = (abs(hx.get_weight(5))/2)*0.05+((abs(hx.get_weight(5))/2))
          print(val)
        
          if val<=300: #gram
           print("light weight")
          elif val>300 : #gram
           print("heavy weight")
            
          hx.power_down()
          hx.power_up()
          time.sleep(0.1)

        val = (abs(hx.get_weight(5))/2)*0.05+((abs(hx.get_weight(5))/2))
        
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
        
        
        
'''
#connection

==========load cell interface to hx711==========
Red: E+
Black: E-
Green: A-
White: A+
================================================

============ hx711 interface to RPI ============
VCC to Raspberry Pi Pin 2 (5V)
GND to Raspberry Pi Pin 6 (GND)
DT to Raspberry Pi Pin 29 (GPIO 5)
SCK to Raspberry Pi Pin 31 (GPIO 6)
================================================

'''






  