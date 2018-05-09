from Classes.words import Words
from Classes.hangman import Hangman

playerGuesses = 8

words = Words(playerGuesses)
secretWord = words.chooseWord().lower()

hangman = Hangman(secretWord, playerGuesses)

hangman.printHeader(words)
hangman.startGame()
