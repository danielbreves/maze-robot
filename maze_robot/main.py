# Import necessary modules
from machine import Pin, freq, PWM
from pico_car import Motor, Car, Ultrasonic
import uasyncio as asyncio


# Add time library
import time

# Initialise motors
ultrasonic_m = Ultrasonic(27, 26) #echo, trigger
ultrasonic_l = Ultrasonic(3, 2)
ultrasonic_r = Ultrasonic(14, 15)
motor_left = Motor(19, 20, 21)
motor_right = Motor(18, 17, 16)


# Onboard led
led = Pin("LED", Pin.OUT)


# Create car object
picoCar = Car(motor_left, motor_right)

# Wait a few seconds before starting the sequence
time.sleep(1)

# Functions
def get_ultrasonic_distance(): # Return all distances
    return (round(ultrasonic_r.check()), round(ultrasonic_m.check()), round(ultrasonic_l.check()))

# Ultrasonic Test

prev_list = [get_ultrasonic_distance(), get_ultrasonic_distance(), get_ultrasonic_distance(), get_ultrasonic_distance()]

while True:
    us_distance = get_ultrasonic_distance()
    prev_list.append(us_distance)
    prev_list.pop(0)    
    if (us_distance[1] < 15 or us_distance[2] > 15):
        
        print("Right: "+str({us_distance[0]}) + " Middle: " + str({us_distance[1]}) + " Left: " + str({us_distance[2]}) + "      " + str(prev_list) + "       "+ "      Turning Right")
    else:
        print("Right: "+str({us_distance[0]}) + " Middle: " + str({us_distance[1]}) + " Left: " + str({us_distance[2]}) + "      " + str(prev_list) + "       ")
    time.sleep(0.5)


# Movement function
def move():
    print('True')
    GREEN_ZONE = 60
    ORANGE_ZONE = 15

    # Get ultrasonic distance
    us_distance = get_ultrasonic_distance()
    if us_distance[0] < 8: # Turn if ffacing wall
        picoCar.right(50)
        time.sleep(0.02)
    elif us_distance[2] < 8:
        picoCar.left(50)
        time.sleep(0.02)
    else:
        # Movement
        if us_distance[1] >= GREEN_ZONE: # Distance is greater than green zone
            picoCar.forward(speed=120)
            led.off()
        elif us_distance[1] < GREEN_ZONE and us_distance[1] >= ORANGE_ZONE: # Distance is between green and orange zone
            picoCar.forward(speed=100)
            led.off()

        else: # Distance is less than orange zone
            if us_distance[2] > us_distance[0]: # turn left
                picoCar.right(speed = 100) 
                time.sleep(0.35)
            else: # turn right
                picoCar.left(speed = 102)
                time.sleep(0.35)
    


        
# Control sequence
while True:
    move() 
    time.sleep(0.1)


 