"""
Modify the above program in exercise_2a to store the report in an output file, bmi.dat
"""

infile = open("customers.dat", "r")
outfile = open("bmi.dat", "w")

line = infile.readline()

print("{0:<8} {1:<8} {2:<8} {3:<8}".format("Name", "Weight", "Height", "BMI"), file=outfile)

while(line != ""):
    splitLines = line.split(",")
    name = splitLines[0]
    weight = float(splitLines[1])
    height = float(splitLines[2])
    bmi = weight / height**2
    print("{0:<8} {1:<8} {2:<8} {3:<8.2f}".format(name, weight, height, bmi), file=outfile)
    line = infile.readline()

infile.close()
outfile.close()