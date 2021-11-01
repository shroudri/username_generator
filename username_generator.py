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
    lowercaseFile = open("/tmp/lowercase", "w")             # Defining output file
    with open(wordlist) as f:                                  # If output file is the input
        lines = f.readlines()                               # Read all lines of the input
        for line in lines:                                  
            lowercaseFile.writelines(line.lower()) 


def lowercase_transformations():
    f = open("/tmp/lowercase", "r")
    lines = f.readlines()
    for line in lines:                                      # For every line of the file (for example one line: John Lennon)
        print(line.split()[0])                              # john lennon -> john
        print(line.split()[1])                              # john lennon -> lennon
        print(line[0] + '.' + line.split()[1])              # john lennon -> j.lennon
        print(line[0] + '-' + line.split()[1])              # john lennon -> j-lennon
        print(line[0] + '_' + line.split()[1])              # john lennon -> j_lennon
        print(line[0] + '+' + line.split()[1])              # john lennon -> j+lennon
        print(line[0] + line.split()[1])                    # john lennon -> jlennon
        print(line.split()[1]+line.split()[0])              # john lennon -> lennonjohn



def uppercase_transformations():
    f = open("/tmp/lowercase", "r")
    lines = f.readlines()
    for line in lines:
        firstWord = line.split()[0]
        secondWord = line.split()[1]
        print(firstWord.capitalize())                                       # john lennon -> John
        print(secondWord.capitalize())                                      # john lennon -> Lennon
        print(firstWord[0].upper() + '.' + secondWord.capitalize())         # john lennon -> J.Lennon
        print(firstWord[0].upper() + '_' + secondWord.capitalize())         # john lennon -> J_Lennon
        print(firstWord[0].upper() + '-' + secondWord.capitalize())         # john lennon -> J-Lennon
        print(firstWord[0].upper() + secondWord.capitalize())               # john lennon -> JLennon
        print(secondWord.capitalize() + firstWord.capitalize())             # john lennon -> LennonJohn
        print(firstWord.upper())                                            # john lennon -> JOHN
        print(secondWord.upper())                                           # john lennon -> LENNON
        print (firstWord.upper() + secondWord.upper())                      # john lennon -> JOHNLENNON




parser = argparse.ArgumentParser(description='Python script to generate user lists for bruteforcing!')
parser.add_argument('-w', '--wordlist', type=str, metavar='wordlist', required=True, help="Specify path to the wordlist")
parser.add_argument('-u', '--uppercase', action='store_true', help='Also produce uppercase permutations. Disabled by default')


args = parser.parse_args()

if args.uppercase is False:
    file = args.wordlist
    generate_root_list_lowercase(file)
    lowercase_transformations()
elif args.uppercase is True:
    file = args.wordlist
    generate_root_list_lowercase(file)
    lowercase_transformations()
    uppercase_transformations()
else:
    exit()