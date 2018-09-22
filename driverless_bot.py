from AlbotOnline.Snake.SnakeGame import SnakeGame
import random, math

game = SnakeGame()


def getPos(board, x,y):
    return board.grid(x,y)

def getNeighbors(x,y):
    return set((x-1,y),(x,y-1),(x+1,y),(x,y+1))

def inBounds(x,y, grid_size=10):
    border = grid_size-1
    return not (x < 0 or y < 0 or y > border or x > border)

def isBlocked(board, x,y):
    return board.grid[x][y] in ['X','E','P'] or not inBounds(x,y)

def isNotEnclosed(board,x,y):
    return sum(map(isBlocked, getNeighbors(x,y))) < 3

def isFreeSpace(board,x,y):
    if not inBounds(x,y):
        return False
    return not isBlocked(board,x,y)

def freeSpacesInRadius(board,x,y,radius):
    spaces = 0
    for i in range(-radius,radius,1):
        for j in range(-radius,radius,1):
            spaces += isFreeSpace(board,x+i,y+j)
    return spaces

def distanceToEnemy(board):
    return math.sqrt((board.player.x-board.enemy.x)**2+(board.player.y-board.enemy.y)**2)

def freeSpacesInDirection(board,x,y,direction):
    spaces = 0
    directionInt = ['right','up','left','down'].index(direction)
    factor = [1,1,-1,-1][directionInt]
    i=0
    while(isFreeSpace(board,x+factor*i,y) if directionInt%2==0 else isFreeSpace(board,x,y+factor*i)):
        i+=1
        spaces+=1
    return spaces

def main():
    while(game.awaitNextGameState() == "ongoing"):
        board = game.currentBoard

        playerMoves, enemyMoves = game.getPossibleMoves(board)
        rankedMoves = list(map(lambda x: evalMove(board,x,1), playerMoves))
        rankedMoves.sort(key=lambda tup: tup[0], reverse=True)

        print(rankedMoves)

        game.makeMove(rankedMoves[0][1])


def evalMove(board,direction,depth):
    #return miniMax(game.simulateMove(board,direction,board.player.dir),True,depth,simpleEval), direction
    return simpleEval(game.simulateMove(board,direction,board.enemy.dir)),direction

def miniMax(board, maxiPlayer, depth, eval):
    print('Recursion: ',depth)
    if not depth or game.evaluateBoard(board) != 'ongoing':
        return eval(board)

    playerMoves, enemyMoves = game.getPossibleMoves(board)
    children = map(lambda x: game.simulateMove(board, x, board.enemy.dir), playerMoves) if maxiPlayer else map(lambda x: game.simulateMove(board, board.player.dir, x), enemyMoves)
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
    p = board.player
    free5 = freeSpacesInRadius(board, p.x, p.y, 2)
    free3 = freeSpacesInRadius(board, p.x, p.y, 1)
    dist = distanceToEnemy(board)
    freeDir = freeSpacesInDirection(board, p.x, p.y, p.dir)
    state = game.evaluateBoard(board)
    print(state)
    if state == 'enemyWon' or state == 'draw':
        return -10
    else:
        return free5/25 + 3*(free3-4)/9 - 3*(dist-3)/14 + (freeDir-3)/9


main()

