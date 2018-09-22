from AlbotOnline.Snake.SnakeGame import SnakeGame
import random

game = SnakeGame()


def getPos(board, x,y):
    return board.grid(x,y)

def getNeighbors(x,y):
    return set((x-1,y),(x,y-1),(x+1,y),(x,y+1))

def inBounds(x,y, grid_size=10):
    border = grid_size-1
    return x < 0 or y < 0 or y > border or x > border

def isBlocked(board, x,y):
    return board.grid(x,y) in ['X','E','P'] or not inBounds(x,y)

def isNotEnclosed(board,x,y):
    return sum(map(isBlocked, getNeighbors(x,y))) < 3


def main():
    while(game.awaitNextGameState() == "ongoing"):
        board = game.currentBoard
        board.printBoard("Current Board")

        playerMoves, enemyMoves = game.getPossibleMoves(board)

        rankedMoves = list(map(evalMove, playerMoves))

        rankedMoves.sort(key=lambda tup: tup[0], reverse=True)

        print(rankedMoves)

        game.makeMove(rankedMoves[0][1])


def evalMove(direction):
    score = random.randrange(1, 5)

    lastBoard = game.currentBoard
#    for i in range(1000):



    return (score, direction)


def miniMax(board, maxiPlayer, depth, eval):
    if(not depth or game.evaluateBoard(board) != 'ongoing'):
        return eval(board)

    playerMoves, enemyMoves = game.getPossibleMoves(board)
    children = map(lambda x: game.simulateMove(board, x, ''), playerMoves) if maxiPlayer else map(lambda x: game.simulateMove(board, '', x), enemyMoves)
    if maxiPlayer:
        value = -float('inf')
        for child in children:
            value = max(value, miniMax(child, not maxiPlayer, depth-1, eval))
        return value
    else:
        value = float('inf')
        for child in children:
            value = min(value, miniMax(child, not maxiPlayer, depth-1, eval))
        return value

def simpleEval(board):


main()

