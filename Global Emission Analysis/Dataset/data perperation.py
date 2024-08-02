import pandas as pd
import numpy as np

# Load the CSV data into a pandas DataFrame
data = pd.read_csv('merge.csv')

# Replace 0 with NaN
data.replace(0, np.nan, inplace=True)

# Display the first few rows of the DataFrame
print(data.head())

# Handle missing values, if any
# For simplicity, we'll drop rows with missing values, but you could also fill them
data = data.dropna()

# Convert columns to appropriate data types if necessary
data['latest year available_x'] = data['latest year available_x'].astype(int)

# Save cleaned data for later use
data.to_csv('cleaned_data.csv', index=False)



