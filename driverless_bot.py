from AlbotOnline.Snake.SnakeGame import SnakeGame
import random

game = SnakeGame()


def getPos(board, x,y):
    return board.grid(x,y)

def getNeighbors(x,y):
    return set((x-1,y),(x,y-1),(x+1,y),(x,y+1))

def inBounds(x,y, grid_size=10):
    border = grid_size-1
    x < 0 or y < 0 or y > border or x > border

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

    return (score, direction)



main()