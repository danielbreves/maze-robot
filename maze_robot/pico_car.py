from machine import Pin, freq, PWM
import utime

class Ultrasonic:
    def __init__(self, echo_pin, trigger_pin):
        self.echo = Pin(echo_pin, Pin.IN)
        self.trigger = Pin(trigger_pin, Pin.OUT)
    
    def check(self): # Get ultrasonic distance
        self.trigger.low()
        utime.sleep_us(2)
        self.trigger.high()
        utime.sleep_us(5)
        self.trigger.low()
        while self.echo.value() == 0:
            signaloff = utime.ticks_us()
        while self.echo.value() == 1:
            signalon = utime.ticks_us()
        timepassed = signalon-signaloff
        distance = (timepassed * 0.0343)/2
        return distance

class Motor:
    def __init__(self, input_1_pin, input_2_pin, enable_pin):
        self.forward_pin = Pin(input_1_pin, Pin.OUT)
        self.backward_pin = Pin(input_2_pin, Pin.OUT)
        self.pwm_pin = PWM(Pin(enable_pin))
        self.pwm_pin.freq(1000)

    
    #Helper function to allow speed to be set between 0 - 100.
    def to_pwm(self, value):
        return int(value/100*65535)
        
    def forward(self, speed=100):
        self.pwm_pin.duty_u16(self.to_pwm(speed))
        self.forward_pin.high()
        self.backward_pin.low()
        
    def backward(self, speed=100):
        self.pwm_pin.duty_u16(self.to_pwm(speed))
        self.forward_pin.low()
        self.backward_pin.high()
        
    def stop(self):
        self.forward_pin.low()
        self.backward_pin.low()
        self.pwm_pin.duty_u16(65535)
        

class Car:
    def __init__(self, motor_left, motor_right):
        self.motor_left = motor_left
        self.motor_right = motor_right
        self.turn_wheel_speed_percentage = 60
        
    def forward(self, speed=100):
        self.motor_left.forward(speed)
        self.motor_right.forward(speed)
        
    def backward(self, speed=100):
        self.motor_left.backward(speed)
        self.motor_right.backward(speed)
        
    def backward_left_turn(self, speed=10, duration=2):
        self.motor_left.backward(speed)
        self.motor_right.forward(speed)
        utime.sleep_us(duration)
        self.motor_right.stop()
        self.motor_left.stop()
        
    def backward_right_turn(self, speed=10, duration=2):
        self.motor_left.forward(speed)
        self.motor_right.backward(speed)
        utime.sleep_us(duration)
        self.motor_right.stop()
        self.motor_left.stop()
        
    def right(self, speed=100):
        self.motor_left.stop()
        self.motor_right.forward(speed)
        
    def left(self, speed=100):
        self.motor_left.forward(speed)
        self.motor_right.stop()
    
    def stop(self):
        self.motor_left.stop();
        self.motor_right.stop();
        
    def forward_right(self, speed=100):
        self.motor_left.forward(speed * self.turn_wheel_speed_percentage / 100)
        self.motor_right.forward(speed)
        
    def forward_left(self, speed=100):
        self.motor_left.forward(speed)
        self.motor_right.forward(speed * self.turn_wheel_speed_percentage / 100)
        
    def backward_right(self, speed=100):
        self.motor_left.backward(speed * self.turn_wheel_speed_percentage / 100)
        self.motor_right.backward(speed)
        
    def backward_left(self, speed=100):
        self.motor_left.backward(speed)
        self.motor_right.backward(speed * self.turn_wheel_speed_percentage / 100)
    
    def distance(self):
        trigger = Pin(0, Pin.OUT)
        echo = Pin(1, Pin.IN)
        trigger.low
        utime.sleep_us(2)
        trigger.high()
        utime.sleep_us(5)
        trigger.low()
        while echo.value() == 0:
            signaloff = utime.ticks_us()
        while echo.value() == 1:
            signalon = utime.ticks_us()
        timepassed = signalon - signaloff
        distance = (timepassed * 0.0343) / 2
        return distance
