"""
Modify question 1 on loops by writing a function displayFromTo(x, y). The function
displays consecutive numbers from the smaller to the larger number. Write also
function main() for the user to enter 2 values which are used to call the function.
"""

def displayFromTo(num1, num2):
    sum = 0
    for i in range (num1, num2 + 1, 1):
        print(i)
        sum += i
    print("Total sum of all the above number: {0}".format(sum))

def main():
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer (larger than first integer): "))
    return num1, num2

num1, num2 = main()
displayFromTo(num1, num2)