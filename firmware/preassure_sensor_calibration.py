from machine import ADC, Pin
from time import sleep

# --- ADC setup ---
scale_sensor = ADC(Pin(34))
scale_sensor.atten(ADC.ATTN_11DB)
scale_sensor.width(ADC.WIDTH_12BIT)

# --- Calibration constants ---
ADC_MIN = 120      # ADC reading at empty scale
ADC_MAX = 2850     # ADC reading at reference weight
GRAMS_MAX = 5000.0 # Reference weight in grams

def read_average(samples=10, delay_time=0.01):
    """Take multiple readings and return the average."""
    total = 0
    for _ in range(samples):
        total += scale_sensor.read()
        sleep(delay_time)
    return total / samples

def adc_to_grams(reading):
    """Convert ADC reading to grams."""
    reading = max(ADC_MIN, min(reading, ADC_MAX))
    return (reading - ADC_MIN) * GRAMS_MAX / (ADC_MAX - ADC_MIN)

def measure_weight(label):
    """Prompt user to place/pick weight 3 times and return average ADC value."""
    readings = []
    for i in range(3):
        input(f"Step {i+1}/3: Place the {label} on the scale and press Enter...")
        reading = read_average()
        readings.append(reading)
        input("Now pick it up and press Enter...")
    avg_reading = sum(readings) / len(readings)
    print(f"Average ADC value for {label}: {avg_reading:.0f}\n")
    return avg_reading

# --- Main script ---
print("Welcome to the weight calibration script!\n")

# Step 1: Light weight
light_avg = measure_weight("light foam ball")

# Step 2: Medium weight
medium_avg = measure_weight("medium weight object")

# Step 3: Heavy weight
heavy_avg = measure_weight("heavy weight object")

# Display ADC ranges for categories
print("Calibration complete! Here are the ADC ranges for each category:")
print(f"Low (light): 0 – {light_avg:.0f}")
print(f"Medium: {light_avg:.0f} – {medium_avg:.0f}")
print(f"High (heavy): {medium_avg:.0f} – {heavy_avg:.0f}")


