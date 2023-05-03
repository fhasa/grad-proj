
import RPi.GPIO as GPIO
from time import sleep

# high low ->forward
# low high ->backward 

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

def moveCityAheavy():

    #cell1 movements

    #cell1 f movement
    # f stop 
    GPIO.output(cell1Fa,GPIO.LOW)
    GPIO.output(cell1Fb,GPIO.LOW)
    #cell1 T movement 
    # t back
    GPIO.output(cell1Ta,GPIO.HIGH)
    GPIO.output(cell1Tb,GPIO.LOW)    
    #cell1 M movement 
    # m forward
    GPIO.output(cell1Ma,GPIO.LOW)
    GPIO.output(cell1Mb,GPIO.HIGH)   
    
    #cell2 movements

    #cell2 f movement
    # f back 
    GPIO.output(cell2Fa,GPIO.HIGH)
    GPIO.output(cell2Fb,GPIO.LOW)
    #cell2 T movement 
    # t back
    GPIO.output(cell2Ta,GPIO.HIGH)
    GPIO.output(cell2Tb,GPIO.LOW)    
    #cell2 M movement 
    #  m stop
    GPIO.output(cell2Ma,GPIO.LOW)
    GPIO.output(cell2Mb,GPIO.LOW)  
   
    #cell3 movements
    #
    #cell3 f movement 
    # f stop
    GPIO.output(cell3Fa,GPIO.LOW)
    GPIO.output(cell3Fb,GPIO.LOW)
    #cell3 T movement 
    #t back
    GPIO.output(cell3Ta,GPIO.HIGH)
    GPIO.output(cell3Tb,GPIO.LOW)    
    #cell3 M movement 
    #m forward
    GPIO.output(cell3Ma,GPIO.LOW)
    GPIO.output(cell3Mb,GPIO.HIGH)  
   

    #cell4 movements

    #cell4 f movement
    # f back ward 
    GPIO.output(cell3Fa,GPIO.HIGH)
    GPIO.output(cell3Fb,GPIO.LOW)
    #cell4 T movement
    # t stop 
    GPIO.output(cell3Ta,GPIO.LOW)
    GPIO.output(cell3Tb,GPIO.LOW)    
    #cell4 M movement 
    # m backword
    GPIO.output(cell3Ma,GPIO.HIGH)
    GPIO.output(cell3Mb,GPIO.LOW)  
    sleep(15)
    GPIO.cleanup() 
moveCityAheavy()



