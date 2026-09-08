import random
import pandas as pd
from datetime import datetime, timedelta

vehicles = ["VH001", "VH002", "VH003", "VH004", "VH005"]

start_time = datetime(2026, 9, 8, 9, 0, 0)

vehicle_data = []

for i in range(1000):

    vehicle_id = random.choice(vehicles)

    timestamp = start_time + timedelta(minutes=i * 5)

    engine_temperature = round(random.uniform(80, 110), 2)
    battery_voltage = round(random.uniform(11.5, 13.0), 2)
    vibration = round(random.uniform(1, 9), 2)
    brake_temperature = round(random.uniform(60, 120), 2)
    speed = random.randint(20, 100)
    mileage = random.randint(10000, 100000)
    fault_code = random.choice(["F000", "F001", "F002"])

    warning_count = 0

    if engine_temperature > 100:
        warning_count += 1

    if battery_voltage < 12:
        warning_count += 1

    if vibration > 7:
        warning_count += 1

    if brake_temperature > 100:
        warning_count += 1

    if warning_count >= 2:
        maintenance_required = "Yes"
    else:
        maintenance_required = "No"

    vehicle_data.append({
        "vehicle_id": vehicle_id,
        "timestamp": timestamp,
        "engine_temperature": engine_temperature,
        "battery_voltage": battery_voltage,
        "vibration": vibration,
        "brake_temperature": brake_temperature,
        "speed": speed,
        "mileage": mileage,
        "fault_code": fault_code,
        "maintenance_required": maintenance_required
    })

print(vehicle_data[:5])
df = pd.DataFrame(vehicle_data)

df.to_csv(
    "data/raw/vehicle_sensor_data.csv",
    index=False
)

print("Dataset created successfully.")
print(df.head())