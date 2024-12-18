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
input("do you want to start?")

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
        return f"'{word}' is a valid word."
    else:
        return f"'{word}' is not a valid word."

word = input("Enter a word:").upper()

print(is_english_word(word))

# 516f08d3-804f-431f-8f03-e85b28a9c241
c = []
for letter, values in letter_data.items():
    quantity = values[1]
    c.extend([letter] * quantity)
len_c = len(c)
print("Expanded list c (letters):", c)
print("Length of c:", len_c)
#summary stats. length of string, string split, verify each letter is in the original set. 
letter = [x for x in word]
print("summary stats")
print("Letters in word:", letter)
print("Length of word:", len(letter))
handOneTempLen = [char for char in handOne]
print("Hand One length:", len(handOneTempLen))
print("Difference:", len(handOneTempLen) - len(letter))

handOne_letters = [char for char in handOne]

# Check if all characters in 'word' are in 'handOne_letters'
result = all(char in handOne_letters for char in word)

# Display result of comparison
print(f"Can '{word}' be formed with the letters in handOne ,aka,'{result}'?:", result)

print("Do you have another word to check? Y if yes N if no")
txt = "welcome"
print(txt)
result = list(txt)
print(result)
print(len(txt))
print(len(result))
