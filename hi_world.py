import csv
import pandas as pd
letter_data = {}
with open('quid_data.csv', mode='r') as file:
     reader = csv.DictReader(file)
     for row in reader:
          letter = row['Letter']
          points=int(row['Points']) 
          quantity= int(row['Quantity'])
          letter_data[letter] = (points, quantity)

print(letter_data)          

df = pd.DataFrame.from_dict(letter_data, orient='index', columns=['Points', 'Quantity'])

# Print the DataFrame as a table
print(df)