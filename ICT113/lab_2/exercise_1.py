"""
(String) Write a program that reads in an email address, e.g. joe@suss.edu.sg
Display the name and the organisation on separate lines. Example:
Input email address: joe@suss.edu.sg
Name is joe
Organisation is suss.edu.sg
Assume input is valid.
"""

email = input("Enter your email address: ")
splitEmail = email.split("@")
name = splitEmail[0]
organisation = splitEmail[1]

print("Input email address: {0}".format(email))
print("Name is {0}".format(name))
print("Organisation is {0}".format(organisation))