# Gage Farmer
# HiLoGame.py
# 8/1/2021

import random


def main():

    active = True
    x = True

    # gets maximum number from user
    while x:
        maximum = input("What should the maximum number for this game be? ")
        try:
            maximum = int(maximum)
            x = False
        except ValueError:
            print(" ")

    # chooses random number from range
    answer = int(random.randrange(1, maximum))

    while active:
        x = True

        while x:
            safe = True
            print(" ")
            guess = input("Guess my number: ")
            try:
                guess = int(guess)
                x = False
            except ValueError:
                safe = False

        if safe:
            if guess == answer:
                print("You guessed my number!")
                active = False

            elif guess > answer:
                print("Your guess is too high")

            elif guess < answer:
                print("Your guess is too low")

    x = True
    while x:
        replay = input(f"\nDo you wish to play again? (Y/N): ")
        if str.lower(replay) == 'y':
            x = False
            print(" ")
            main()
        elif str.lower(replay) == 'n':
            return 0


main()
