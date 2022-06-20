#!/usr/bin/env python

import random

def main():
    """Start a Periodic Table guessing game."""
    print("Guess the name of the alkali metal element!")

    periodic = [
        "lithium",
        "sodium",
        "potassium",
        "rubidium",
        "cesium",
        "francium"
        ]

    x = random.choice(periodic)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("What elemen am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))

main()
