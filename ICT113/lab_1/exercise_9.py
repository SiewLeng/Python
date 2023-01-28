"""
Write a program that reads in a time in 24 hr format. The program displays the
time after adding 1 second to the time.
First example:
Enter current hr: 2
Enter current min: 58
Enter current sec: 50
Clock time is 02:58:59
After 1 second, the time is 02:59:00
Second example:
Enter current hr: 23
Enter current min: 59
Enter current sec: 59
Clock time is 23:59:59
After 1 second, the time is 00:00:00
"""

hour = int(input("Enter current hr: "))
min = int(input("Enter current min: "))
sec = int(input("Enter current sec: "))

currentSecInTotal = sec + 1
currentSec = currentSecInTotal % 60
currentMinInTotal = min + currentSecInTotal // 60
currentMin = currentMinInTotal % 60
currentHourInTotal = hour + currentMinInTotal // 60
currentHour = currentHourInTotal % 24

print("Current clocktime is ", end = "")
print(f"{hour:02d}:", end = "")
print(f"{min:02d}:", end = "")
print(f"{sec:02d}")
print("After 1 second, the time is ", end = "")
print(f"{currentHour:02d}:", end = "")
print(f"{currentMin:02d}:", end = "")
print(f"{currentSec:02d}")