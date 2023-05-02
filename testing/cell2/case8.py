'''
case 8

in this case all  motors from cell two
must move forward and backward and stop togther

cell-no: 21
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
    GPIO.cleanup() 


case8()     