import pandas as pd

# Replace 'file1.csv' and 'file2.csv' with the actual file paths or names
data1 = pd.read_csv('../Tableau/the-streets-of-cape/data/streets.csv')
data2 = pd.read_csv('../Tableau/the-streets-of-cape/data/Valuation.csv')

# Display tcd Zalhe first few rows of each file to confirm they were loaded correctly
print("Data from file1.csv:")
print(data1.head())

print("\nData from file2.csv:")
print(data2.head())
# Standardize the column format by stripping extra spaces and converting to lowercase if needed
data1['address'] = data1['address'].str.strip().str.lower()
data2['AddressOne'] = data2['AddressOne'].str.strip().str.lower()

# Merge data1 and data2 on the columns 'address' and 'AddressOne'
merged_data = pd.merge(data1, data2, left_on='address', right_on='AddressOne', how='inner')

# Display the first few rows to check the merged result
print("Merged Data:")
print(merged_data.head())
column_names = merged_data.columns.tolist()
print("List of Column Names:")
print(column_names)
frequency_table = merged_data['LAST YR'].value_counts()

# Display the frequency table
print("Frequency Table for Value24:")
print(frequency_table)
merged_data= merged_data.rename(columns={'address':'Address', 'location/lat':'Lat', 'location/lng':'Lon', 'PID#':'pid', 'CHECK':'Check', 'NO#':'Num', 'STREET':'Street', 'ACCT#':'Acct', 'TOTAL ASSESS':'Value24', 'diff in value':'diff', 'Diff in assessment':'DiffA', 'TAXES':'Tax24', 'LAST YR':'Value23', 'LAST YR TAXES':'Tax23'})

column_names = merged_data.columns.tolist()
print("List of Column Names:")
print(column_names)
selected_data = merged_data[['Address', 'Lat', 'Lon', 'pid', 'Check', 'Value24', 'Tax24', 'Value23', 'Tax23']]
print(selected_data.head())
# Assuming columns are named 'Value' and 'Tax'
range_summary = merged_data[['Value24', 'Tax24', 'Value23', 'Tax23']].agg(['min', 'max'])

print("Range of Values in 'Value' and 'Tax' Columns:")
print(range_summary)
