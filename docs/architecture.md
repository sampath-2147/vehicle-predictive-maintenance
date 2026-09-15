# System Architecture

## Overview

The Vehicle Predictive Maintenance project combines data generation, data processing, SQL analysis, machine learning, and AWS services into a small end-to-end prototype.

## Overall Flow

                    ANALYTICAL PATH
                         
Python → Pandas → MySQL → Power BI → User
                  |
                  ↓
                 SQL


                    ML PATH

Processed Data → Random Forest → Prediction


                    CLOUD PATH

CSV → S3 → Lambda → CloudWatch
## Component Responsibilities

### Python

Python is used to generate the simulated vehicle sensor dataset and perform data processing.

### Pandas and NumPy

Pandas and NumPy are used for data inspection, cleaning, validation, transformation, and exploratory analysis.

### MySQL

MySQL provides relational storage and allows SQL-based data validation and analysis.

### Machine Learning

A Random Forest Classifier is used as the initial machine-learning model for binary classification of maintenance requirements.

### Amazon S3

S3 provides cloud object storage for vehicle sensor CSV files.

### AWS Lambda

Lambda provides event-driven serverless processing when a file is uploaded to S3.

### CloudWatch

CloudWatch provides logging and monitoring for Lambda execution.

## Current Prototype Boundary

The machine-learning model is developed and evaluated locally.

The AWS Lambda component currently uses lightweight maintenance-condition evaluation rather than loading the complete Scikit-learn runtime.

This design was chosen to keep the AWS deployment lightweight while still demonstrating the cloud processing architecture.

## Production Extension

With real vehicle telemetry and historical maintenance records, the architecture could be extended with:

- production data ingestion
- stronger data validation
- centralized model training
- model versioning
- scalable inference
- alerting and notification
- database integration
- failure handling and retry mechanisms