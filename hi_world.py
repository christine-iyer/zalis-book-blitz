import csv
import pandas as pd
import random
import requests
import nltk
from nltk.corpus import words

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

def is_english_word(word):
    api_key = '516f08d3-804f-431f-8f03-e85b28a9c241'
    url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"
    response = requests.get(url)
    response_json = response.json()
    
    # Check if the first item in the response is a dictionary (indicating a valid word with definitions)
    if response_json and isinstance(response_json[0], dict):
        return True  # Word is valid
    else:
        return False  
word = input("Enter a word:").upper()



# def is_english_word(word):
#     api_key = '516f08d3-804f-431f-8f03-e85b28a9c241'
#     url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"
#     response = requests.get(url)
#     # If the word exists, the API returns a list of definitions. Otherwise, it suggests alternatives.
#     return bool(response.json())

# #this is not properly verifying if it's a word.
# respod = bool
print(is_english_word(word))
print('regarding its validity')
 # True if word is valid

# 516f08d3-804f-431f-8f03-e85b28a9c241

#summary stats. length of string, string split, verify each letter is in the original set. 
letter = [x for x in word]
print(letter)
print(len(letter))
print(len(handOne))
print(len(handOne)- len(letter))

handOne_letters = [char for card in handOne for char in card]

# Check if all characters in 'word' are in 'handOne_letters'
result = all(char in handOne_letters for char in word)

print(word) 
print(result)
