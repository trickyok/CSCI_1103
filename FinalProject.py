# Gage Farmer
# FinalProject.py
# 8/12/21
# Tells user which numbers in a range are divisible
# by 3 and/or 5


def main():

    # Gets range from user
    start = input("Please enter starting value: ")
    end = input("Please enter ending value: ")
    crange = range(int(start), int(end)+1)

    # Loops through each number and defines what they are divisible by
    for i in crange:
        strToPrint = str(i)
        bothPossible = False

        if div3(i):
            strToPrint = str(i) + " -- 3"
            bothPossible = True

        if div5(i):
            strToPrint = str(i) + " -- 5"
            if bothPossible:
                strToPrint = str(i) + " -- Both"

        print(strToPrint)


def div3(num):

    if num % 3 == 0:
        return True


def div5(num):
    if num % 5 == 0:
        return True


main()
