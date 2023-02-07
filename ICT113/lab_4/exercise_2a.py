"""
(File handling) The name, weight and height of some customers in a gym are stored
in a comma separated file, customer.dat
Write a program that reads each line of customer.dat and as each line is read, it
computes the body mass index (bmi) report as follows:
Name Weight Height BMI
John 50 1.4 25.51
Peter 60 1.7 20.76
...
Joe 45 1.45 21.40
BMI is computed using the formula: bmi = weight / height^2
"""

infile = open("customers.dat", "r")
line = infile.readline()

print("{0:<8} {1:<8} {2:<8} {3:<8}".format("Name", "Weight", "Height", "BMI"))

while(line != ""):
    splitLines = line.split(",")
    name = splitLines[0]
    weight = float(splitLines[1])
    height = float(splitLines[2])
    bmi = weight / height**2
    print("{0:<8} {1:<8} {2:<8} {3:<8.2f}".format(name, weight, height, bmi))
    line = infile.readline()

infile.close()

