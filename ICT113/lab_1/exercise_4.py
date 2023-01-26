"""
Write a program that reads in a positive integer representing time in seconds
and converts it to hour, minute and seconds. For example, if the input is 3670
seconds, output 1 hour, 1 minute and 10 seconds.
"""
totalInSeconds = int(input("Enter time in seconds: "))

seconds = totalInSeconds % 60
minutesInTotal = totalInSeconds // 60
minutes = minutesInTotal % 60
hours = minutesInTotal // 60

# print("output: ", hours, "hours, ", minutes, "minutes, ", seconds, "seconds")
print(f"output: {hours} hours, {minutes} minutes, {seconds} seconds")


