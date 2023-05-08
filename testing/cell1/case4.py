'''
case 4

in this case all  motors from cell one 
must move forward and backward and stop togther

cell-no: 1
motor: F, T, M

movement: 
F,T, M: Forward and backward and Stop

Excpected output: all  motors from cell1 
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





# speed pin

#cell1
GPIO.setup(cell1Ta,GPIO.OUT)
GPIO.setup(cell1Tb,GPIO.OUT)

GPIO.setup(cell1Fb,GPIO.OUT)
GPIO.setup(cell1Fa,GPIO.OUT)

GPIO.setup(cell1Ma,GPIO.OUT)
GPIO.setup(cell1Mb,GPIO.OUT)




'''
the running code will start here
 here i define the code as a function and i call it
'''

def case4():# whole cell will move forward and backward and stop togther

    # cell1 move forward 
    #cell1 f movement 
    GPIO.output(cell1Fa,GPIO.LOW)
    GPIO.output(cell1Fb,GPIO.HIGH)
    #cell1 T movement 
    GPIO.output(cell1Ta,GPIO.LOW)
    GPIO.output(cell1Tb,GPIO.HIGH)    
    #cell1 M movement 
    GPIO.output(cell1Ma,GPIO.LOW)
    GPIO.output(cell1Mb,GPIO.HIGH)   
    sleep(8)

    # cell1 move backward 
    #cell1 f movement 
    GPIO.output(cell1Fa,GPIO.HIGH)
    GPIO.output(cell1Fb,GPIO.LOW)
    #cell1 T movement 
    GPIO.output(cell1Ta,GPIO.HIGH)
    GPIO.output(cell1Tb,GPIO.LOW)    
    #cell1 M movement 
    GPIO.output(cell1Ma,GPIO.HIGH)
    GPIO.output(cell1Mb,GPIO.LOW)  

    sleep(6)
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


case4()     
sleep(5)
GPIO.cleanup() 