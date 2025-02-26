
# Data Pipeline with Reddit, Python, Docker, and Airflow, integrating AWS Glue, S3, and Redshift

A scalable ETL pipeline for Reddit data using Python, Docker, and Airflow, integrating AWS Glue, S3, and Redshift for efficient data extraction, transformation, and storage. This pipeline automates data ingestion from Reddit, processes it using Glue, and loads it into Redshift for analytics and insights.


## Table of Contents

- Overview
- Architecture
- Prerequisites
- System Setup
- Project Demo

## Overview

The pipeline is designed to:

- Extract data from Reddit using its API.
- Store the raw data into an S3 bucket from Airflow.
- Transform the data using AWS Glue.
- Load the transformed data into Amazon Redshift for analytics and querying.

## Architecture

    ![Project Architecture](RedditDataPipeline-Architecture.png)

- Reddit API: Source of the data.
- Apache Airflow & Celery: Orchestrates the ETL process and manages task distribution.
- PostgreSQL: Temporary storage and metadata management.
- Amazon S3: Raw data storage.
- AWS Glue: Data cataloging and ETL jobs.
- Amazon Redshift: Data warehousing and analytics.

## Prerequisites

- AWS Account with appropriate permissions for S3, Glue, Athena, and Redshift.
- Reddit API credentials.
- Docker Installation
- Python 3.9 or higher

## System Setup
- Clone the repository

    
        git clone https://github.com/aadidubey7/RedditDataEngineering.git
        
- Create a virtual environment
        
        python3 -m venv .venv

- Activate the virtual environment

        .\.venv\Scripts\activate

- Install the dependencies

        pip install -r requirements.txt

- Add your credentials in the utils/conf.py file. However, storing credentials in a file is not recommended. Instead, use environment variables for better security.

- Starting the containers
        
        docker-compose up -d

- Launch the Airflow web UI.

        open http://localhost:8080

## Project Demo
