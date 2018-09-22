from AlbotOnline.Snake.SnakeGame import SnakeGame
from multiprocessing import Pool
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




def evalMove(direction):
    score = 0

    lastBoard = game.currentBoard
    playerMoves, enemyMoves = game.getPossibleMoves(lastBoard)
    moveeval = game.evaluateBoard(game.simulateMove(lastBoard, direction, enemyMoves[0]))
    if (moveeval == "enemyWon"):
        return (-1000, direction)

    iterations = 15
    for i in range(iterations):
        score += run_test_game(game.simulateMove(lastBoard, direction, enemyMoves[0]))
    for i in range(iterations):
        score += run_test_game(game.simulateMove(lastBoard, direction, enemyMoves[1]))
    for i in range(iterations):
        score += run_test_game(game.simulateMove(lastBoard, direction, enemyMoves[2]))

    return (score, direction)


def run_test_game (board):
    simBoardState = game.evaluateBoard(board)

    if (simBoardState == "ongoing"):
        playerMoves, enemyMoves = game.getPossibleMoves(board)
        simBoard = game.simulateMove(board, random.choice(playerMoves), random.choice(enemyMoves))
        return run_test_game(simBoard)
    elif (simBoardState == "enemyWon"):
        return -1
    else:
        return 1




pool = Pool(processes=3)


def main():
    while(game.awaitNextGameState() == "ongoing"):
        board = game.currentBoard

        playerMoves, enemyMoves = game.getPossibleMoves(board)

        rankedMoves = list(pool.map(evalMove, playerMoves))

        rankedMoves.sort(key=lambda tup: tup[0], reverse=True)

        print(rankedMoves)

        game.makeMove(rankedMoves[0][1])



main()