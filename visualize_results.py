import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine

# Execute SQL query
query = "SELECT party, total_votes FROM national_results WHERE year = 2020;"
result = pd.read_sql(query, con=engine)

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(result['party'], result['total_votes'], color='blue')
plt.xlabel('Party')
plt.ylabel('Total Votes')
plt.title('2020 National Election Results by Party')
plt.show()