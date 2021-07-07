# invoice.py
# Gage Farmer
# 7/7/2021

from math import *
import random


def main():

    # Assigns default values
    bookNum = 1
    labNum = 1
    creditNum = 3

    # For if you want to enter your own inputs
    selfInput = False

    # Gathers input values and makes costs of books random
    # because books are rarely the same price.
    if selfInput:
        creditNum = int(input("Number of Credit Hours: "))
        labNum = int(input("Number of Lab Classes: "))
        bookNum = int(input("Number of Books: "))
        bookFee = 0.99
        for i in range(bookNum):
            bookFee += random.randrange(30, 120)

    # Calculates fees
    bookFee = bookNum * 52.99
    labFee = labNum * 25.00
    tuitionFee = creditNum * 157.93

    # Calls layout to print invoice
    layout(round(bookFee, 2), round(labFee, 2), round(tuitionFee, 2))


def layout(bookFee, labFee, tuitionFee):

    # Calculates total
    totalFee = bookFee + labFee + tuitionFee

    # These are all just for formatting purposes
    frame = "**************************************************"
    address = "       Columbus State Community College\n" \
              "        550 East Spring Street\n" \
              "        Columbus, OH 43215"
    split = "--------------------------------------------------"
    bills = f"       Product Name:     Product Price:\n" \
            f"        Books             ${bookFee}\n" \
            f"        Lab Fees          ${labFee}\n" \
            f"        Tuition           ${tuitionFee}"
    total = f"                         Total:\n" \
            f"                          ${totalFee}"
    thanks = "   Thank you for being a Columbus State Student           "
    endl = "\n"

    # Prints invoice
    print(frame, endl, address, endl, split, endl, bills, endl, split,
          endl, total, endl, split, endl, endl, thanks, endl, frame)


main()
