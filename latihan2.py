#!/usr/bin/env python

import random
from re import X

def main():
    """Start a number guessing game between 1-100."""
    print("Guess the number!")

    # x= random.randint(1, 100)
    x = random.gauss(1,5)
    print(x)
    guess = None

    while x!=guess:

        guess=int(input("Pick up a number between 1 to 5:"))

        if x==guess:
            print("You genius!")
        elif x > guess:
            print("Try a bigger number.")
        elif x < guess:
            print("Try a smaller number.")

main()