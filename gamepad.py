#!/usr/bin/env python
# coding: Latin-1

# Load library functions we want

from inputs import get_gamepad
from explorerhat import motor
from drv8830 import DRV8830, I2C_ADDR1, I2C_ADDR3

def runCommand(commmand):
    print("RunningCommand")
    print(command)
    
    if command == "forwards":
        #forwards code
        left.forward()
        right.forward()
        left.set_voltage(powerDrv)
        right.set_voltage(powerDrv)
        motor.one.forwards(powerExp)
        motor.two.forwards(powerExp)
    elif command == "reverse":
        left.reverse()
        right.reverse()
        left.set_voltage(powerDrv)
        right.set_voltage(powerDrv)
        motor.one.backwards(powerExp)
        motor.two.backwards(powerExp)
    elif command == "left":
        left.reverse()
        right.forward()
        left.set_voltage(powerDrv)
        right.set_voltage(powerDrv)
        motor.one.forwards(powerExp)
        motor.two.backwards(powerExp)
    elif command == "right":
        left.forward()
        right.reverse()
        left.set_voltage(powerDrv)
        right.set_voltage(powerDrv)
        motor.one.backwards(powerExp)
        motor.two.forwards(powerExp)
    elif command == "turnLeft":
        left.reverse()
        right.forward()
        left.set_voltage(powerDrv)
        right.set_voltage(powerDrv)
        motor.one.backwards(powerExp)
        motor.two.forwards(powerExp)
    elif command == "turnRight":
        left.forward()
        right.reverse()
        left.set_voltage(powerDrv)
        right.set_voltage(powerDrv)
        motor.one.forwards(powerExp)
        motor.two.backwards(powerExp)
    elif command == "forwardsLeft":
        left.brake()
        right.forward()
        left.set_voltage(0)
        right.set_voltage(powerDrv)
        motor.one.forwards(powerExp)
        motor.two.stop()
    elif command == "forwardsRight":
        left.forward()
        right.brake()
        left.set_voltage(powerDrv)
        right.set_voltage(0)
        motor.one.stop()
        motor.two.forwards(powerExp)
    elif command == "reverseLeft":
        left.reverse()
        right.brake()
        left.set_voltage(powerDrv)
        right.set_voltage(0)
        motor.one.stop()
        motor.two.backwards(powerExp)
    elif command == "reverseRight":
        left.brake()
        right.reverse()
        left.set_voltage(0)
        right.set_voltage(powerDrv)
        motor.one.backwards(powerExp)
        motor.two.stop()
    elif command == "stop":
        left.brake()
        right.brake()
        motor.one.stop()
        motor.two.stop()
        right.set_voltage(0)
        left.set_voltage(0)

# Init
left = DRV8830(I2C_ADDR1)
right = DRV8830(I2C_ADDR3)

maxPowerExplorer = 100
maxPowerDrv = 5.06
powerExp = maxPowerExplorer * 0.5
powerDrv = maxPowerDrv * 0.5

command = ""

try:
    print('Press CTRL+C to quit')

    # Loop indefinitely
    while True:

        events = get_gamepad()

        command = ""

        for event in events:
            #print(event.code, event.state)
            if event.code == "ABS_Y":
                # Left stick y axis
                if event.state > 130:
                    command = "reverse"
                    #print("reverse")
                elif event.state < 125:
                    # print("forwards")
                    command = "forwards"
            if event.code == "ABS_Z":
                # Right stick x axis
                if event.state > 130:
                    print("turn right")
                    command = "turnRight"
                elif event.state < 125:
                    print("turn left")
                    command = "turnLeft"
            if event.code == "ABS_X":
                # Left stick x axis
                if event.state > 130:
                    print("Right")
                    command = "right"
                elif event.state < 125:
                    command = "left"
            if event.code == "BTN_TL":
                if event.state == True:
                    command = "reverseLeft"
                    print("L2")
            if event.code == "BTN_TR":
                if event.state == True:
                    print("R2")
                    command = "reverseRight"
            if event.code == "BTN_Z":
                if event.state == True:
                    print("R1")
                    command = "forwardsRight"
            if event.code == "BTN_WEST":
                if event.state == True:
                    print("L1")
                    command = "forwardsLeft"
            if event.code == "BTN_EAST":
                    command = "stop"
            #else:
                #runCommand("stop")
            runCommand(command)

except KeyboardInterrupt:

    # CTRL+C exit, disable all drives
    print("stop")
    motor.stop()
print("bye")
