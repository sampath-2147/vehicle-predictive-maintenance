import json


def lambda_handler(event, context):

    print("Vehicle maintenance inference started")

    vehicle = event["vehicle"]

    engine_temperature = float(vehicle["engine_temperature"])
    battery_voltage = float(vehicle["battery_voltage"])
    vibration = float(vehicle["vibration"])
    brake_temperature = float(vehicle["brake_temperature"])

    warning_count = 0

    if engine_temperature > 100:
        warning_count += 1

    if battery_voltage < 12:
        warning_count += 1

    if vibration > 7:
        warning_count += 1

    if brake_temperature > 100:
        warning_count += 1

    maintenance_required = "Yes" if warning_count >= 2 else "No"

    result = {
        "vehicle_id": vehicle["vehicle_id"],
        "maintenance_required": maintenance_required,
        "warning_count": warning_count
    }

    print(f"Prediction result: {result}")

    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }