def getNamesAndSize():
    player_1 = input("Enter player 1 name: ")
    player_2 = input("Enter player 2 name: ")
    while player_1.lower() == player_2.lower():
        player_2 = input("Enter player 2 name: ")
    size = int(input("Size of game board: "))
    while (size % 2 == 0 or size < 3):
        size = int(input("Size of game board: "))
    return {
        'player_1': player_1, 
        'player_2': player_2,
        'size': size
    }

def getNewBoard(size):
    list = []
    for i in range (0, size, 1):
        row = []
        for n in range (0, size, 1):
            row.append('-')
        list.append(row)
    return list

def printBoard(list):
    rowHead = '  '
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

def getNextTile(name, symbol):
    stringInput = input('{0}, place your {1} tile: '.format(name, symbol))
    splitInput = stringInput.split(' ')
    square_1 = splitInput[0]
    square_2 = splitInput[1]
    return(square_1, square_2)

def isSquaresWithinBoundary(square_1, square_2, list):
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
    
def isSquareNotOccupied (square_1, square_2, list):
    square_1x = int(square_1[0])
    square_1y = int(square_1[1])
    square_2x = int(square_2[0])
    square_2y = int(square_2[1])
    return (
        list[square_1x][square_1y] == '-' and
        list[square_2x][square_2y] == '-'
    )

def isBothSquaresVertical(square_1, square_2, list):
    square_1x = int(square_1[0])
    square_1y = int(square_1[1])
    square_2x = int(square_2[0])
    square_2y = int(square_2[1])
    return (
        (square_2y == square_1y) and 
        (square_2x == square_1x - 1 or square_2x == square_1x + 1)
    )

def isBothSquaresHorizontal(square_1, square_2, list):
    square_1x = int(square_1[0])
    square_1y = int(square_1[1])
    square_2x = int(square_2[0])
    square_2y = int(square_2[1])
    return (
        (square_2x == square_1x) and 
        (square_2y == square_1y - 1 or square_2y == square_1y + 1)
    )

def validateTile(square_1, square_2, list):
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

def placeTitle(square_1, square_2, symbol, list):
    square_1x = int(square_1[0])
    square_1y = int(square_1[1])
    square_2x = int(square_2[0])
    square_2y = int(square_2[1])
    list[square_1x][square_1y] = symbol
    list[square_2x][square_2y] = symbol
    printBoard(list)

namesAndSize = getNamesAndSize()
player_1 = namesAndSize.get('player_1')
player_2 = namesAndSize.get('player_2')
size = namesAndSize.get('size')
list = getNewBoard(size)
symbol = {
    player_1: 'X',
    player_2: 'O'
}
currentPlayer = player_1
printBoard(list)

(square_1, square_2) = getNextTile(currentPlayer, symbol.get(currentPlayer))
while(not validateTile(square_1, square_2, list)):
    (square_1, square_2) = getNextTile(currentPlayer, symbol.get(currentPlayer))
placeTitle(square_1, square_2, symbol.get(currentPlayer), list)








