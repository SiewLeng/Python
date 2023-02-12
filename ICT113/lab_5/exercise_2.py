"""
(Nested list) A nested list is used to represent the scores of 2 players A and B in a
badminton game as follows:
gameScore=[['A','B'],[21,11],[19,21],[20,22]]

The above represents 3 games played between player A and B. Based on the game
score, the score of the first game score is 21-11 in which Player A is the winner, etc.
The overall game score is 1-2 and player B is the winner.

It is possible that only 2 games are played with the game score, as shown in the
following example:
gameScore=[['A','B'],[21,1],[21,10]]

In this example, the overall game score is 2-0 and player A is the winner.

a. Write a function displayGameScore(gameScore) that has a list in the above
format as parameter and displays a summary game score. The result should be
displayed in the following format:
Player A vs B
Game 1 21-11
Game 2 19-21
Game 3 11-21
Overall 1-2
Winner is player B
Test the function using any of the above lists.

b. Write a function getPlayerNames() that prompts for the names of 2 players
and returns a game score list. The score list returned should be in the following
structure:
[ [ ‘player 1 name’, ‘player 2 name’] ]
Since there are no game scores yet, the list consists of only the player names.

c. Write a function inputGameScores(scoreList) that has the score list as
parameter and prompts for a game score. For example,
Game 1 score A vs B: 21-10
Game 2 score A vs B: 21-11
Game 3 score A vs B: <enter> key to represent end of input
(Assuming the players names are A and B)
The scores are entered with a dash in between. Add each game score in score
list. Test out the function.

d. Write a main function to test out all 3 functions.
"""

def displayGameScore(gameScore):
    player_0 = gameScore[0][0]
    player_1 = gameScore[0][1]
    scores = {
        player_0: 0,
        player_1: 0
    }
    print('Player {0} vs {1}'.format(player_0, player_1))
    for i in range(1, len(gameScore), 1):
        if (gameScore[i][0] > gameScore[i][1]):
            scores[player_0] += 1
        elif(gameScore[i][1] > gameScore[i][0]):
            scores[player_1] += 1
        print('Game {0} {1}-{2}'.format(i, gameScore[i][0], gameScore[i][1]))
    print('Overall {0}-{1}'.format(scores[player_0], scores[player_1]))
    winner = ""
    if (scores[player_0] > scores[player_1]):
        winner = player_0
    elif (scores[player_1] > scores[player_0]):
        winner = player_1
    if (winner != ""):
        print('Winner is player {0}'.format(winner))
    else:
        print('It is a tie. There is no winner')

def getPlayerNames():
    player_0 = input('Enter player 1 name: ')
    player_1 = input('Enter player 2 name: ')
    while (player_0.lower() == player_1.lower()):
        player_1 = input('Enter player 2 name: ')
    scoreList = []
    scoreList.append([player_0, player_1])
    return scoreList

def inputGameScores(scoreList):
    count = 1
    toExit = False
    player_0 = scoreList[0][0]
    player_1 = scoreList[0][1]
    while(not toExit):
        score = input('Game {0} score {1} vs {2}: '.format(count, player_0, player_1))
        if (score != ''):
            score_0 = score.split('-')[0]
            score_1 = score.split('-')[1]
            scoreList.append([score_0, score_1])
        else:
            toExit = True
        count += 1

def main():
    scoreList = getPlayerNames()
    inputGameScores(scoreList)
    displayGameScore(scoreList)

main()



