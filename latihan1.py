#!/usr/bin/env python

import random

def main():
    """Start a number guessing game between 1-100."""
    print("Guess the number!")

    x= random.randint(1, 5)
    print(x)
    guess = None

    while x!=guess:

        guess=int(input("Pick up a number between 1 to 5:"))

        if x==guess:
            print("You genius!")
        else:
            print("Your answer is wrong.")
        
main()