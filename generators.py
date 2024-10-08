import random
import time

# Genearte random temperature readings from a sensor
def generate_sensor_data():
    while True:
        # Generate random temperature between 10 and 25 on at a time using yield function
        yield random.uniform(10.0, 25.0)  
        # delay 1s between readings
        time.sleep(1)  

# Process the infinite stream of sensor data
for data in generate_sensor_data():
    print(f"Sensor reading: {data}")
    if data > 20.5:
        print("Warning: High temperature!")
