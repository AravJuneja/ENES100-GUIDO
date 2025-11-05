from machine import Pin, PWM
from time import sleep

# ===== DC Motor Control Class =====
class DCMotor:
    def __init__(self, pin1, pin2, enable_pin, min_duty=750, max_duty=1023):
        self.pin1 = pin1
        self.pin2 = pin2
        self.enable_pin = enable_pin
        self.min_duty = min_duty
        self.max_duty = max_duty
        self.speed = 0

    def forward(self, speed):
        self.speed = speed
        self.enable_pin.duty(self._duty_cycle(self.speed))
        self.pin1.value(1)
        self.pin2.value(0)

    def stop(self):
        self.enable_pin.duty(0)
        self.pin1.value(0)
        self.pin2.value(0)

    def _duty_cycle(self, speed):
        if speed <= 0 or speed > 100:
            return 0
        return int(self.min_duty + (self.max_duty - self.min_duty) * ((speed - 1) / (100 - 1)))

# ===== Pin Configuration =====
FREQUENCY = 15000  # PWM frequency (Hz)

PIN_IN1 = 19   # L298N IN1
PIN_IN2 = 18   # L298N IN2
PIN_ENA = 23   # L298N ENA (PWM)

# ===== Initialize Pins =====
in1 = Pin(PIN_IN1, Pin.OUT)
in2 = Pin(PIN_IN2, Pin.OUT)
ena = PWM(Pin(PIN_ENA), freq=FREQUENCY)

# ===== Create Motor Object =====
motor = DCMotor(in1, in2, ena)

# ===== Run Motor =====
print("Motor running forward at 100% speed for 5 seconds...")
motor.forward(100)
sleep(5)

print("Stopping motor.")
motor.stop()

print("Done ✅")

