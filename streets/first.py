import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data1 = pd.read_csv('full-data.csv')
# print('Finding null values:')
# print(data1[data1['Tax24'].isnull()])
#data1 = pd.read_csv('../Tableau/the-streets-of-cape/data/cape_streets.csv')
# data2 = pd.read_csv('../Tableau/the-streets-of-cape/data/Valuation.csv')

# Display first few rows of each file to confirm they were loaded correctly
print("Data from file1.csv:")
print(data1.head())
print(data1.columns)
# Standardize the column format by stripping extra spaces and converting to lowercase if needed
# #data1['Address'] = data1['Address'].str.strip().str.lower()
# # Merge data1 and data2 on the columns 'address' and 'AddressOne'
# # merged_data = pd.merge(data1, data2, left_on='address', right_on='AddressOne', how='inner')
# # column_names = merged_data.columns.tolist()
# column_names = data1.columns.tolist()
frequency_table = data1['Value24'].value_counts()

# # Display the frequency table
print("Frequency Table for Value24:")
print(frequency_table)
# merged_data= data1.rename(columns={'address':'Address', 'location/lat':'Lat', 'location/lng':'Lon', 'PID#':'pid', 'CHECK':'Check', 'NO#':'Num', 'STREET':'Street', 'ACCT#':'Acct', 'TOTAL ASSESS':'Value24', 'diff in value':'diff', 'Diff in assessment':'DiffA', 'TAXES':'Tax24', 'LAST YR':'Value23', 'LAST YR TAXES':'Tax23'})

# column_names = merged_data.columns.tolist()
# print("List of Column Names:")
# print(column_names)
# selected_data = merged_data[['Address', 'Lat', 'Lon', 'pid', 'Check', 'Value24', 'Tax24', 'Value23', 'Tax23']]
# print(selected_data.head())
# # Assuming columns are named 'Value' and 'Tax'
range_summary = data1[['Value24', 'Tax24', 'Value23', 'Tax23']].agg(['average'])

print("Range of Values in 'Value' and 'Tax' Columns:")
print(range_summary)
# print(selected_data.dtypes)
# print(selected_data['Value24'].describe)
# print(int(selected_data['Value24'][0]))

# List of columns to plot
value_columns = ['Value23', 'Value24', 'Tax23', 'Tax24']

# Plot histograms for each column
for column in value_columns:
    plt.figure(figsize=(8, 6))
    plt.hist(data1[column], bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Histogram of {column} (Entire Dataset)')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()


def plot_neighborhood_distributions(df):
    # Set the style for better visualization
#     plt.style.use('seaborn')
    
    # Create a figure with 4 subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Distribution by Neighborhood', fontsize=16, y=1.02)
    
    # Flatten axes array for easier iteration
    axes = axes.ravel()
    
    # Data to plot
    plot_data = [
        ('Value23', 'Property Values 2023'),
        ('Value24', 'Property Values 2024'),
        ('Tax23', 'Property Tax 2023'),
        ('Tax24', 'Property Tax 2024')
    ]
    
    # Create boxplots for each metric
    for idx, (column, title) in enumerate(plot_data):
        sns.boxplot(data=df, x='Neighborhood', y=column, ax=axes[idx])
        
        # Customize each subplot
        axes[idx].set_title(title)
        axes[idx].set_xlabel('Neighborhood')
        axes[idx].tick_params(axis='x', rotation=45)
        axes[idx].set_ylabel(f'{title} ($)')
        
        # Add grid for better readability
        axes[idx].grid(True, linestyle='--', alpha=0.7)
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    
    return fig

# Example usage:

fig = plot_neighborhood_distributions(data1)
plt.show()
fig.savefig('neighborhood_distributions.png', dpi=300, bbox_inches='tight')
# Group by Neighborhood and plot histograms for each neighborhood
neighborhoods = data1['Neighborhood'].unique()

for neighborhood in neighborhoods:
    neighborhood_data = data1[data1['Neighborhood'] == neighborhood]
    
    for column in value_columns:
        plt.figure(figsize=(8, 6))
        plt.hist(neighborhood_data[column], bins=20, color='lightcoral', edgecolor='black')
        plt.title(f'Histogram of {column} - {neighborhood} Neighborhood')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()
