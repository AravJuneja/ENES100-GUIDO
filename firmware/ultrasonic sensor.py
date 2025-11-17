from machine import Pin, time_pulse_us
import time

# Pin configuration (change if needed)
TRIG_PIN = 14
ECHO_PIN = 12

trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

def get_distance():
    # Make sure trigger is low
    trig.value(0)
    time.sleep_us(2)

    # Send a 10 µs trigger pulse
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    # Measure the echo pulse length
    try:
        duration = time_pulse_us(echo, 1, 30000)  # 30 ms timeout
    except OSError as ex:
        # If no pulse is received within timeout
        return None

    # Calculate distance in cm (speed of sound = 343 m/s)
    distance_cm = (duration / 2) * 0.0343
    return distance_cm

# Main loop
while True:
    dist = get_distance()
    if dist is None:
        print("Out of range")
    else:
        print("Distance: {:.2f} cm".format(dist))
    time.sleep(1)

