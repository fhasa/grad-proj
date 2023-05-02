'''
case 10

in this case T motor from cell three 
must move forward and backword 

cell-no: 3
motor: T
movement

T: Forward and backward
F: stop
M: Stop

Excpected output:  T motor from cell3
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

#cell1

cell1Fa= 18
cell1Fb=22
cell1Ta = 21
cell1Tb=19
cell1Ma=36
cell1Mb=38


#cell2

cell2Fa= 2
cell2Fb=3
cell2Ta =4
cell2Tb=14
cell2Ma=15
cell2Mb=17


#cell3

cell3Fa= 27
cell3Fb=23
cell3Ta = 24
cell3Tb=10
cell3Ma=9
cell3Mb=11

#cell4

cell4Fa= 25
cell4Fb=8
cell4Ta =7
cell4Tb=1
cell4Ma=12
cell4Mb=16




# speed pin

#cell1
GPIO.setup(cell1Ta,GPIO.OUT)
GPIO.setup(cell1Tb,GPIO.OUT)

GPIO.setup(cell1Fb,GPIO.OUT)
GPIO.setup(cell1Fa,GPIO.OUT)

GPIO.setup(cell1Ma,GPIO.OUT)
GPIO.setup(cell1Mb,GPIO.OUT)

#cell2
GPIO.setup(cell2Ta,GPIO.OUT)
GPIO.setup(cell2Tb,GPIO.OUT)

GPIO.setup(cell2Fb,GPIO.OUT)
GPIO.setup(cell2Fa,GPIO.OUT)

GPIO.setup(cell2Ma,GPIO.OUT)
GPIO.setup(cell2Mb,GPIO.OUT)

#cell3
GPIO.setup(cell3Ta,GPIO.OUT)
GPIO.setup(cell3Tb,GPIO.OUT)

GPIO.setup(cell3Fb,GPIO.OUT)
GPIO.setup(cell3Fa,GPIO.OUT)

GPIO.setup(cell3Ma,GPIO.OUT)
GPIO.setup(cell3Mb,GPIO.OUT)

#cell4
GPIO.setup(cell4Ta,GPIO.OUT)
GPIO.setup(cell4Tb,GPIO.OUT)

GPIO.setup(cell4Fb,GPIO.OUT)
GPIO.setup(cell4Fa,GPIO.OUT)

GPIO.setup(cell4Ma,GPIO.OUT)
GPIO.setup(cell4Mb,GPIO.OUT)
# settig pins ends here





'''
the running code will start here
 here i define the code as a function and i call it
'''

def case10():# T will move forward and backward 

    # F move forward 
    #cell3 f movement 
    GPIO.output(cell3Fa,GPIO.LOW)
    GPIO.output(cell3Fb,GPIO.LOW)
    #cell3 T movement 
    GPIO.output(cell3Ta,GPIO.LOW)
    GPIO.output(cell3Tb,GPIO.HIGH)    
    #cell3 M movement 
    GPIO.output(cell3Ma,GPIO.LOW)
    GPIO.output(cell3Mb,GPIO.LOW)   
    sleep(8)

    # T move backward 
    #cell3 f movement 
    GPIO.output(cell3Fa,GPIO.LOW)
    GPIO.output(cell3Fb,GPIO.LOW)
    #cell3 T movement 
    GPIO.output(cell3Ta,GPIO.HIGH)
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
    GPIO.cleanup() 


case10()     