'''
case 9

in this case F motor from cell three 
must move forward and backword 

cell-no: 3
motor: F
movement

F: Forward and backward
T: stop
M: Stop

Excpected output:  F motor from cell3
move forward for 8 second then backward 
for 7 second then the whole cell stops
'''
import RPi.GPIO as GPIO
from time import sleep


# high low ->backword
# low high ->forward 

##########################################    settig pins start here ############################################################3

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)



#cell3

cell3Fa= 27
cell3Fb=23
cell3Ta = 24
cell3Tb=10
cell3Ma=9
cell3Mb=11




# speed pin

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

def case9():
    # F will move forward and backward 

    # F move forward 
    #cell3 f movement 
    GPIO.output(cell3Fa,GPIO.LOW)
    GPIO.output(cell3Fb,GPIO.HIGH)
    #cell3 T movement 
    GPIO.output(cell3Ta,GPIO.LOW)
    GPIO.output(cell3Tb,GPIO.LOW)    
    #cell3 M movement 
    GPIO.output(cell3Ma,GPIO.LOW)
    GPIO.output(cell3Mb,GPIO.LOW)   
    sleep(8)

    # F move backward 
    #cell3 f movement 
    GPIO.output(cell3Fa,GPIO.HIGH)
    GPIO.output(cell3Fb,GPIO.LOW)
    #cell3 T movement 
    GPIO.output(cell3Ta,GPIO.LOW)
    GPIO.output(cell3Tb,GPIO.LOW)    
    #cell3 M movement 
    GPIO.output(cell3Ma,GPIO.LOW)
    GPIO.output(cell3Mb,GPIO.LOW)  

    sleep(6)
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


case9()     
sleep(5)  
GPIO.cleanup()