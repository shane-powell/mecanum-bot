import time
from explorerhat import motor
from drv8830 import DRV8830, I2C_ADDR1, I2C_ADDR3

v = 4
speed = 70

left = DRV8830(I2C_ADDR1)
right = DRV8830(I2C_ADDR3)

left.set_voltage(0)
right.set_voltage(0)
#time.sleep(3)

#Set Voltages
left.set_voltage(v)
right.set_voltage(v)

# Move forward
left.forward()
right.forward()
motor.one.forwards(speed)
motor.two.forwards(speed)
time.sleep(0.5)

# Slide to the left
left.reverse()
right.forward()
motor.one.forwards(speed)
motor.two.backwards(speed)
time.sleep(2)

# Slide to the right
left.forward()
right.reverse()
motor.one.backwards(speed)
motor.two.forwards(speed)
time.sleep(2)

# Take it back now yall
left.reverse()
right.reverse()
motor.one.backwards(speed)
motor.two.backwards(speed)
time.sleep(0.5)

#Clean up
left.brake()
right.brake()
motor.one.speed(0)
motor.two.speed(0)
right.set_voltage(0)
left.set_voltage(0)
