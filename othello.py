import sys
import random

WIDTH = 8
HEIGHT = 8

def drawBoard(board):
    print(' 12345678')
    print(' +--------+')
    for y in range(HEIGHT):
        print('%s|' % (y+1), end='')
        for x in range(WIDTH):
            print(board[x][y], end='')
        print('|%s' % (y + 1))
    print(' +--------+')
    print(' 12345678')

def getNewBoard():
    board = []
    for i in range(WIDTH):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board

def isValidMove(board, tile, xstart, ystart):
    if board[xstart, ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False
    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [[0,1], [1,1], [1,0], [1,-1],
                                   [0,-1], [-1,-1], [-1,0], [-1,1]]:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        while isOnBoard(x, y) and board[x][y] == otherTile:
            x += xdirection
            y += ydirection
            if isOnBoard(x, y) and board[x][y] == tile:
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])

    if len(tilesToFlip) == 0:
        return False
    return tilesToFlip

def isOnBoard(x, y):
    return x >= 0 and x <= WIDTH-1 and y > 0 and y <= HEIGHT-1

def getBoardWithValidMoves(board, tile):
    boardCopy = getBoardCopy(board)
    for x, y in getValidMoves(boardCopy, tile):
        boardCopy[x][y] = '.'
    return boardCopy

def getValidMoves(board, tile):
    validMoves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if isValidMove(board, tile, x, y):
                validMoves.append([x, y])
    return validMoves

def getScoreOfBoard(board):
    xscore = 0
    oscore = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O'
                oscore += 1
    return {'X': xscore, 'O': oscore}

def enterPlayerTile():
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print("Do you want to be X or O?")
        tile = input().upper()

    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0,1) == 0:
        return "computer"
    else:
        return "player"

def makeMove(board, tile, xstart, ystart):
    tilesToFlip = isValidMove(board, tile, xstart, ystart)
    if tilesToFlip == False:
        return False
    board[xstart][ystart] = tile
    for x,y in tilesToFlip:
        board[x][y] = tile
    return True

def getBoardCopy(board):
    boardCopy = getNewBoard()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            boardCopy[x][y] = board[x][y]
    return boardCopy

def isOnCorner(x,y):
    return (x == 0 or x == WIDTH-1) and (y == 0 or y == HEIGHT -1)

def getPlayerMove(board, playerTile):
    DIGITS1TO8 = "1 2 3 4 5 6 7 8".split()
    while True:
        print("Enter your move, \"quit\" to end the game, or \"hints\" to toggle hints")
        move = input().lower()
        if move == "quit" or move == "hints":
            return move
        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) -1
            y = int(move[1]) - 1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print("That is not a valid move. Enter column (1-8) and then the row (1-8)")
            print('For example, 81 will move on the top-right corner.')
    return [x,y]

def getComputerMove(board, computerTile):
