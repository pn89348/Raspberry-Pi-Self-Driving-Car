# Setup
import time
import curses
stdscr = curses.initscr()

# curses.noecho()
# curses.cbreak()
# stdscr.keypad(True)
# curses.curs_set(0)

running = True
FOREGROUND = curses.COLOR_WHITE
BACKGROUND = curses.COLOR_BLACK
h, w = stdscr.getmaxyx()

def display_text(text, position_y=0, position_x=0, center_x=True, center_y=True, offset_x=0, offset_y=0):
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
    if key == curses.KEY_UP:
        display_text("UP")
    elif key == curses.KEY_DOWN:
        display_text("DOWN")
    elif key == curses.KEY_LEFT:
        running = False
    else:
        display_text("PRESS UP OR DOWN KEY, LEFT TO QUIT")


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, FOREGROUND, BACKGROUND)

    stdscr.attron(curses.color_pair(1))

    while running:
        key = stdscr.getch()
        process_key(key)

curses.wrapper(main)

# # Cleanup
# curses.curs_set(1)
# curses.nocbreak()
# stdscr.keypad(False)
# curses.echo()
# curses.endwin()
