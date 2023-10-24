"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""

import random

def title():
    print('\033[1m' + '=' * 8 + " Welcome! " + '=' * 8 +  '\033[0m')
    print("Guess the number between 1 and 100. \nEnter the number in the field below.\n")

def game():
    n = random.randint(1, 100)
    attempt = 1

    while True:
        a = int(input("Gimme a number: "))

        if a == n:
            print('\033[1m' + f"\nYou won! The number was {n}. It took you {attempt} attempts." + '\033[0m')
            break
        elif a < n:
            print("Too low")
            attempt += 1
        elif a > n:
            print("Too high")
            attempt += 1

def main():
    title()
    game()

main()