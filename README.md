 # Vehicle-predictive-maintenance

---

 ## 1. Project Overview

Vehicle-predictive-maintenance is a prototype project for a critical problem faced by many vehicle owners/drivers which sometimes may cost huge money and may also lead to accidents.

The main issue which this project is trying to solve is predicting maintenance of a vehicle before a simple issue turn into a major issue which can cause a huge impact later based on historical/stimulated data.

---
## 2.Business Problem

A vehicle can develop a problem before the driver or the maintenance team realize that a vehicle is developing.

So, the actual business problem is "Which vehicles are likely to require maintenance so that my team can inspect them before a serious failure occurs?"

---
## 3. Objective

The objective is to identify whether a vehicle may require maintenance before it breakdown and cause trouble for the driver or the maintenance team to identify the issue.

To avoid the following impacts by a delay -
- vehicle downtime
- Unexpected repair costs
- Operational delays
- Safety concerns
- Lost productivity

---
## 4. Proposed Solution

The proposed solution is to extract data collected from vehicle sensors in a structured format then clean and validate the data using python and then use relavent sensor readings to predict whether the maintenance may be required.

---
## 5. Dataset

This project uses simulated vehicle sensor data generated using Python.

The dataset represents structured vehicle telemetry containing parameters such as engine temperature, battery voltage, vibration, brake temperature, speed, mileage, fault codes, and maintenance status.

The data was generated with predefined conditions to create a maintenance-required label. The dataset is used to demonstrate the complete predictive maintenance workflow.

> Note: The dataset is simulated and does not represent real-world vehicle telemetry.

---
## 6. Data Processing

The generated dataset was loaded and analyzed using Pandas and NumPy.

The following data quality checks were performed:

- Checked data types
- Checked missing values
- Checked duplicate records
- Validated sensor value ranges
- Converted timestamp values to datetime
- Filtered and sorted records for analysis

The processed dataset was saved separately in the `data/processed/` directory.

---
## 7. Exploratory Data Analysis

Basic exploratory analysis was performed to understand the relationship between vehicle sensor readings and maintenance requirements.

The analysis showed that observations labelled as requiring maintenance generally had:

- Higher engine temperature
- Higher vibration
- Higher brake temperature
- Slightly lower battery voltage

These observations will be considered when selecting features for the machine learning stage.

---
