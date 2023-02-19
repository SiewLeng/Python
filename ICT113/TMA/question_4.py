import random
from math import floor

def getNamesAndSize():
    """
    Prompt the user to enter the names of player 1 and 2.\n
    Prompt the user to enter size of the board.\n
    Return  the names of both players (string) and size of the board (int)
    """
    player_1 = input("Enter player 1 name: ")
    player_2 = input("Enter player 2 name: ")
    while player_1.lower() == player_2.lower():
        print('The name entered must be different!')
        player_2 = input("Enter player 2 name: ")
    size = int(input("Size of game board: "))
    while (size % 2 == 0 or size < 3):
        print('The size of board must be odd and at least 3!')
        size = int(input("Size of game board: "))
    return {
        'player_1': player_1, 
        'player_2': player_2,
        'size': size
    }

def getNewBoard(size: int):
    """
    Return a new board represented by 2 dimenisional list with dimension of size x size.\n
    All the items in the list is initalised with value of '-'.
    """
    list = []
    for i in range (0, size, 1):
        row = []
        for n in range (0, size, 1):
            row.append('-')
        list.append(row)
    return list

def printBoard(list: list):
    """
    Print a square board with size equal to the length of list.\n
    Each item in the list represents a row on the board.\n
    First item in list represents first row on the board.\n
    Last item in the list represents last row on the board.\n
    list[x][y] represents the x row and y column of the board.
    """
    rowHead = '\n  '
    for i in range(0, len(list) - 1, 1):
        rowHead += '{0} '.format(i)
    rowHead += '{0}'.format(len(list) - 1)
    print(rowHead)

    for i in range(0, len(list), 1):
        string = '{0} '.format(i)
        for n in range(0, len(list[i]) - 1, 1):
            string += '{0} '.format(list[i][n])
        string += '{0}'.format(list[i][len(list) - 1])
        print(string)

def getNextTile(name: str, symbol: str):
    """
    Prompt the player which 2 squares on the board to place his tile.\n
    Return the 2 squares based on the user input.
    """
    stringInput = input('\n{0}, place your {1} tile: '.format(name, symbol))
    splitInput = stringInput.split(' ')
    square_1 = splitInput[0]
    square_2 = splitInput[1]
    return(square_1, square_2)

def isSquaresWithinBoundary(square_1: str, square_2: str, list: list):
    """
    Validate that both square_1 and square_2 are within the boundary of the \n
    board defined by the list.
    """
    square_1x = int(square_1[0])
    square_1y = int(square_1[1])
    square_2x = int(square_2[0])
    square_2y = int(square_2[1])
    return (
        (square_1x >= 0 and square_1x <= len(list) - 1) and
        (square_1y >= 0 and square_1y <= len(list) - 1) and
        (square_2x >= 0 and square_2x <= len(list) - 1) and
        (square_2y >= 0 and square_2y <= len(list) - 1)
    )
    
def isSquareNotOccupied (square_1: str, square_2: str, list: list):
    """
    Validate that both square_1 and square_2 are not occupied on \n
    the board defined by the list.
    """
    square_1x = int(square_1[0])
    square_1y = int(square_1[1])
    square_2x = int(square_2[0])
    square_2y = int(square_2[1])
    return (
        list[square_1x][square_1y] == '-' and
        list[square_2x][square_2y] == '-'
    )

def isBothSquaresVertical(square_1: str, square_2: str, list: list):
    """
    Validate that both square_1 and square_2 are vertical.
    """
    square_1x = int(square_1[0])
    square_1y = int(square_1[1])
    square_2x = int(square_2[0])
    square_2y = int(square_2[1])
    return (
        (square_2y == square_1y) and 
        (square_2x == square_1x - 1 or square_2x == square_1x + 1)
    )

def isBothSquaresHorizontal(square_1: str, square_2: str, list: list):
    """
    Validate that both square_1 and square_2 are horizontal.
    """
    square_1x = int(square_1[0])
    square_1y = int(square_1[1])
    square_2x = int(square_2[0])
    square_2y = int(square_2[1])
    return (
        (square_2x == square_1x) and 
        (square_2y == square_1y - 1 or square_2y == square_1y + 1)
    )

