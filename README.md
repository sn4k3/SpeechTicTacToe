# SpeechTicTacToe
A basic text based tic tac toe game using voice commands.
Speech a free position number to play against the computer.

# How to play
* Run 'tictactoe.py' with Python 3.3+
* Follow console instructions
* Speech a free position number to play against the computer.

# Game board


	===========================
		TIC-TAC-TOE
	===========================

	          |     |     
	       1  |  2  |  3
	     _____|_____|_____
	          |     |     
	       4  |  5  |  6
	     _____|_____|_____
	          |     |     
	       7  |  8  |  9  
	          |     |
	          
	Turn: Human
    HINT: To make a move Speech a free position number.


# Voice Recognition

In order to improve the quality of the results we use Google API first, if it fails or no network it will use Sphinx in fail-over case.


# Requirements
* Python 3.3+ (required)
* PyAudio 0.2.9+ (required only if you need to use microphone input, Microphone)
* PocketSphinx (required only if you need to use the Sphinx recognizer, recognizer_instance.recognize_sphinx)
* FLAC encoder (required only if the system is not x86-based Windows/Linux/OS X)

