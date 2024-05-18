# Election Result Aggregator

## Project Overview
The Election Result Aggregator is a data processing pipeline designed to analyze U.S. presidential election data from 1976 to 2020. The project extracts data, transforms it for uniformity and clarity, and loads it into a MySQL database for aggregation. The system then uses SQL procedures to provide insights into national and state-level election results.

## Features
- **Data Standardization**: Standardizes candidate names and party affiliations.
- **Data Aggregation**: Aggregates total votes by party and candidate at both national and state levels.
- **Reporting**: Supports basic reporting and visualization of aggregated data.

## Prerequisites
- Python 3.x
- MySQL Server
- Python libraries: pandas, sqlalchemy, matplotlib (for visualization)
- MySQL connector for Python (mysql-connector-python or pymysql)

## Installation

### Database Setup
1. Install MySQL Server and ensure it is running.
2. Create a new database for the project:
   ```sql
   CREATE DATABASE election_data;
   USE election_data;
   ```

