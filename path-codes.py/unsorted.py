import RPi.GPIO as GPIO
from time import sleep

# high low -> backward
# low high -> forward 

# settig pins start here

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#cell1

cell1Fa= 18
cell1Fb=22
cell1Ta = 21
cell1Tb=19
cell1Ma=36
cell1Mb=38


#cell1
GPIO.setup(cell1Ta,GPIO.OUT)
GPIO.setup(cell1Tb,GPIO.OUT)

GPIO.setup(cell1Fb,GPIO.OUT)
GPIO.setup(cell1Fa,GPIO.OUT)

GPIO.setup(cell1Ma,GPIO.OUT)
GPIO.setup(cell1Mb,GPIO.OUT)
def moveUnsorted():

    #cell1 movements

    #cell1 f movement 
    # f for
    GPIO.output(cell1Fa,GPIO.LOW)
    GPIO.output(cell1Fb,GPIO.HIGH)
    #cell1 T movement 
    GPIO.output(cell1Ta,GPIO.LOW)
    GPIO.output(cell1Tb,GPIO.HIGH)    
    #cell1 M movement 
    GPIO.output(cell1Ma,GPIO.LOW)
    GPIO.output(cell1Mb,GPIO.LOW)   
    sleep(15)
   

moveUnsorted()
sleep(5)
GPIO.cleanup() 
