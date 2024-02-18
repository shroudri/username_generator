#!/usr/bin/python3

# Script created by shroudri
# First script ever, don't be too hard on me :P
#   Namelist should look like this:
#   John Lennon
#   Max Verstappen
#   Lewis Hamilton
#   and so on ....




import argparse


def generate_root_list_lowercase(wordlist):
    names = []
    with open(wordlist) as f:                               # Open file for processing
        for line in f:
            names.append(line.strip().lower())
    return names


def lowercase_transformations(names):
    for line in names:
        print(line.split()[0])                              # john lennon -> john
        print(line.split()[1])                              # john lennon -> lennon
        print(line[0] + '.' + line.split()[1])              # john lennon -> j.lennon
        print(line[0] + '-' + line.split()[1])              # john lennon -> j-lennon
        print(line[0] + '_' + line.split()[1])              # john lennon -> j_lennon
        print(line[0] + '+' + line.split()[1])              # john lennon -> j+lennon
        print(line[0] + line.split()[1])                    # john lennon -> jlennon
        print(line.split()[0]+line.split()[1])              # john lennon -> johnlennon
        print(line.split()[1]+line.split()[0])              # john lennon -> lennonjohn
        print(line.split()[0] + '.' + line.split()[1])      # john lennon -> john.lennon
        print(line.split()[1] + '.' + line.split()[0])      # john lennon -> lennon.john



def uppercase_transformations(names):
    for line in names:
        firstWord = line.split()[0]
        secondWord = line.split()[1]
        print(firstWord.capitalize())                                       # john lennon -> John
        print(secondWord.capitalize())                                      # john lennon -> Lennon
        print(firstWord[0].upper() + '.' + secondWord.capitalize())         # john lennon -> J.Lennon
        print(firstWord[0].upper() + '_' + secondWord.capitalize())         # john lennon -> J_Lennon
        print(firstWord[0].upper() + '-' + secondWord.capitalize())         # john lennon -> J-Lennon
        print(firstWord[0].upper() + secondWord.capitalize())               # john lennon -> JLennon
        print(firstWord.capitalize() + secondWord.capitalize())             # john lennon -> JohnLennon
        print(secondWord.capitalize() + firstWord.capitalize())             # john lennon -> LennonJohn
        print(firstWord.upper())                                            # john lennon -> JOHN
        print(secondWord.upper())                                           # john lennon -> LENNON
        print (firstWord.upper() + secondWord.upper())                      # john lennon -> JOHNLENNON




parser = argparse.ArgumentParser(description='Python script to generate user lists for bruteforcing!')
parser.add_argument('-w', '--wordlist', type=str, metavar='wordlist', required=True, help="Specify path to the wordlist")
parser.add_argument('-u', '--uppercase', action='store_true', help='Also produce uppercase permutations. Disabled by default')


args = parser.parse_args()

names = generate_root_list_lowercase(args.wordlist)
lowercase_transformations(names)

if args.uppercase:
    uppercase_transformations(names)
