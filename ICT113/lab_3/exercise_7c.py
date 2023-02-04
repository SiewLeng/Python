"""
Modify question 1 on loops by writing a function displayFromTo(x, y). The function
displays consecutive numbers from the smaller to the larger number. Write also
function main() for the user to enter 2 values which are used to call the function.
"""

def displayFromTo(num1, num2):
    step = 0
    if num1 < num2:
        step += 1
    elif num1 > num2:
        step += -1
    if step == 0:
        print(num1)
    else:
        for i in range(num1, num2 + step, step):
            print(i)

def main():
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))
    return num1, num2

num1, num2 = main()
displayFromTo(num1, num2)