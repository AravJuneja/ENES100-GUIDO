"""
main.py acts as the mission controller.
"""

from motor_control import MotorControl



# Pin Configs for Motors 
PIN_IN1 = 19
PIN_IN2 = 18
PIN_ENA = 23
PIN_IN3 = 5
PIN_IN4 = 17
PIN_ENB = 16



motors = MotorControl(PIN_IN1, PIN_IN2, PIN_ENA, PIN_IN3, PIN_IN4, PIN_ENB)

motors.forward(100)
sleep(5)
motors.stop()


