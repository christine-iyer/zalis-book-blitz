import csv
import pandas as pd
import random

# Initialize letter_data dictionary
letter_data = {}

# Read CSV file and populate letter_data dictionary
with open('quid_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        letter = row['Letter']
        points = int(row['Points'])
        quantity = int(row['Quantity'])
        letter_data[letter] = {'Points': points, 'Quantity': quantity}

# Create DataFrame from letter_data dictionary
df = pd.DataFrame.from_dict(letter_data, orient='index', columns=['Points', 'Quantity'])

# Print the DataFrame column "Quantity"
print(df["Quantity"])

# Convert the dictionary into a list of tuples (letter, points, quantity)
letter_list = [(letter, data['Points'], data['Quantity']) for letter, data in letter_data.items()]

# Shuffle the list of letter cards
random.shuffle(letter_list)

# Print the shuffled list of letter cards
print("Shuffled letter cards:")
for card in letter_list:
    print(card)

# Initialize empty lists to represent each hand
handOne = []
handTwo = []

# Deal 5 cards to each hand
for i in range(5):
    handOne.append(letter_list.pop())  # Deal card to handOne
    handTwo.append(letter_list.pop())  # Deal card to handTwo

# Print the hands after dealing all cards
print("Hand One:")
for card in handOne:
    print(card)

print("Hand Two:")
for card in handTwo:
    print(card)
