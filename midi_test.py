import rtmidi.midiutil
import sys
from rtmidi.midiconstants import PROGRAM_CHANGE


print(rtmidi.midiutil.list_input_ports())

portToUse = 1  # FastTrack Input A

try:
    midiIn, portName = rtmidi.midiutil.open_midiinput(portToUse)
except(EOFError, KeyboardInterrupt):
    sys.exit()

while True:
    msg = midiIn.get_message()
    if msg:
        status = msg[0][0]
        data = msg[0][1]
        channel = status & 0xF
        if (status - channel) == PROGRAM_CHANGE:
            print("\nchannel: {0}".format(channel))
            print("data: {0}".format(data))
