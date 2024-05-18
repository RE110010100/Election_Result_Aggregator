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
### Python Environment Setup
1. Ensure Python is installed on your machine.
2. Install required Python libraries:
   ```bash
   pip install pandas sqlalchemy matplotlib mysql-connector-python
   ```
### Clone the Repository
```bash
git clone https://your-repository-url.git
cd your-project-directory
```
## Usage

### Loading the Data

1. Place the 1976-2020-president.csv data file in the project directory.
2. Run the Python script to load and transform the data
```bash
python extract_transform_election_data.py
```

### Creating Database Tables and Running Procedures
1. Execute the SQL scripts to create the necessary database tables:

```bash
mysql -u username -p database_name < create_tables.sql
```

2. Run the procedures to aggregate the data:
```bash
mysql -u username -p database_name < procedures.sql
```

### Querying and Reporting

1. Use SQL queries to fetch aggregated data from MySQL for analysis or reporting.
2. Optionally, run the Python visualization script to view graphical representations of the data:

```bash
python visualize_results.py
```

### Files Included

1. extract_transform_election_data.py: Script for loading and transforming election data.
2. create_tables.sql: SQL script for creating database tables.
3. procedures.sql: SQL script for inserting and aggregating data.
4. visualize_results.py: Python script for data visualization (optional).






