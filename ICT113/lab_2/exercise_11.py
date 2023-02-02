"""
A computer store allows customers to buy laptops and pay by instalments.
The payment plan is based on the purchase amount as given in the following
table:

Amount                  Payment
Less than 1000          No instalment. Pay full amount.
At least 1000           Either pay in 6 monthly instalments with an addition
                        of 5% of the amount, or pay in 12 monthly
                        instalments with an addition of 10% of the amount.
                        Payment is the result of adding interest to the amount
                        and then dividing by the number of monthly
                        installments.

Write a program that reads in the amount of the laptop. If the amount is at
least 1000, prompt the user to select 0, 6 or 12 months, and displays the
instalment plan. Examples of different input are as follows:
"""

amount = float(input("Enter amount of labtop:"))
isPayByInstallment = False
noOfMonthOfInstallment = 0
output = ""

if (amount > 1000):
    noOfMonthOfInstallment = int(input("Pay in 0, 6 or 12 month instalment: "))

if (noOfMonthOfInstallment == 0):
    output = "Please pay ${0:0.2f}. No instalment plan.".format(amount)
elif(noOfMonthOfInstallment == 6):
    amountPerMonth = (1 + 5 / 100) * amount / 6
    output += "6 month instalment plan of ${0:0.2f} per month".format(amountPerMonth)
elif(noOfMonthOfInstallment == 12):
    amountPerMonth = (1 + 10 / 100) * amount / 12
    output += "12 month instalment plan of ${0:0.2f} per month".format(amountPerMonth)
else:
    output += "Invalid number of month installment!"

print(output)

