import time
from explorerhat import motor
from drv8830 import DRV8830, I2C_ADDR1, I2C_ADDR3

left = DRV8830(I2C_ADDR1)
right = DRV8830(I2C_ADDR3)

# Move forward
#left.set_direction('forward')
left.forward()
right.forward()
motor.one.forwards()
motor.two.forwards()
time.sleep(3.0)

left.brake()
right.brake()
motor.one.speed(0)
motor.two.speed(0)