def validateTile(square_1: str, square_2: str, list: list):
    """
    Validate that both square_1 and square_2 are within the boundary of board defined by list.\n
    Validate that both square_1 and square_2 are not occupied on the board defined by list.\n
    Validate the both square_1 and square_2 are either horizontal or vertical.\n
    If one of the above validations fail, return False.\n
    Otherwise, return True.
    """
    result = True
    if (not isSquaresWithinBoundary(square_1, square_2, list)):
        print("Squares are out of the boundary of board!!")
        result = False
    elif (not isSquareNotOccupied (square_1, square_2, list)):
        print("Square occupied!!")
        result = False
    elif(
        not isBothSquaresVertical(square_1, square_2, list) and
        not isBothSquaresHorizontal(square_1, square_2, list)
    ):
        print("The squares must be vertical or horizontal!!")
        result = False

    return result

def placeTitle(square_1: str, square_2: str, symbol: str, list: list):
    """
    Update which of the 2 squares on the board represented by list are occupied by symbol
    based on square_1 and square_2.\n
    Print the board based on the updated list.
    """
    square_1x = int(square_1[0])
    square_1y = int(square_1[1])
    square_2x = int(square_2[0])
    square_2y = int(square_2[1])
    list[square_1x][square_1y] = symbol
    list[square_2x][square_2y] = symbol
    printBoard(list)

def isTileOccupiedBySymbol(list: list, symbol: str):
    """
    If the any of the square on the board represented by list is occupied by the symbol, return True.\n
    Otherwise, return False.
    """
    for i in range (0, len(list), 1):
        for n in range(0, len(list), 1):
            if (list[i][n] == symbol):
                return True
    return False

def isGameAlive(list: list, symbolMap: dict, player_1: str, player_2: str):
    """
    Validate the game is still alive.\n
    If board is not occupied by both players yet, return True.\n
    If board is occupied by both players and there are at least two horizontal squares or 
    two vertical squares, return True.\n
    Otherwise, return False.
    """
    if (
        isTileOccupiedBySymbol(list, symbolMap.get(player_1)) and
        isTileOccupiedBySymbol(list, symbolMap.get(player_2))
    ):
        for i in  range (0, len(list), 1):
            for n in range (0, len(list) - 1, 1):
                if (list[i][n] == '-' and list[i][n + 1] == '-'):
                    return True
        for i in  range (0, len(list), 1):
            for n in range (0, len(list) - 1, 1):
                if (list[n][i] == '-' and list[n + 1][i] == '-'):
                    return True
        return False
    return True

"""
Initalised the data for the game.
"""
namesAndSize = getNamesAndSize()
player_1 = namesAndSize.get('player_1')
player_2 = namesAndSize.get('player_2')
size = namesAndSize.get('size')
symbolMap = {
    player_1: 'X',
    player_2: 'O'
}
toContinueAnotherRound = True

def randomisedPlayer(player_1: str, player_2: str):
    randomNum = floor(random.random() * 2)
    if random == 0:
        return player_1
    return player_2

"""
Control loop for the game to continue in another round.
This loop will termiate if there is a winner in the game.
"""
while(toContinueAnotherRound):
    list = getNewBoard(size)
    numOfTilePlaced = {
        player_1: 0,
        player_2: 0
    }
    isNextPlayerTurn = True
    currentPlayer = randomisedPlayer(player_1, player_2)
    printBoard(list)
    """
    Control loop for next player to place his tile.\n
    This loop will terminate if there are no available squares on the board
    for the player to place his tile after both players have placed their tiles.
    """
    while (isNextPlayerTurn):
        (square_1, square_2) = getNextTile(currentPlayer, symbolMap.get(currentPlayer))
        while(not validateTile(square_1, square_2, list)):
            (square_1, square_2) = getNextTile(currentPlayer, symbolMap.get(currentPlayer))
        placeTitle(square_1, square_2, symbolMap.get(currentPlayer), list)
        if currentPlayer == player_1:
            numOfTilePlaced[player_1] += 1
        else:
            numOfTilePlaced[player_2] += 1
        if (not isGameAlive(list, symbolMap, player_1, player_2)):
            isNextPlayerTurn = False
        else:
            if currentPlayer == player_1:
                currentPlayer = player_2
            else:
                currentPlayer = player_1
    """
    Announce the result for this round of game.
    """
    if (numOfTilePlaced[player_1] == numOfTilePlaced[player_2]):
        print ('\nIt is a tie !! Rematch')
    else:
        winner = player_1
        if (numOfTilePlaced[player_2] >  numOfTilePlaced[player_1]):
            winner = player_2
        print('\n{0} {1} - {2} {3}'.format(player_1, numOfTilePlaced[player_1], player_2, numOfTilePlaced[player_2]))
        print('{0} is the winner'.format(winner))
        toContinueAnotherRound = False










