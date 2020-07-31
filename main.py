## SETUP
# Import Libraries
import RPi.GPIO as gpio
import curses
import time

# Initialize Screen
stdscr = curses.initscr()

# Declare Variables
FOREGROUND = curses.COLOR_WHITE
BACKGROUND = curses.COLOR_BLACK
ASCII = {i: chr(i) for i in range (128)} # ASCII dictionary
h, w = stdscr.getmaxyx() # Screen size
running = True # variable to control the main loop
forward_pin = 12
reverse_pin = 11
power = 100
gear = 'D'

## FUNCTIONS
# Raspberry Pi Functions
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

def cleanup():
    stop()
    gpio.cleanup()

# Curses Functions
def display_text(text, position_y=0, position_x=0, center_y=False, center_x=False, offset_y=0, offset_x=0):
    '''
    Displays text on the terminal screen using Curses
    Parameters:
    text: Text to be displayed on the screen
    position_y: Position on the y axis where text will be displayed (overwritten by center_y)
    position_x: Position on the x axis where text will be displayed (overwritten by center_x)
    center_y: Centers the text on the y axis with an optional offset (offset_y), overwrites position_y
    center_x: Centers the text on the x axis with an optional offset (offset_x), overwrites position_x
    offset_y: Offsets the position along the y axis IF center_y is True
    offset_x: Offsets the position along the x axis IF center_x is True
    '''
    global h
    global w
    h, w = stdscr.getmaxyx()
    if center_x:
        x = int((w / 2 - len(text) / 2) + offset_x)
    else:
        x = position_x
    if center_y:
        y = int((h / 2) + offset_y)
    else:
        y = position_y

    stdscr.addstr(y, x, text)
    stdscr.refresh()

def process_key(key):
    global running
    stdscr.clear()
    if key < 128:
        letter = display_text(ASCII[key])
        if letter.lower() == 'w':
            if gear == 'D':
                forward(power)
            elif gear == 'R':
                reverse(power)
            else:
                stop()
        elif letter.lower() == 's':
            stop()
        elif letter == 'q':
            if power >= 5:
                power -= 5
            else:
                power = 0
        elif letter == 'e':
            if power <= 95:
                power += 5
            else:
                power = 100
        elif letter == 'Q':
            if gear == 'D':
                gear = 'N'
            elif gear == 'N':
                gear = 'R'
            else:
                gear = 'R'
        elif letter == 'E':
            if gear == 'R':
                gear = 'N'
            elif gear == 'N':
                gear = 'D'
            else:
                gear = 'D'
        elif letter == ' ':
            stop()
        elif letter.lower() == 'p':
            running = False
        else:
            stop()
    else:
        pass



### MAIN FUNCTION
def main(stdscr):
    try:
        ## Setup
        # Curses
        curses.curs_set(0)
        curses.init_pair(1, FOREGROUND, BACKGROUND)
        # Raspberry Pi
        setup()

        stdscr.attron(curses.color_pair(1))

        ## Main Loop
        while running:
            # Input
            key = stdscr.getch()
            process_key(key)
            # Update
            display_text(gear, y_position=1, center_x=True)

        cleanup()
    except(Exception):
        print(Exception)
        cleanup()

curses.wrapper(main)
