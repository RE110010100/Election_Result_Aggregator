import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine
import time

# Start the timer for the entire ETL process
start_time = time.time()


# MySQL connection string (update username, password, host, and database name)
engine = create_engine('mysql+mysqlconnector://root:rohan123@localhost/Election_Results')

# Loading the dataset (Extraction)
load_start = time.time()
# Load the dataset
data = pd.read_csv('1976-2020-president.csv')
load_duration = time.time() - load_start

# Data transformation
transform_start = time.time()
# Normalize party names
party_mapping = {
    'DEMOCRAT': 'DEMOCRATIC',
    'REPUBLICAN': 'REPUBLICAN',
    # Assume all others are minor parties or independents
}
data['party_simplified'] = data['party_detailed'].map(party_mapping).fillna('OTHER')

# Standardize candidate names
data['candidate'] = data['candidate'].str.upper().replace('[^A-Z ]', '', regex=True)
transform_duration = time.time() - transform_start

# Loading data into MySQL (Loading)
load_db_start = time.time()
# Load transformed data into MySQL
data.to_sql('election_data', con=engine, if_exists='replace', index=False, chunksize=500)

load_db_duration = time.time() - load_db_start

# End the timer for the entire ETL process
total_duration = time.time() - start_time

print(f"Total ETL Time: {total_duration}s")
print(f"Data Load Time: {load_duration}s")
print(f"Data Transformation Time: {transform_duration}s")
print(f"Database Load Time: {load_db_duration}s")




