import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Motor 1 pins
Motor1A = 11
Motor1B = 12
Motor1E = 13

# Motor 2 pins
Motor2A = 15
Motor2B = 16
Motor2E = 18

# Set up GPIO pins for motor 1
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)
motor1_pwm = GPIO.PWM(Motor1E, 100)
motor1_pwm.start(0)

# Set up GPIO pins for motor 2
GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)
GPIO.setup(Motor2E, GPIO.OUT)
motor2_pwm = GPIO.PWM(Motor2E, 100)
motor2_pwm.start(0)

# Function to move motors forward with speed control
def forward(speed):
    # Set motor 1 to move forward
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    
    # Set motor 2 to move forward
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    
    # Set motor speeds using PWM signals
    motor1_pwm.ChangeDutyCycle(speed)
    motor2_pwm.ChangeDutyCycle(speed)

# Function to move motors backward with speed control
def backward(speed):
    # Set motor 1 to move backward
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    
    # Set motor 2 to move backward
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    
    # Set motor speeds using PWM signals
    motor1_pwm.ChangeDutyCycle(speed)
    motor2_pwm.ChangeDutyCycle(speed)

# Function to stop motors
def stop():
    # Set motor speeds to 0
    motor1_pwm.ChangeDutyCycle(0)
    motor2_pwm.ChangeDutyCycle(0)

# Main program loop
while True:
    # Move motors forward at half speed for 2 seconds
    forward(50)
    time.sleep(2)
    
    # Stop motors for 1 second
    stop()
    time.sleep(1)
    
    # Move motors backward at full speed for 2 seconds
    backward(100)
    time.sleep(2)
    
    # Stop motors for 1 second
    stop()
    time.sleep(1)
