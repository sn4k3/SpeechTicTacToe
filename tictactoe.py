"""
Tiago Conceição
m35767
Project 1 - Tic-Tac-Toe
Multi-modal Systems

Tic Tac Toe game
Speech a free position number to play against the computer
"""

import random
import sys

# 0 = Easy, 1 = Normal, 2 = Hard
difficulty = 0
grid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
game = None
playerTurn = True
playerSymbol = {True: 'X', False: 'O'}
playerName = {True: 'Human', False: 'Computer AI'}
gameOver = False


def buildGame():
    global game
    game = """
\t          |     |     
\t       %(g0)s  |  %(g1)s  |  %(g2)s
\t     _____|_____|_____
\t          |     |     
\t       %(g3)s  |  %(g4)s  |  %(g5)s
\t     _____|_____|_____
\t          |     |     
\t       %(g6)s  |  %(g7)s  |  %(g8)s  
\t          |     |
""" % {'g0': grid[0], 'g1': grid[1], 'g2': grid[2], 'g3': grid[3], 'g4': grid[4], 'g5': grid[5], 'g6': grid[6],
       'g7': grid[7], 'g8': grid[8]}


def renderGame():
    if gameOver:
        return
    print('\n\t===========================\n\t\tTIC-TAC-TOE\n\t===========================')
    buildGame()
    print(game)
    if playerTurn:
        print(' Turn: Human')
        print(' HINT: To make a move Speech a free position number.')
    else:
        print(' Turn: Computer AI - Please wait, thinking....')


def playMove(position):
    global playerTurn
    global gameOver
    if gameOver:
        print('GameOver!')
        return
    if position < 0 or position > 8:
        print('Invalid Move, out of bounds')
        return

    if not grid[position].isdigit():
        print('Invalid move, already placed')
        return

    grid[position] = playerSymbol[playerTurn]
    renderGame()

    if isWinner():
        gameOver = True
        print('Game Over, {0} [{1}] is the winner!'.format(playerName[playerTurn], playerSymbol[playerTurn]))
        return

    playerTurn = not playerTurn
    if not playerTurn:
        computeMove()


# Computer Move (Bot)
def computeMove():
    if difficulty == 0:
        while True:
            position = random.randint(0, 8)
            print(position)
            if grid[position].isdigit():
                playMove(position)
                break


def isWinner():
    le = playerSymbol[playerTurn]
    return ((grid[6] == le and grid[7] == le and grid[8] == le) or  # across the bottom
            (grid[3] == le and grid[4] == le and grid[5] == le) or  # across the middle
            (grid[0] == le and grid[1] == le and grid[2] == le) or  # across the top
            (grid[6] == le and grid[3] == le and grid[0] == le) or  # down the left side
            (grid[7] == le and grid[4] == le and grid[1] == le) or  # down the middle
            (grid[8] == le and grid[5] == le and grid[2] == le) or  # down the right side
            (grid[6] == le and grid[4] == le and grid[2] == le) or  # diagonal Bottom left to top right
            (grid[8] == le and grid[4] == le and grid[0] == le))    # diagonal Top left to bottom right


def restart():
    global grid, playerTurn, gameOver
    grid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    playerTurn = True
    gameOver = False


def main():
    while True:
        renderGame()
        raw = input("Type 'q' to quit or 'r' to restart\n")

        if not gameOver and playerTurn and raw.isdigit() and 1 <= int(raw) <= 9:
            playMove(int(raw) - 1)
            continue
        if raw == 'q':
            sys.exit(1)
            break
        elif raw == 'r':
            restart()
            continue


if __name__ == "__main__":
    main()
