"""
Modify program in 1b to cater for any 2 integer input sequence. If the first is smaller
than the second, print from the smaller to larger. If the first is greater than the second,
print from the larger down to the smaller. Use only 1 loop structure for the printing.
"""

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

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




