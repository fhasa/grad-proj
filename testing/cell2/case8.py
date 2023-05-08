'''
case 8

in this case all  motors from cell two
must move forward and backward and stop togther

cell-no: 2
motor: F, T, M

movement: 
F,T, M: Forward and backward and Stop

Excpected output: all  motors from cell2 
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


#cell2

cell2Fa= 2
cell2Fb=3
cell2Ta =4
cell2Tb=14
cell2Ma=15
cell2Mb=17




# speed pin

#cell2
GPIO.setup(cell2Ta,GPIO.OUT)
GPIO.setup(cell2Tb,GPIO.OUT)

GPIO.setup(cell2Fb,GPIO.OUT)
GPIO.setup(cell2Fa,GPIO.OUT)

GPIO.setup(cell2Ma,GPIO.OUT)
GPIO.setup(cell2Mb,GPIO.OUT)




'''
the running code will start here
 here i define the code as a function and i call it
'''

def case8():# whole cell will move forward and backward and stop togther

    # cell2 move forward 
    #cell2 f movement 
    GPIO.output(cell2Fa,GPIO.LOW)
    GPIO.output(cell2Fb,GPIO.HIGH)
    #cell2 T movement 
    GPIO.output(cell2Ta,GPIO.LOW)
    GPIO.output(cell2Tb,GPIO.HIGH)    
    #cell2 M movement 
    GPIO.output(cell2Ma,GPIO.LOW)
    GPIO.output(cell2Mb,GPIO.HIGH)   
    sleep(8)

    # cell2 move backward 
    #cell2 f movement 
    GPIO.output(cell2Fa,GPIO.HIGH)
    GPIO.output(cell2Fb,GPIO.LOW)
    #cell2 T movement 
    GPIO.output(cell2Ta,GPIO.HIGH)
    GPIO.output(cell2Tb,GPIO.LOW)    
    #cell2 M movement 
    GPIO.output(cell2Ma,GPIO.HIGH)
    GPIO.output(cell2Mb,GPIO.LOW)  

    sleep(6)
    # cell 2 stop 
    #cell2 f movement 
    GPIO.output(cell2Fa,GPIO.LOW)
    GPIO.output(cell2Fb,GPIO.LOW)
    #cell2 T movement 
    GPIO.output(cell2Ta,GPIO.LOW)
    GPIO.output(cell2Tb,GPIO.LOW)    
    #cell2 M movement 
    GPIO.output(cell2Ma,GPIO.LOW)
    GPIO.output(cell2Mb,GPIO.LOW) 


case8()     
sleep(5)  
GPIO.cleanup()