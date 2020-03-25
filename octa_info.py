import os.path
import keyboard


def printStuff(programIndex):
    f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "{0}.txt".format(programIndex)), "r")
    content = f.read()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("PROGRAM {0}".format(programIndex))
    print("-----------------------------------------------")
    
    print(content)
    numNewLines = 9 - content.count('\n')
    while numNewLines > 0:
        print("\n")
        numNewLines -= 1

printStuff(0)

while True:
    if keyboard.is_pressed('a'):
        printStuff(0)

    if keyboard.is_pressed('s'):
        printStuff(1)

