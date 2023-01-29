"""
(if...else) A telco charges the following for usage of data in a foreign country:

Data         Rate
Up to 2GB    $5 flat
Above 2GB    $5 + $1 for every 100MB or part

thereof

Two example runs are shown here:
Run 1:
Amount of data used (GB): 1.5
Charge is $5.00
Run 2:
Amount of data used (GB): 2.54
Charge is $11.00
"""

from math import ceil

data = float(input("Enter the amount of data used in GB: "))
charge = 0

if (data <= 2):
    charge += 5
else:
    charge += 5 + ceil((data - 2) * 1000 / 100) * 1

print("Charge is ${0:0.2f}".format(charge))

