import csv
import pandas as pd
import random
letter_data = {}
with open('quid_data.csv', mode='r') as file:
     reader = csv.DictReader(file)
     for row in reader:
          letter = row['Letter']
          points=int(row['Points']) 
          quantity= int(row['Quantity'])
          letter_data[letter] ={'Points': points, 'Quantity': quantity}

print(letter_data['W'])          

df = pd.DataFrame.from_dict(letter_data, orient='index', columns=['Points', 'Quantity'])

# Print the DataFrame as a table
print(df["Quantity"])

#draw a random card
letter_data[letter] = {'Points': points, 'Quantity': quantity}

# Convert the dictionary into a list of tuples (letter, points, quantity)
letter_list = [(letter, data['Points'], data['Quantity']) for letter, data in letter_data.items()]

# Shuffle the list in place
random.shuffle(letter_list)

# Print the shuffled list of letter cards
print("Shuffled letter cards:")
for card in letter_list:
    print(card)