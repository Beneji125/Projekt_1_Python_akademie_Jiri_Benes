"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jiří Beneš
email: Beneji125@gmail.com
"""

import re

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

        TEXT_VYCISTENY_ROZDELENY = re.sub(r'[.,!?":;\'()]', '', VYBRANY_TEXT).split()

        TEXT_BEZ_CISEL = []
        for words in TEXT_VYCISTENY_ROZDELENY:
            if words.isalpha():
                TEXT_BEZ_CISEL.append(words)
        print(f"There are {(len(TEXT_BEZ_CISEL))} words in the selected text.")

        titlecase_count = 0
        for word in TEXT_VYCISTENY_ROZDELENY:
            if word.istitle():
                titlecase_count += 1
        print(f"There are {(titlecase_count)} titlecase words")

        uppercase_count = 0
        for word in TEXT_BEZ_CISEL:
            if word.isupper():
                uppercase_count += 1
        print(f"There are {(uppercase_count)} uppercase words.")

        lowercase_count = 0
        for word in TEXT_BEZ_CISEL:
            if word.islower():
                lowercase_count += 1
        print(f"There are {(lowercase_count)} lowercase words.")

        TEXT_BEZ_SLOV = []
        for numbers in TEXT_VYCISTENY_ROZDELENY:
            if numbers.isnumeric():
                TEXT_BEZ_SLOV.append(numbers)
        print(f"There are {(len(TEXT_BEZ_SLOV))} numeric strings.")

        TEXT_BEZ_SLOV_SOUCET = []
        for numbers in TEXT_VYCISTENY_ROZDELENY:
            if numbers.isnumeric():
                TEXT_BEZ_SLOV_SOUCET.append(int(numbers))
        print(f"The sum of all the numbers is {sum(TEXT_BEZ_SLOV_SOUCET)}")

        print("-"*65)

        SLOVA_DLOUHA_1 = []
        SLOVA_DLOUHA_2 = []
        SLOVA_DLOUHA_3 = []
        SLOVA_DLOUHA_4 = []
        SLOVA_DLOUHA_5 = []
        SLOVA_DLOUHA_6 = []
        SLOVA_DLOUHA_7 = []
        SLOVA_DLOUHA_8 = []
        SLOVA_DLOUHA_9 = []
        SLOVA_DLOUHA_10 = []
        SLOVA_DLOUHA_11 = []
        SLOVA_DLOUHA_12 = []
        for words in TEXT_VYCISTENY_ROZDELENY:
            if len(words) == 1:
                SLOVA_DLOUHA_1.append(words)
            elif len(words) == 2:
                SLOVA_DLOUHA_2.append(words)
            elif len(words) == 3:
                SLOVA_DLOUHA_3.append(words)
            elif len(words) == 4:
                SLOVA_DLOUHA_4.append(words)
            elif len(words) == 5:
                SLOVA_DLOUHA_5.append(words)
            elif len(words) == 6:
                SLOVA_DLOUHA_6.append(words)
            elif len(words) == 7:
                SLOVA_DLOUHA_7.append(words)
            elif len(words) == 8:
                SLOVA_DLOUHA_8.append(words)
            elif len(words) == 9:
                SLOVA_DLOUHA_9.append(words)
            elif len(words) == 10:
                SLOVA_DLOUHA_10.append(words)
            elif len(words) == 11:
                SLOVA_DLOUHA_11.append(words)
            elif len(words) == 12:
                SLOVA_DLOUHA_12.append(words)
        print(f"""{"LEN":<4}|{"OCCURENCES":^20}|{"NR.":>3}
{"-"*65}
{"1":<4}|{len(SLOVA_DLOUHA_1) * "*":<20}|{len(SLOVA_DLOUHA_1):>3}
{"2":<4}|{len(SLOVA_DLOUHA_2) * "*":<20}|{len(SLOVA_DLOUHA_2):>3}
{"3":<4}|{len(SLOVA_DLOUHA_3) * "*":<20}|{len(SLOVA_DLOUHA_3):>3}
{"4":<4}|{len(SLOVA_DLOUHA_4) * "*":<20}|{len(SLOVA_DLOUHA_4):>3}
{"5":<4}|{len(SLOVA_DLOUHA_5) * "*":<20}|{len(SLOVA_DLOUHA_5):>3}
{"6":<4}|{len(SLOVA_DLOUHA_6) * "*":<20}|{len(SLOVA_DLOUHA_6):>3}
{"7":<4}|{len(SLOVA_DLOUHA_7) * "*":<20}|{len(SLOVA_DLOUHA_7):>3}
{"8":<4}|{len(SLOVA_DLOUHA_8) * "*":<20}|{len(SLOVA_DLOUHA_8):>3}
{"9":<4}|{len(SLOVA_DLOUHA_9) * "*":<20}|{len(SLOVA_DLOUHA_9):>3}
{"10":<4}|{len(SLOVA_DLOUHA_10) * "*":<20}|{len(SLOVA_DLOUHA_10):>3}
{"11":<4}|{len(SLOVA_DLOUHA_11) * "*":<20}|{len(SLOVA_DLOUHA_11):>3}
{"12":<4}|{len(SLOVA_DLOUHA_12) * "*":<20}|{len(SLOVA_DLOUHA_12):>3}
{"-"*65}
""")
    else:
        print(f"""We do not have a text with this number. Quitting the program""")
        quit()

else:
    print("Username or Password is inccorect. Quitting the program")
    quit()