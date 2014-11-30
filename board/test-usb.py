from practicum import findDevices
from peri import PeriBoard
from time import sleep

devs = findDevices()

if len(devs) == 0:
    print "*** No MCU board found."
    exit(1)

b = PeriBoard(devs[0])
print "*** MCU board found"
print "*** Device manufacturer: %s" % b.getVendorName()
print "*** Device name: %s" % b.getDeviceName()

count = 0
while True:
    sleep(1)
    swu = b.getSwitchUp()
    swd = b.getSwitchDown()
    swl = b.getSwitchLeft()
    swr = b.getSwitchRight()
    swb = b.getSwitchBomb()
    light = b.getLight()

    if swu is True:
        stateUp = "PRESSED"
    else:
        stateUp = "RELEASED"

    if swd is True:
        stateDown = "PRESSED"
    else:
        stateDown = "RELEASED"

    if swl is True:
        stateLeft = "PRESSED"
    else:
        stateLeft = "RELEASED"

    if swr is True:
        stateRight = "PRESSED"
    else:
        stateRight = "RELEASED"

    if swb is True:
        stateBomb = "PRESSED"
    else:
        stateBomb = "RELEASED"

    print "Count: %d | SwitchUp state: %-8s | SwitchDown state: %-8s | SwitchLeft state: %-8s | SwitchRight state: %-8s | SwitchBomb state: %-8s | Light value: %d" % (
            count, stateUp, stateDown, stateLeft, stateRight, stateBomb, light)

    count += 1

