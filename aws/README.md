# AWS Integration

This project includes a small AWS-based workflow to demonstrate cloud storage, event-driven processing, serverless execution, and monitoring.

## AWS Services Used

### Amazon S3

Amazon S3 is used as the cloud storage layer for vehicle sensor CSV files.

The project uses an S3 bucket containing an `incoming/` folder where the processed vehicle sensor CSV is uploaded.

Example:

vehicle-predictive-maintenance-2026-2147
- incoming/
  - vehicle_sensor_data_cleaned.csv

## AWS Lambda

AWS Lambda is used for serverless processing of vehicle data.

The project contains two Lambda implementations:

### 1. Vehicle Data Processor

`vehicle-predictive-maintenance-processor`

This Lambda is triggered when a CSV file is uploaded to the S3 bucket.

The function:
- Receives the S3 event
- Identifies the bucket and object
- Reads the uploaded CSV
- Processes the records
- Writes execution information to CloudWatch

The Lambda successfully processed 1,000 rows from the project dataset.

### 2. ML Inference / Maintenance Decision Lambda

`vehicle-predictive-maintenance-ml-inference`

A lightweight Lambda implementation was created for the AWS demonstration.

Instead of packaging the complete Scikit-learn runtime into Lambda, the function uses the same maintenance-condition logic used to generate the simulated maintenance labels.

This keeps the Lambda deployment lightweight and avoids exceeding the Lambda deployment package size limit.

## CloudWatch

CloudWatch is used to monitor Lambda execution through logs.

The logs help verify:
- S3 events were received
- The correct bucket and object were processed
- CSV records were processed
- Maintenance decisions were generated
- Application errors can be investigated

## IAM

Lambda execution permissions were configured using IAM.

The Lambda execution role includes permissions required for CloudWatch logging and S3 object access.

S3 object access was restricted to the project input location rather than granting unrestricted bucket access.

## AWS Region

The project resources were created in:

`eu-north-1` — Europe (Stockholm)

## Important ML Note

The Random Forest model was developed and evaluated locally using the simulated vehicle dataset.

The AWS Lambda component demonstrates the serverless processing and maintenance-decision workflow.

The current dataset and maintenance labels are simulated and should not be considered representative of real-world vehicle predictive-maintenance performance.