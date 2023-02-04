"""
Division of 2 numbers x by y can be done by repeatedly, subtracting y from x until y
is less than x. For example, if x=11 and y=4, then 11-4-4=3. The quotient is 2 (subtract
twice) and the remainder is 3. Write a function divide(x, y) that uses the above
algorithm to return the quotient and remainder. Test the function.
"""
# x divided by y
def divide(x, y):
    Q = 0
    R = x
    while (R >= y):
        Q += 1
        R = x - Q * y
    return Q, R

def main():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    Q,R = divide(x, y)
    print("x divided by y: {0} r {1}".format(Q, R))

main()