"""
(Nested list) In a diving competition, every diver makes 3 dive attempts. Each dive
attempt is awarded a score which is a value between 0 and 10, inclusive of 0 and
10. The diver with the best total wins.
You are given the scores for 6 divers:
scores=[[7.9,7.8,8.2],[8.0,8.5,8.4],[9.0,9.1,9.5],
[9.0,9.2,9.2],[8.5,8.8,9.0],[9.7,9.3,9.2]]

a. Display the results in the following format:
Diver A1 A2 A3 Total
1 7.9 7.8 8.2 23.9
2 8.0 8.5 8.4 24.9
3 9.0 9.1 9.5 27.6
4 9.0 9.2 9.2 27.4
5 8.5 8.8 9.0 26.3
6 9.7 9.3 9.2 28.2
You may assume that every diver will make 3 attempts (fixed). However, the
number of divers can vary.
b. Display the top 3 positions in descending order of the total score as follows:
Top three positions
Diver Total
6 28.2
3 27.6
4 27.4
Assume there are no ties.
"""
def displayScores(scores):
    print("{0:>5} {1:<3} {2:<3} {3:<3} {4:<5}".format('Diver', 'A1', 'A2', 'A3', 'Total'))
    for i in range(0, len(scores), 1):
        print('{0:>5} '.format(i + 1), end = '')
        total = 0
        for n in range(0, len(scores[i]), 1):
            total += scores[i][n]
            print('{0:<3} '.format(scores[i][n]), end = '')
        print('{0:<5}'.format(total))

def displaceTop3Position(scores):
    result = []
    for i in range(0, len(scores), 1):
        total = 0
        for n in range(0, len(scores[i]), 1):
            total += scores[i][n]
        result.append({
            'diver': i + 1,
            'total': total
        })
    for i in range(0, len(result) - 1, 1):
        highestTotal = result[i]['total']
        index = i
        for n in range(i + 1, len(result), 1):
            if (result[n]['total'] > highestTotal):
                index = n
                highestTotal = result[n]['total']
        if (i != index):
            temp = result[i]
            result[i] = result[index]
            result[index] = temp
    print('\nTop Three Position')
    print('{0:>5}  {1:<6}'.format('Diver', 'Total'))
    for i in range(0, 3, 1):
        print('{0:>5}  {1:<6}'.format(result[i]['diver'], result[i]['total']))

scores =[
    [7.9,7.8,8.2],
    [8.0,8.5,8.4],
    [9.0,9.1,9.5],
    [9.0,9.2,9.2],
    [8.5,8.8,9.0],
    [9.7,9.3,9.2]
]
displayScores(scores)
displaceTop3Position(scores)
