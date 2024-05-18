import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine

# MySQL connection string (update username, password, host, and database name)
engine = create_engine('mysql+mysqlconnector://root:rohan123@localhost/Election_Results')

# Load the dataset
data = pd.read_csv('1976-2020-president.csv')

# Normalize party names
party_mapping = {
    'DEMOCRAT': 'DEMOCRATIC',
    'REPUBLICAN': 'REPUBLICAN',
    # Assume all others are minor parties or independents
}
data['party_simplified'] = data['party_detailed'].map(party_mapping).fillna('OTHER')

# Standardize candidate names
data['candidate'] = data['candidate'].str.upper().replace('[^A-Z ]', '', regex=True)

# Load transformed data into MySQL
data.to_sql('election_data', con=engine, if_exists='replace', index=False, chunksize=500)



