# Gage Farmer
# HealthCalculator.py
# 8/11/21
# Calculates BMI a and heart rate at specific values for different body types

import math


def main():

    # Gets all of the inputs
    print("Please enter the following values for the user...")
    height = int(input("Height in inches: "))
    weight = int(input("Weight in pounds: "))
    age = input("Current age: ")
    restingHR = input("Resting heart rate: ")

    # Prints results
    print("\nResults...")
    print("Your BMI is: " + bmi(height, weight))

    print("\nExercise Intensity Heart Rates:")
    print("Intensity       Max Heart Rate\n")

    chart = karvonen(age, restingHR)

    for i in range(10):
        intensity = (0.5 + (i * 0.05))
        print(str("{:.2f}".format(intensity)) + "            " + str(chart[intensity]))


def bmi(height=int, weight=int):

    # Converts lbs to kg and in to m^2
    # Calculates BMI and passes it back along with the category they fit in

    weight = weight / 2.205
    height = (height / 39.37) ** 2

    result = weight / height

    if result < 18.5:
        category = "Underweight"
    elif 18.5 <= result < 24.9:
        category = "Normal Weight"
    elif 25 <= result < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    result = "{:.2f}".format(result)
    return str(result) + " -- " + category


def karvonen(age=int, restingHR=int):

    # Calculates heart rate at specific intensities then returns them in grid formation

    chart = dict()

    for i in range(10):
        intensity = (0.5 + (i * 0.05))
        result = (((220 - int(age)) - int(restingHR)) * intensity) + int(restingHR)
        chart[intensity] = "{:.2f}".format(result)

    return chart


main()
