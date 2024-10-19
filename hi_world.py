import pandas as pd
print("This random py file does not serve any particular purpose, other \nthan reflects my first py file. And so many firsts...\nFirst time executing python files from my own VS. \nIt happens to be in the Zali's stuff \nfolder because she and I will both be learning python as part \nof our mentorship. \nHi Listening rn, will call later. \nBut you can certainly get started. \nOne of the forist rules is this one: \n'Stop and think!'!")
# Read the CSV into a DataFrame
df = pd.read_csv('quid_data.csv')

# Convert the DataFrame to a dictionary with the 'Letter' column as keys and tuples for (Point value, Quantity)
letter_data = df.set_index('Letter').T.to_dict('index')['Point value']

# Alternatively, you can convert it to the exact same format as the csv approach
letter_data = df.set_index('Letter').apply(lambda x: (x['Point value'], x['Quantity']), axis=1).to_dict()

# Print or use the dictionary
print(letter_data)