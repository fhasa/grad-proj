'''
case 17

in this case we will test the movement of cell 1 and 3 togther

cell-no: 1 + 3
motor: all motors
movement


Excpected output:  cell 1 and cell 3 will move 8 seconds together 
forward and then for 8 second backward

'''
import RPi.GPIO as GPIO
from time import sleep


# high low ->backword
# low high ->forward 

##########################################    settig pins start here ############################################################3

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#cell1

cell1Fa= 18
cell1Fb=22
cell1Ta = 21
cell1Tb=19
cell1Ma=36
cell1Mb=38




#cell3

cell3Fa= 27
cell3Fb=23
cell3Ta = 24
cell3Tb=10
cell3Ma=9
cell3Mb=11


# speed pin

#cell1
GPIO.setup(cell1Ta,GPIO.OUT)
GPIO.setup(cell1Tb,GPIO.OUT)

GPIO.setup(cell1Fb,GPIO.OUT)
GPIO.setup(cell1Fa,GPIO.OUT)

GPIO.setup(cell1Ma,GPIO.OUT)
GPIO.setup(cell1Mb,GPIO.OUT)

#cell3
GPIO.setup(cell3Ta,GPIO.OUT)
GPIO.setup(cell3Tb,GPIO.OUT)

GPIO.setup(cell3Fb,GPIO.OUT)
GPIO.setup(cell3Fa,GPIO.OUT)

GPIO.setup(cell3Ma,GPIO.OUT)
GPIO.setup(cell3Mb,GPIO.OUT)





'''
the running code will start here
 here i define the code as a function and i call it
'''

def case18():
   
    # cell1 movement
    #cell1 f movement 
    GPIO.output(cell1Fa,GPIO.LOW)
    GPIO.output(cell1Fb,GPIO.HIGH)
    #cell1 T movement 
    GPIO.output(cell1Ta,GPIO.LOW)
    GPIO.output(cell1Tb,GPIO.HIGH)    
    #cell1 M movement 
    GPIO.output(cell1Ma,GPIO.LOW)
    GPIO.output(cell1Mb,GPIO.HIGH)   
    

    #cell3 movement code 
    #cell3 f movement 
    GPIO.output(cell3Fa,GPIO.LOW)
    GPIO.output(cell3Fb,GPIO.HIGH)
    #cell3 T movement 
    GPIO.output(cell3Ta,GPIO.LOW)
    GPIO.output(cell3Tb,GPIO.HIGH)    
    #cell M movement 
    GPIO.output(cell3Ma,GPIO.LOW)
    GPIO.output(cell3Mb,GPIO.HIGH)  

    sleep(8)


# ######### stop case #####
    # cell 1 stop 
    #cell1 f movement 
    GPIO.output(cell1Fa,GPIO.LOW)
    GPIO.output(cell1Fb,GPIO.LOW)
    #cell1 T movement 
    GPIO.output(cell1Ta,GPIO.LOW)
    GPIO.output(cell1Tb,GPIO.LOW)    
    #cell1 M movement 
    GPIO.output(cell1Ma,GPIO.LOW)
    GPIO.output(cell1Mb,GPIO.LOW) 
 
    # cell 3 stop 
    #cell3 f movement 
    GPIO.output(cell3Fa,GPIO.LOW)
    GPIO.output(cell3Fb,GPIO.LOW)
    #cell3 T movement 
    GPIO.output(cell3Ta,GPIO.LOW)
    GPIO.output(cell3Tb,GPIO.LOW)    
    #cell3 M movement 
    GPIO.output(cell3Ma,GPIO.LOW)
    GPIO.output(cell3Mb,GPIO.LOW) 


case18()     
sleep(5)
GPIO.cleanup() 
