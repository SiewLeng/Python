"""
Write a program that reads an input representing a change which is an
amount less than 1 dollar. The program calculates the change into 50, 10, 5
and 1 cent coins. The program then displays the number of each coin
required for that change. E.g.
Enter change: 47
50 cent: 0
10 cent: 4
5 cent: 1
1 cent: 2
"""

change = int(input("Enter the change in cent: "))
centInOnes = change % 10
noOfOneCent = centInOnes % 5
noOfFiveCent = centInOnes // 5
centInTens = change // 10
noOfTenCents = centInTens % 5
noOfFiftyCents = centInTens // 5

print ("50 cent: ", noOfFiftyCents)
print ("10 cent: ", noOfTenCents)
print ("5 cent: ", noOfFiveCent)
print ("1 cent: ", noOfOneCent)
