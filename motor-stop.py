import time
from explorerhat import motor
from drv8830 import DRV8830, I2C_ADDR1, I2C_ADDR3


left = DRV8830(I2C_ADDR1)
right = DRV8830(I2C_ADDR3)

#Clean up
left.brake()
right.brake()
motor.one.speed(0)
motor.two.speed(0)
right.set_voltage(0)
left.set_voltage(0)
