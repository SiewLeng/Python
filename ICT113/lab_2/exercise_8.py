"""
(if...elif...else) Modify the program in question 2 with the following rate:

Data         Rate
Up to 2GB    $5 flat
Above 2GB    $5 + $1 for every 100MB or part thereof
Above 4GB    $25 flat

The program also validates that input must be greater than 0. Otherwise,
display “Invalid input!”.
"""
from math import ceil

isValidInput = False
input = input("Enter the amount of data used in GB: ")
charge = 0
output = ""

if (len(input.split(".")) == 1):
    isValidInput = input.isdigit() and float(input) > 0
elif (len(input.split(".")) == 2):
    isValidInput = input.split(".")[0].isdigit() and input.split(".")[1].isdigit() and float(input) > 0

if (isValidInput):
    inputFloat = float(input)
    if (inputFloat <= 2):
        charge += 5
    elif(inputFloat <= 4):
        charge += 5 + ceil((inputFloat - 2) * 1000 / 100) * 1
    else:
        charge += 25
    output += "The charge is ${0:0.2f}".format(charge)
else:
    output = "Invalid input!"

print(output)