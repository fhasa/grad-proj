'''
case 17

in this case we will test the movement of cell 1 and 2 togther

cell-no: 1 + 2
motor: all motors
movement


Excpected output:  cell 1 and cell 2 will move 8 seconds together 
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

def case17():
   
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
    

    #cell2 movement code 
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

# #### backward movement
    # cell1 movement
    #cell1 f movement 
    GPIO.output(cell1Fa,GPIO.HIGH)
    GPIO.output(cell1Fb,GPIO.LOW)
    #cell1 T movement 
    GPIO.output(cell1Ta,GPIO.HIGH)
    GPIO.output(cell1Tb,GPIO.LOW)    
    #cell1 M movement 
    GPIO.output(cell1Ma,GPIO.HIGH)
    GPIO.output(cell1Mb,GPIO.LOW)   
    

    #cell2 movement code 
    #cell2 f movement 
    GPIO.output(cell2Fa,GPIO.HIGH)
    GPIO.output(cell2Fb,GPIO.LOW)
    #cell2 T movement 
    GPIO.output(cell2Ta,GPIO.HIGH)
    GPIO.output(cell2Tb,GPIO.LOW)    
    #cell2 M movement 
    GPIO.output(cell2Ma,GPIO.HIGH)
    GPIO.output(cell2Mb,GPIO.LOW)  


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


case17()     
sleep(9)
GPIO.cleanup() 
