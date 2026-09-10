#count of total number of records
SELECT COUNT(*) FROM vehicle_sensor_data;

#check for missing values
-- vehicle_id 
SELECT COUNT(*)
FROM vehicle_sensor_data
WHERE vehicle_id IS NULL;

-- engine_temperature
SELECT COUNT(*)
FROM vehicle_sensor_data
WHERE engine_temperature IS NULL;

-- battery_voltage
SELECT COUNT(*)
FROM vehicle_sensor_data
WHERE battery_voltage IS NULL;

-- vibration
SELECT COUNT(*)
FROM vehicle_sensor_data
WHERE vibration IS NULL;

-- fault_code
SELECT COUNT(*)
FROM vehicle_sensor_data
WHERE fault_code IS NULL;

-- timestamp
SELECT COUNT(*)
FROM vehicle_sensor_data
WHERE timestamp IS NULL;

-- brake_temperature
SELECT COUNT(*)
FROM vehicle_sensor_data
WHERE brake_temperature IS NULL;

-- speed
SELECT COUNT(*)
FROM vehicle_sensor_data
WHERE speed IS NULL;

-- mileage
SELECT COUNT(*)
FROM vehicle_sensor_data
WHERE mileage IS NULL;

-- maintenance_required
SELECT COUNT(*)
FROM vehicle_sensor_data
WHERE maintenance_required IS NULL;

# checking duplicates in dataset 

SELECT vehicle_id, timestamp, COUNT(*)
FROM vehicle_sensor_data
GROUP BY vehicle_id, timestamp
HAVING COUNT(*) > 1;

# categorical data validation
-- fault_code
SELECT DISTINCT fault_code
FROM vehicle_sensor_data;

-- maintenance_required
SELECT DISTINCT maintenance_required
FROM vehicle_sensor_data;