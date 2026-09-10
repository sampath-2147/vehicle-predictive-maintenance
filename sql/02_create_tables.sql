# create tabel inside the database
CREATE table vehicle_sensor_data (
record_id int auto_increment primary key, 
vehicle_id VARCHAR(20),
time_stamp datetime,
engine_temperature decimal(5,2),
battery_voltage decimal(5,2),
vibration decimal(5,2),
brake_temperature decimal(5,2),
speed int,
mileage int,
fault_code varchar(20),
maintenance_required varchar(10) );

#rename column with wrong name
ALTER TABLE vehicle_sensor_data 
RENAME COLUMN time_stamp TO timestamp;

