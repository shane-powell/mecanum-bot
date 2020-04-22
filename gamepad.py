#!/usr/bin/env python
# coding: Latin-1

# Load library functions we want

from inputs import get_gamepad
from explorerhat import motor
from drv8830 import DRV8830, I2C_ADDR1, I2C_ADDR3

def runCommand(commmand):
    
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
        right.brake()
        left.set_voltage(0)
        right.set_voltage(powerDrv)
        motor.one.backwards(powerExp)
        motor.two.stop()
    else:
        left.brake()
        right.brake()
        motor.one.stop()
        motor.two.stop()
        right.set_voltage(0)
        left.set_voltage(0)

# Init
left = DRV8830(I2C_ADDR1)
right = DRV8830(I2C_ADDR3)

maxPower  = 1.0
power_left = 0.0
power_right = 0.0
x_axis = 0.0
y_axis = 0.0

maxPowerExplorer = 100
maxPowerDrv = 5.06
powerExp = maxPowerExplorer / 2
powerDrv = maxPowerDrv / 2

command = ""

try:
    print('Press CTRL+C to quit')

    # Loop indefinitely
    while True:

        events = get_gamepad()
        for event in events:
            print(event.code, event.state)
            if event.code == "ABS_Y":
                # Left stick y axis
                if event.state > 130:
                    runCommand("reverse")
                    print("reverse")
                elif event.state < 125:
                    print("forwards")
                    runCommand("forwards")
            elif event.code == "ABS_Z":
                # Right stick x axis
                if event.state > 130:
                    print("turn right")
                    runCommand("turnRight")
                elif event.state < 125:
                    print("turn left")
                    runCommand("turnLeft")
            elif event.code == "ABS_X":
                # Left stick x axis
                if event.state > 130:
                    print("Right")
                    runCommand("right")
                elif event.state < 125:
                    runCommand("left")
            elif event.code == "BTN_TL":
                if event.state == True:
                    runCommand("reverseLeft")
                    print("L2")
            elif event.code == "BTN_TR":
                if event.state == True:
                    print("R2")
                    runCommand("reverseRight")
            elif event.code == "BTN_Z":
                if event.state == True:
                    print("R1")
                    runCommand("forwardsRight")
            elif event.code == "BTN_WEST":
                if event.state == True:
                    print("L1")
                    runCommand("forwardsLeft")
            else:
                runCommand("stop")

except KeyboardInterrupt:

    # CTRL+C exit, disable all drives
    print("stop")
    motor.stop()
print("bye")