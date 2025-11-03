from machine import Pin, time_pulse_us
from time import sleep

# Define pins
trig = Pin(12, Pin.OUT)
echo = Pin(23, Pin.IN)

def get_distance():
    # Trigger the sensor
    trig.value(0)
    sleep(0.000002)
    trig.value(1)
    sleep(0.00001)
    trig.value(0)
    
    try:
        # Measure pulse duration in microseconds
        duration = time_pulse_us(echo, 1, 30000)  # 30ms timeout
    except OSError:  # timeout, no echo received
        return None
    
    # Convert to distance in cm
    distance = (duration * 0.0343) / 2
    return distance, duration

def measure_surface(repeats=5):
    distances = []
    durations = []
    
    for _ in range(repeats):
        result = get_distance()
        if result:
            distance, duration = result
            distances.append(distance)
            durations.append(duration)
        sleep(0.05)
    
    if not distances:
        return None, None
    
    # Calculate average and standard deviation
    avg_distance = sum(distances) / len(distances)
    avg_duration = sum(durations) / len(durations)
    stdev_distance = (sum((x - avg_distance)**2 for x in distances)/len(distances))**0.5
    
    return avg_distance, stdev_distance

while True:
    avg_dist, stdev = measure_surface()
    
    if avg_dist is None:
        print("No echo detected!")
        sleep(0.5)
        continue
    
    # Simple heuristic:
    # Hard objects → low variation (stdev < ~0.5 cm)
    # Soft objects → higher variation (stdev > ~0.5 cm)
    if stdev < 0.5:
        material = "Hard"
    else:
        material = "Soft or foam"
    
    print("Distance: {:.2f} cm | Variation: {:.2f} | Material: {}".format(avg_dist, stdev, material))
    sleep(0.5)

