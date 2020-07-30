import RPi.GPIO as gpio
import time

forward_pin = 12
reverse_pin = 11
power = 100

def setup():
    # Raspberry Pi Setup
    gpio.setmode(gpio.BOARD)
    gpio.setup(forward_pin, gpio.OUT)
    gpio.setup(reverse_pin, gpio.OUT)

    # PWM Setup
    global forward_pwm
    forward_pwm = gpio.PWM(forward_pin, 1000)
    forward_pwm.start(0)
    global reverse_pwm
    reverse_pwm = gpio.PWM(reverse_pin, 1000)
    reverse_pwm.start(0)

def forward(speed=100):
    #gpio.output(forward_pin, gpio.HIGH)
    gpio.output(reverse_pin, gpio.LOW)
    forward_pwm.ChangeDutyCycle(speed)

def reverse(speed=100):
    #gpio.output(reverse_pin, gpio.HIGH)
    gpio.output(forward_pin, gpio.LOW)
    reverse_pwm.ChangeDutyCycle(speed)

def stop():
    gpio.output(forward_pin, gpio.LOW)
    gpio.output(reverse_pin, gpio.LOW)


setup()


forward(power)
time.sleep(2)
stop()
gpio.cleanup()
