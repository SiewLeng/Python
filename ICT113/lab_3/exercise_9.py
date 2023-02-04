"""
Write a function getValidValue(msg, x, y) that prompts the user for an input using
msg, between x and y (float, inclusive of both). If the value is out of range, display
‘Invalid input. Try again’ and prompt again for input. The function returns the valid
input between x and y. Call the function using this test:
            mark = getValidValue(‘Enter mark’, 0, 100)

Write also function main() to call the function. main() displays the mark.
"""

def getValidValue(msg, x, y):
    value = float(input(msg + ": "))
    while (value > y or value < x):
        print("Invalid input. Try again")
        value = float(input(msg + ": "))
    return value

def main():
    mark = getValidValue("Enter mark", 0, 100)
    print("The valid mark enter is {0}".format(mark))

main()