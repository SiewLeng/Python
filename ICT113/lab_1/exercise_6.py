"""
A restaurant is offering meals at 50% discount. A service charge (10%) and
GST (7%) apply to the discounted cost. While the service charge applies to
the discounted price, note that the GST calculation is based on the total of the
discounted amount and the service charge.
Write a program that reads in the cost of the meal and displays a detailed
receipt. An example is as follows:
Enter meal amount ($): 120
Receipt
Cost of meal: $120.00
50% discount: $ 60.00
Service charge: $ 6.00
GST: $ 4.62
Total amount: $ 70.62
(Output should be formatted.)
"""

costOfMeal = float(input("Enter meal amout ($): "))
discount = 50 / 100 * costOfMeal
discountedPrice = costOfMeal - discount
serviceCharge = 10 / 100 * discountedPrice
gst = 7 / 100 * (discountedPrice + serviceCharge)
total = discountedPrice + serviceCharge + gst

print("Receipt")
print("{:<20s}".format("Cost of meal:"), end = '')
print(f"${costOfMeal:6.2f}")
print("{:<20s}".format("50% discount:"), end = '')
print(f"${discountedPrice:6.2f}")
print("{:<20s}".format("Service Charge:"), end = '')
print(f"${serviceCharge:6.2f}")
print("{:<20s}".format("GST"), end = '')
print(f"${gst:6.2f}")
print("{:<20s}".format("Total: "), end = '')
print(f"${total:6.2f}")