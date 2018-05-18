import logging
from Classes.words import Words
from Classes.hangman import Hangman

logging.basicConfig(filename='hang.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

def main():
    playerGuesses = 8

    words = Words(playerGuesses)
    secretWord = words.chooseWord().lower()

    hangman = Hangman(secretWord, playerGuesses)

    hangman.printHeader(words)
    hangman.startGame()

if __name__ == '__main__':
    main()
