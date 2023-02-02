"""
(while, sentinel loop) Write a program that simulates the point of sale at a supermarket
checkout. The program inputs the quantity and price of items and displays price, the
subtotal. Input ends when -1 is entered for quantity to indicate there is no more item
to checkout. The GST and the final price are then computed. For example,
Enter quantity: 2
Enter unit price: 1.5
Subtotal is $3.00
Enter quantity: 4
Enter unit price: 2.25
Subtotal is $9.00
Enter quantity: -1
Total price is $12.00
GST is $0.84
Please pay $12.84
"""

numOfQuantity = int(input("Enter quantity: "))
total = 0
gst = 0
final = 0

while (numOfQuantity != -1):
    unitPrice = float(input("Enter unit price: "))
    subtotal = numOfQuantity * unitPrice
    total += subtotal
    print("Subtotal is ${0:0.2f}".format(subtotal))
    numOfQuantity = int(input("Enter quantity: "))

gst = 7 / 100 * total
final = total + gst

print("Total price is ${0:0.2f}".format(total))
print("GST is ${0:0.2f}".format(gst))
print("Please pay ${0:0.2f}".format(final))