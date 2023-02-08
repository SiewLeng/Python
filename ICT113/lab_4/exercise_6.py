"""
(Multiple lists) A program is required to record and display the results of a swimming
competition. The swimming pool has 5 lanes. The swimmer name for each lane is
first recorded. After the race, the timings for the swimmers are captured. The results
for the race is then displayed.

a. Write a function inputSwimmers() that prompts for 5 swimmer names and returns the
names in a list.
An example of the input session is as follows:
Enter lane 1 swimmer: James
Enter lane 2 swimmer: Joseph
...
Enter lane 5 swimmer: Ian
Test the function.

b. Write another function inputTiming(swimmers) that has the list of swimmers names.
The function creates an empty list, and records the timing for each of the swimmers.
The timings list is returned. An example of the input session is as follows:
Enter timing for James: 47.15
Enter timing for Joseph: 46.91
....
Enter timing for Ian: 48.01

c. Write another function printResults(swimmers, timings) that has the name and
timing lists as parameters. The function prints a summary of the results as follows:
James 47.15s
Joseph 46.91s
...
Ian 48.01s
Fastest is 46.91s
Assume all the timings are unique. Write a main function to test out all the parts
in this question.

d. Modify the function in part c) that prints the summary in sorted order of the timing.
Therefore, the summary may look like this:
Joseph 46.91s
James 47.15s
...
Ian 48.01s
"""

#(a)
def inputSwimmers():
    swimmers = []
    for i in range (1, 6, 1):
        prompt = 'Enter lane {0} swimmer: '.format(i)
        swimmers.append(input(prompt))
    return swimmers


#(b)
def inputTiming(swimmers):
    print('\n')
    timings = []
    for i in range (0, len(swimmers), 1):
        prompt = 'Enter timing for {0}: '.format(swimmers[i])
        timings.append(float(input(prompt)))
    return timings

#(c)
def printResults(swimmers, timings):
    print('\n')
    fastestTime = timings[0]
    for i in range (0, len(swimmers), 1):
        print('{0:<10} {1:>5.2f}s'.format(swimmers[i], timings[i]))
        if (timings[i] < fastestTime):
            fastestTime = timings[i]
    print('Fastest is {0}s'.format(fastestTime))

#(d)
def printSortedResult(swimmers, timings): 
    print('\n')
    for i in range (0, len(swimmers) - 1, 1):
        indexOfFastestTiming = i
        for n in range (i + 1, len(timings), 1):
            if (timings[n] < timings[indexOfFastestTiming]):
                indexOfFastestTiming = n
        if (indexOfFastestTiming != i):
            temp = timings[i]
            timings[i] = timings[indexOfFastestTiming]
            timings[indexOfFastestTiming] = temp
    
    for i in range (0, len(swimmers), 1):
        print('{0:<10} {1:>5.2f}s'.format(swimmers[i], timings[i]))


swimmers = inputSwimmers()
timings = inputTiming(swimmers)
printResults(swimmers, timings)
printSortedResult(swimmers, timings)