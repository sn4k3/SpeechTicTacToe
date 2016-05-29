#!/usr/bin/python
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
import speech_recognition as sr

# 0 = Easy, 1 = Normal, 2 = Hard
difficulty = 0
grid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
game = None
playerTurn = True
playerSymbol = {True: 'X', False: 'O'}
playerName = {True: 'Human', False: 'Computer AI'}
gameOver = False

answers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

r = sr.Recognizer()


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
    print('\n\t===========================\n\t\tTIC-TAC-TOE\n\t===========================')
    buildGame()
    print(game)

    if gameOver:
        return

    if playerTurn:
        print(' Turn: Human')
        print(' HINT: To make a move Speech a free position number.')
        waitForHumanInput()
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
        if playerTurn:
            waitForHumanInput()
        return

    if not grid[position].isdigit():
        print('Invalid move, already placed')
        if playerTurn:
            waitForHumanInput()
        return

    grid[position] = playerSymbol[playerTurn]


    if isWinner():
        gameOver = True
        renderGame()
        print('Game Over, {0} [{1}] is the winner!'.format(playerName[playerTurn], playerSymbol[playerTurn]))
        return

    playerTurn = not playerTurn
    renderGame()
    if not playerTurn:
        computeMove()


# Computer Move (Bot)
def computeMove():
    if difficulty == 0:
        while True:
            position = random.randint(0, 8)
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
            (grid[8] == le and grid[4] == le and grid[0] == le))  # diagonal Top left to bottom right


def restart():
    global grid, playerTurn, gameOver
    grid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    playerTurn = True
    gameOver = False


def waitForHumanInput():
    if gameOver or not playerTurn:
        return

    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    text = None
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        text = r.recognize_google(audio)
        processTextFromAudio(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    if text is None:
        # recognize speech using Sphinx
        try:
            text = r.recognize_sphinx(audio)
            processTextFromAudio(text)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))


def processTextFromAudio(text):
    if text.isdigit():
        text = int(text)
        if text < 1 or text > 9:
            print('Invalid Move, out of bounds, try again')
            waitForHumanInput()
            return
        else:
            playMove(text-1)
            return
    else:
        if text in answers:
            playMove(answers[text])
            return

    print('Invalid Move, not recognized "{0}", try again'.format(text))
    waitForHumanInput()
    return


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
