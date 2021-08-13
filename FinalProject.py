# Gage Farmer
# FinalProject.py
# 8/12/21
# Tells user which numbers in a range are divisible
# by 3 and/or 5


def main():

    by3 = []
    by5 = []
    byBoth = []

    # Gets range from user
    start = input("Please enter a starting point: ")
    end = input("Please enter an end point: ")
    range = range(int(start), int(end))

    # Loops through each number and defines what they are divisible by
    for i in range:
        bothPossible = False

        if div3(i):
            by3.append(i)

        if div5(i):
            by5.append(i)
            if bothPossible:
                byBoth.append(i)

    for i in range:

