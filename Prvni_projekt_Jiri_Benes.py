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
north of US 30N and the Union Pacific Railroad,
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

    if TEXT_NUMBER > 0 and TEXT_NUMBER <= (len(TEXTS) + 1):
        VYBRANY_TEXT = TEXTS[TEXT_NUMBER - 1]
        print(f"TEXT_{TEXT_NUMBER}:{VYBRANY_TEXT}")
        print("-"*65)

        TEXT_VYCISTENY_ROZDELENY = re.sub(r'[.,!?":;\'()-]', ' ', VYBRANY_TEXT).split()

        TEXT_BEZ_CISEL = []
        TEXT_BEZ_SLOV = []
        TEXT_BEZ_SLOV_SOUCET = []
        titlecase_count = 0
        uppercase_count = 0
        lowercase_count = 0

        range_of_words = len(max(TEXT_VYCISTENY_ROZDELENY, key=len)) 
        word_lengths = {f'word_length_{n}': [] for n in range(1, range_of_words + 1)}

        for words_and_numbers in TEXT_VYCISTENY_ROZDELENY:
            if words_and_numbers.isalpha():
                TEXT_BEZ_CISEL.append(words_and_numbers)
                if words_and_numbers.isalpha() and words_and_numbers.istitle():
                    titlecase_count += 1
                elif words_and_numbers.isalpha() and words_and_numbers.isupper():
                    uppercase_count += 1
                elif words_and_numbers.isalpha() and words_and_numbers.islower():
                    lowercase_count += 1
            elif words_and_numbers.isnumeric():
                TEXT_BEZ_SLOV.append(words_and_numbers)
                TEXT_BEZ_SLOV_SOUCET.append(int(words_and_numbers))
            else: 
                continue
            length_of_word = len(words_and_numbers)
            word_lengths[f'word_length_{length_of_word}'].append(words_and_numbers)

        print(f"There are {(len(TEXT_BEZ_CISEL))} words in the selected text.")
        print(f"There are {(titlecase_count)} titlecase words")     
        print(f"There are {(uppercase_count)} uppercase words.")
        print(f"There are {(lowercase_count)} lowercase words.")
        print(f"There are {(len(TEXT_BEZ_SLOV))} numeric strings.")
        print(f"The sum of all the numbers is {sum(TEXT_BEZ_SLOV_SOUCET)}")
        print("-"*65)

        pprint.pprint(word_lengths)
        print("-"*65)

        print(f"""{"LEN":<4}|{"OCCURENCES":^50}|{"NR.":>3}""")
        print("-"*65)
        for i, value in enumerate(word_lengths.values(), start=1):
            print(f"{i:<4}|{len(value) * "*":<50}|{len(value):>1}")

    else:
        print(f"""We do not have a text with this number. Quitting the program""")
        quit()

else:
    print("Username or Password is inccorect. Quitting the program")
    quit()
