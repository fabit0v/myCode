#!/usr/bin/env python3

#imports the library random
import random

def main():

    wordbank = ["indentation", "spaces"] 
    wordbank.append(4) #add int 4 to end of list

    tlgstudents = ["Aaron", "Andy", "Asif",
                    "Brent", "Cedric", "Chris",
                    "Cory", "Ebrima", "Franco",
                    "Greg", "Hoon", "Joey",
                    "Jordan", "JC", "LB",
                    "Mabel", "Shon", "Pat", "Zach"]
    
    print(tlgstudents)
    print(wordbank)

    num = int(input("Pick a number between 1-18:" ))#asks user to pick a number
    name = tlgstudents[num] #assigns value from tlgstudents to corresponding int input


    print(f"Your name is {name}")
    print(f"{name} always uses {wordbank[2]} {wordbank[1]} to indent") 
    # calls name, appended int to wordbank, and "spaces"

    name = random.choice(tlgstudents) # chooses random value from tlgstudents
    print(f"Random name: {name}")



main()
