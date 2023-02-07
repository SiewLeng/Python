"""
(File handling) The rainfall (in mm) for each day in a particular month is captured in a
file, rainfall.dat. Write a program to read the rainfall for each day, and display a
summary report as follows:
Rainfall Summary
Average rainfall 5.65mm
No of days with no rain 3 days
Highest rainfall recorded 20.6mm
"""

infile = open("rainfall.dat", "r")
sumOfRainFall = 0
totalNumberOfDays = 0
noOfDaysWithNoRain = 0
averageRainFall = 0
highestRainfall = 0

for line in infile:
    rainfall = float(line)
    sumOfRainFall += rainfall
    if (rainfall == 0):
        noOfDaysWithNoRain += 1
    if (rainfall > highestRainfall):
        highestRainfall = rainfall
    totalNumberOfDays += 1

infile.close()

averageRainFall += sumOfRainFall / totalNumberOfDays

print("Rainfall Summary")
print("Average rainfall: {0:0.2f}mm".format(averageRainFall))
print("No of days with no rain: {0} days".format(noOfDaysWithNoRain))
print("Highest rainfall recorded: {0}mm".format(highestRainfall))

