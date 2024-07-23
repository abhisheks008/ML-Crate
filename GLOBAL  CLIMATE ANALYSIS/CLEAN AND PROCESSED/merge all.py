##Data Merging

## Merge GHG Emissions Data

##```python
import pandas as pd
# Load the data from CSV files
ch4_data = pd.read_csv('CH4_N2O_Emissions.csv')
co2_data = pd.read_csv('CO2_Emissions.csv')
merged_ghg_emissions_data=pd.read_csv('merged_ghg_data.csv')
NOx_data=pd.read_csv('NOx_Emissions.csv')
Ods_data=pd.read_csv('ODS_Consumption.csv')
SO2_data=pd.read_csv('SO2_emissions.csv')

# Merge the datasets on the 'Country' column with outer join
merged_data = ch4_data.merge(NOx_data, on='Country', how='outer')
merged_data = merged_data.merge(co2_data, on='Country', how='outer')
merged_data = merged_data.merge(merged_ghg_emissions_data, on='Country', how='outer')
merged_data = merged_data.merge(Ods_data, on='Country', how='outer')
merged_data = merged_data.merge(SO2_data, on='Country', how='outer')

# Fill missing values with 0
merged_data.fillna(0, inplace=True)

# Save the merged data to a new CSV file
merged_data.to_csv('merge.csv', index=False)

# View the merged data
print(merged_data.head())