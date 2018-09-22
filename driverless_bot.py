from AlbotOnline.Snake.SnakeGame import SnakeGame
import random

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


game = SnakeGame()
while(game.awaitNextGameState() == "ongoing"):
    board = game.currentBoard
    board.printBoard()
    
    # print(board.grid[x][y])

    playerMoves, enemyMoves = game.getPossibleMoves(board)
    
    game.makeMove(random.choice(playerMoves))