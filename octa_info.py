import os.path
import keyboard
import curses

screen = curses.initscr()
screen.clear()
screen.refresh()

def printStuff(programIndex):
    f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "{0}.txt".format(programIndex)), "r")
    content = f.read()
    screen.clear()
    screen.addstr("PROGRAM {0}\n".format(programIndex))
    screen.addstr("-------------------------------------\n")
    screen.addstr(content)
    screen.refresh()

printStuff(0)

while True:
    curses.napms(1)
    if keyboard.is_pressed('a'):
        printStuff(0)

    if keyboard.is_pressed('s'):
        printStuff(1)

    if keyboard.is_pressed('q'):
        curses.endwin()
        break
