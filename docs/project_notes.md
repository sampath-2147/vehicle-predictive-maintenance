# Project Notes

## Day-1 

### What I learned ?

- I had a recap learning session of python fundamentals
- learned how and when to use loops and conditional statements
- lists, tuples, sets, and dictionaries
- Bsic project structure

### What I built

- Created a python script to generate simulated vehicle sensor dataset

### Dataset fields

- vehicle_id
- timestamp
- engine_temperature
- battery_voltage
- vibration
- brake_temperature
- speed
- mileage
- fault_code
- maintenance_required

### Note:
- The dataset is generate due to lack of access to real time sensor dataset.
- The dataset is designed to contain relationships between sensor conditions and maintenance requirements.

## Day-2

### What I learned

- how to import and use pandas, numpy
- Dataframe
- Data inspection
- sorting
- filtering
- groupby
- basics of EDA

### EDA Findings

Maintenance-labelled records generally showed:

- Higher engine temperature
- Higher vibration
- Higher brake temperature
- Lower battery voltage

### Output

Created:

`data/processed/vehicle_sensor_data_cleaned.csv`