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
    return not (x < 0 or y < 0 or y > border or x > border)

def isBlocked(grid, x,y):
    return grid[x][y] in ['X','E','P'] or not inBounds(x,y)

def isFreeSpace(grid,x,y):
    if not inBounds(x,y):
        return False
    return not isBlocked(grid,x,y)


def isNotEnclosed(board,x,y):
    return sum(map(isBlocked, getNeighbors(x,y))) < 3

def positions(grid):
    enemy = (0, 0)
    player = (0, 0)
    for x in range(9):
        for y in range(9):
            if grid[x][y] == "E":
                enemy = (x,y)
            elif grid[x][y] == "P":
                player = (x, y)
    return (player, enemy)

def simulate_move(board, playerMove, enemyMove):
    print("Not implemented")

def evaluateBoard(grid):
    print("Not implemented")

def getPossibleMoves(grid):
    print("Not implemented")
    player, enemy = positions(grid)
    playerNeighbours = getNeighbors()









def evalMove(direction):
    score = 0

    lastBoard = game.currentBoard
    playerMoves, enemyMoves = game.getPossibleMoves(lastBoard)
    moveeval = game.evaluateBoard(game.simulateMove(lastBoard, direction, enemyMoves[0]))
    if (moveeval == "enemyWon"):
        return (-1000, direction)

    print ("start calculating")

    iterations = 70
    for i in range(iterations):
        score += numeric_test_game(game.simulateMove(lastBoard, direction, enemyMoves[0]).grid, direction, enemyMoves[0], 1)
    for i in range(iterations):
        score += numeric_test_game(game.simulateMove(lastBoard, direction, enemyMoves[1]).grid, direction, enemyMoves[1], 1)
    for i in range(iterations):
        score += numeric_test_game(game.simulateMove(lastBoard, direction, enemyMoves[2]).grid, direction, enemyMoves[2], 1)

    return (score, direction)




def numeric_test_game (grid, playerDir, enemyDir, deapth):
    player, enemy = positions(grid)

    playerX, playerY = player
    enemyX, enemyY = enemy

    allDir = ["right", "up", "left", "down"]

    while True:

        if deapth > 30:
            return 0

        possiblePlayerMoves = [x for x in allDir if x != playerDir]
        possibleEnemyMoves = [x for x in allDir if x != enemyDir]
        playerDir = random.choice(possiblePlayerMoves)
        enemyDir = random.choice(possibleEnemyMoves)

        oldPlayerX = playerX
        oldPlayerY = playerY


        oldEnemyX = enemyX
        oldEnemyY = enemyY

        if enemyDir == "right":
            enemyX += 1
        elif enemyDir == "left":
            enemyX -= 1
        elif enemyDir == "up":
            enemyY += 1
        else:
            enemyY -= 1

        if (isFreeSpace(grid, enemyX, enemyY)):
            grid[enemyX][enemyY] = "E"
            grid[oldEnemyX][oldEnemyY] = "X"
        else:
            return (100 / deapth)*(100 / deapth)




        if playerDir == "right":
            playerX += 1
        elif playerDir == "left":
            playerX -= 1
        elif playerDir == "up":
            playerY += 1
        else:
            playerY -= 1

        if (isFreeSpace(grid, playerX, playerY)):
            grid[playerX][playerY] = "P"
            grid[oldPlayerX][oldPlayerY] = "X"
        else:
            return -(100 / deapth)*(100 / deapth)




        deapth += 1






def main():
    while(game.awaitNextGameState() == "ongoing"):
        board = game.currentBoard

        playerMoves, enemyMoves = game.getPossibleMoves(board)

        rankedMoves = list(map(evalMove, playerMoves))

        rankedMoves.sort(key=lambda tup: tup[0], reverse=True)

        print(rankedMoves)

        game.makeMove(rankedMoves[0][1])


if __name__ == "__main__":
    main()