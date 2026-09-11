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

## Day 3 — SQL and Database

### What I Learned

- Database vs DBMS
- MySQL database and table structure
- Primary key and auto-increment
- SQL data types
- Data import from CSV into MySQL
- Data validation using SQL
- SQL aggregation and analysis
- Preparing data for machine learning

### What I Built

Created a MySQL database:

`vehicle_maintenance_db`

Created the main table:

`vehicle_sensor_data`

The table stores vehicle telemetry including:

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

A `record_id` was used as the primary key with auto-increment.

### Data Import

Imported the processed vehicle dataset from CSV into MySQL.

Verified that the table contains 1,000 records.

### Data Validation

Created SQL validation queries to check:

- Total record count
- NULL values
- Duplicate vehicle/timestamp combinations
- Valid categorical values

No NULL values or duplicate vehicle/timestamp combinations were found in the current dataset.

### SQL Analysis

Created queries to analyze:

- Maintenance-required vs normal records
- Maintenance percentage
- Average sensor values per vehicle
- Maintenance-focused sensor averages
- Vehicles with higher maintenance counts
- Fault-code frequency
- Maintenance records by fault code
- Combined vehicle-level metrics

### ML Data Extraction

Created a separate SQL script to extract candidate features for the machine learning stage.

The target variable is:

`maintenance_required`

Vehicle identifiers were excluded from the ML feature set because they are identifiers rather than meaningful predictive measurements.

## Day 4 — Machine Learning

### What I Learned

- Machine learning basics
- Supervised learning
- Binary classification
- Features and target
- One-hot encoding
- Train/test split
- Random Forest classification
- Model prediction
- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- Feature importance
- Model serialization

### ML Problem

The project uses supervised binary classification to predict:

`maintenance_required`

Target values:

- `0` → No maintenance required
- `1` → Maintenance required

### Features

The candidate features used by the model were:

- engine_temperature
- battery_voltage
- vibration
- brake_temperature
- speed
- mileage
- fault_code

The `fault_code` feature was converted using one-hot encoding.

### Train/Test Split

The dataset was divided into:

- 80% training data
- 20% testing data

`random_state=42` was used for reproducibility and `stratify=y` was used to maintain the target-class distribution.

### Model

A Random Forest Classifier was used as the initial machine learning model.

The model was trained using the training dataset and then evaluated on the unseen test dataset.

### Model Evaluation

The current model achieved:

- Accuracy: 1.00
- Precision: 1.00
- Recall: 1.00
- F1-score: 1.00

Confusion matrix:

```text
[[125   0]
 [  0  75]]