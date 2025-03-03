"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jiří Beneš
email: Beneji125@gmail.com
"""

import re

import pprint

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30 and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users = {"bob": "123",
         "ann": "pass123",
         "mike": "password123",
         "liz": "pass123"}

username = input("username: ")
password = input("password: ")

print("-"*65)

if username in users and users[username] == password:
    print(f"Welcome to the app, {username}!")
    print(f"We have {len(TEXTS)} texts that can be analyzed")
    print("-"*65)
    TEXT_NUMBER = int(input("Please enter a number of the text you would like to analyze: "))
    print("-"*65)

    if TEXT_NUMBER > 0 and TEXT_NUMBER <= (len(TEXTS)):
        VYBRANY_TEXT = TEXTS[TEXT_NUMBER - 1]
        print(f"TEXT_{TEXT_NUMBER}: {VYBRANY_TEXT}")
        print("-"*65)

        TEXT_VYCISTENY_ROZDELENY = re.sub(r'[.,!?":;\'()-]', ' ', VYBRANY_TEXT).split()

        POCET_SLOV = []
        TEXT_POUZE_CISLA = []
        TEXT_POUZE_CISLA_SOUCET = []
        TITLECASE_COUNT = []
        UPPERCASE_COUNT = []
        LOWERCASE_COUNT = []

        range_of_words = len(max(TEXT_VYCISTENY_ROZDELENY, key=len)) 
        word_lengths = {f'word_length_{n}': [] for n in range(1, range_of_words + 1)}

        for words_and_numbers in TEXT_VYCISTENY_ROZDELENY:

            length_of_word = len(words_and_numbers)
            word_lengths[f'word_length_{length_of_word}'].append(words_and_numbers)
            POCET_SLOV.append(words_and_numbers)

            if words_and_numbers.isalpha():
                if words_and_numbers.istitle():
                    TITLECASE_COUNT.append(words_and_numbers)
                elif words_and_numbers.isupper():
                    UPPERCASE_COUNT.append(words_and_numbers)
                elif words_and_numbers.islower():
                    LOWERCASE_COUNT.append(words_and_numbers)

            elif words_and_numbers.isnumeric():
                TEXT_POUZE_CISLA.append(words_and_numbers)
                TEXT_POUZE_CISLA_SOUCET.append(int(words_and_numbers))
            
            elif words_and_numbers.isalnum():
                numbers = re.findall(r'\d+', words_and_numbers)
                TEXT_POUZE_CISLA.extend(numbers)
                TEXT_POUZE_CISLA_SOUCET.extend(map(int, numbers))

            else: 
                continue

        print(f"There are {(len(POCET_SLOV))} words in the selected text.")
        print(f"There are {(len(TITLECASE_COUNT))} titlecase words in the selected text.")   
        print(f"There are {(len(UPPERCASE_COUNT))} uppercase words.")
        print(f"There are {(len(LOWERCASE_COUNT))} lowercase words.")
        print(f"There are {(len(TEXT_POUZE_CISLA))} numeric strings.")
        print(f"The sum of all the numbers is {sum(TEXT_POUZE_CISLA_SOUCET)}")
        print("-"*65)

        print("-"*65)

        print(f"""{"LEN":<4}|{"OCCURENCES":^50}|{"NR.":>3}""")
        print("-"*65)
        for i, value in enumerate(word_lengths.values(), start=1):
            print(f"{i:<4}|{len(value) * "*":<50}|{len(value):>1}")

    else:
        print(f"We do not have a text with this number. Quitting the program.")
        quit()

else:
    print("Username or Password is inccorect. Quitting the program.")
    quit()
