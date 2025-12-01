from machine import Pin, PWM
from time import sleep

class MotorControl:
    def __init__(self, 
                 in1, in2, ena, 
                 in3, in4, enb, 
                 min_duty=750, max_duty=1023, freq=15000):

        # Motor A pins
        self.in1 = Pin(in1, Pin.OUT)
        self.in2 = Pin(in2, Pin.OUT)
        self.ena = PWM(Pin(ena), freq=freq)

        # Motor B pins
        self.in3 = Pin(in3, Pin.OUT)
        self.in4 = Pin(in4, Pin.OUT)
        self.enb = PWM(Pin(enb), freq=freq)

        self.min_duty = min_duty
        self.max_duty = max_duty

    def _duty_cycle(self, speed):
        if speed <= 0 or speed > 100:
            return 0
        return int(self.min_duty + (self.max_duty - self.min_duty) * ((speed - 1) / 99))

    def forward_A(self, speed):
        self.ena.duty(self._duty_cycle(speed))
        self.in1.value(1)
        self.in2.value(0)

    def forward_B(self, speed):
        self.enb.duty(self._duty_cycle(speed))
        self.in3.value(1)
        self.in4.value(0)

    def forward(self, speed):
        self.forward_A(speed)
        self.forward_B(speed)

    def stop(self):
        self.ena.duty(0)
        self.enb.duty(0)
        self.in1.value(0)
        self.in2.value(0)
        self.in3.value(0)
        self.in4.value(0)


# ===== MAIN PROGRAM =====
if __name__ == "__main__":
    # Update these pin numbers as needed
    PIN_IN1 = 19
    PIN_IN2 = 18
    PIN_ENA = 23
    PIN_IN3 = 5
    PIN_IN4 = 17
    PIN_ENB = 16

    motors = MotorControl(PIN_IN1, PIN_IN2, PIN_ENA,
                          PIN_IN3, PIN_IN4, PIN_ENB)

    print("Moving forward for 5 seconds...")
    motors.forward(100)
    sleep(5)

    print("Stopping motors...")
    motors.stop()

    print("Done.")
