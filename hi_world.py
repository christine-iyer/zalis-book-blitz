import csv
import pandas as pd
import random
import requests

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
discard = []
# gonna want to add an input field. 
deal = input("Add a number 1-8: ")
deal = int(deal) + 2
# Deal 5 cards to each hand
for i in range(deal):
    handOne.append(letter_list.pop())  # Deal card to handOne
    handTwo.append(letter_list.pop())  # Deal card to handTwo

# Print the hands after dealing all cards
print("Hand One:")
for card in handOne:
    print(card)

print("Hand Two:")
for card in handTwo:
    print(card)

print("Dicard Pile: ")
discard.append(letter_list.pop()) 
print(card)

# Hand One input a word
word = input("Enter a word:")



def is_english_word(word):
    api_key = '516f08d3-804f-431f-8f03-e85b28a9c241'
    url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"
    response = requests.get(url)
    # If the word exists, the API returns a list of definitions. Otherwise, it suggests alternatives.
    return bool(response.json())

user_input = "apple"
print(is_english_word(user_input))  # True if word is valid

# 516f08d3-804f-431f-8f03-e85b28a9c241

