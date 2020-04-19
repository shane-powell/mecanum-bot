import time
from explorerhat import motor
from drv8830 import DRV8830, I2C_ADDR1, I2C_ADDR3

left = DRV8830(I2C_ADDR1)
right = DRV8830(I2C_ADDR3)

#Set Voltages
left.set_voltage(5)
right.set_voltage(5)

# Move forward
left.forward()
right.forward()
motor.one.forwards()
motor.two.forwards()
time.sleep(3.0)

# Slide to the left
left.reverse()
right.forward()
motor.one.backwards()
motor.two.forwards()
time.sleep(3.0)

# Slide to the right
left.forward()
right.reverse()
motor.one.forwards()
motor.two.backwards()
time.sleep(3.0)

# Take it back now yall
left.reverse()
right.reverse()
motor.one.backwards()
motor.two.backwards()
time.sleep(3.0)

#Clean up
left.brake()
right.brake()
motor.one.speed(0)
motor.two.speed(0)
right.set_voltage(0)
left.set_voltage(0)
