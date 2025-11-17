from machine import Pin, PWM
from time import sleep

# ===== Dual DC Motor Control Class =====
class MotorControl:
    def __init__(self, 
                 in1, in2, ena, 
                 in3, in4, enb, 
                 min_duty=750, max_duty=1023, freq=15000):
        # --- Motor A Pins ---
        self.in1 = Pin(in1, Pin.OUT)
        self.in2 = Pin(in2, Pin.OUT)
        self.ena = PWM(Pin(ena), freq=freq)
        DualDCMotor
        # --- Motor B Pins ---
        self.in3 = Pin(in3, Pin.OUT)
        self.in4 = Pin(in4, Pin.OUT)
        self.enb = PWM(Pin(enb), freq=freq)

        # --- Motor Speed Range ---
        self.min_duty = min_duty
        self.max_duty = max_duty

    # ===== Internal Helper =====
    def _duty_cycle(self, speed):
        """Convert 0–100% speed to PWM duty value."""
        if speed <= 0 or speed > 100:
            return 0
        return int(self.min_duty + (self.max_duty - self.min_duty) * ((speed - 1) / (100 - 1)))

    # ===== Motor A Control =====
    def forward_A(self, speed):
        self.ena.duty(self._duty_cycle(speed))
        self.in1.value(1)
        self.in2.value(0)

    def backward_A(self, speed):
        self.ena.duty(self._duty_cycle(speed))
        self.in1.value(0)
        self.in2.value(1)

    def stop_A(self):
        self.ena.duty(0)
        self.in1.value(0)
        self.in2.value(0)

    # ===== Motor B Control =====
    def forward_B(self, speed):
        self.enb.duty(self._duty_cycle(speed))
        self.in3.value(1)
        self.in4.value(0)

    def backward_B(self, speed):
        self.enb.duty(self._duty_cycle(speed))
        self.in3.value(0)
        self.in4.value(1)

    def stop_B(self):
        self.enb.duty(0)
        self.in3.value(0)
        self.in4.value(0)

    def turnTo(theta):
        pass

    def forward(self, speed):
        """Run both motors forward."""
        self.forward_A(speed)
        self.forward_B(speed)

    def backward(self, speed):
        """Run both motors backward."""
        self.backward_A(speed)
        self.backward_B(speed)

        

    def turn

    def stop(self):
        """Stop both motors."""
        self.stop_A()
        self.stop_B()


if __name__ == "__main__":
    # Pin configuration (adjust to match your wiring)
    PIN_IN1 = 19
    PIN_IN2 = 18
    PIN_ENA = 23
    PIN_IN3 = 5
    PIN_IN4 = 17
    PIN_ENB = 16

    motors = DualDCMotor(PIN_IN1, PIN_IN2, PIN_ENA, PIN_IN3, PIN_IN4, PIN_ENB)

    print("Running both motors forward at 100% for 5 seconds...")
    motors.forward(100)
    sleep(5)

    print("Stopping both motors.")
    motors.stop()

    print("Done ✅")
