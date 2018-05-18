import logging
from Classes.words import Words
from Classes.hangman import Hangman

logging.basicConfig(filename='hang.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

def main():
    playerGuesses = 8

    try:
        words = Words(playerGuesses)
        logging.info('Created words object')
    except:
        print 'Unable to create words object'
        print 'Shutting down...'
        exit(1)

    secretWord = words.chooseWord().lower()

    try:
        hangman = Hangman(secretWord, playerGuesses)
        logging.info('Created hangman object')
    except:
        print 'Unable to create hangman object'
        print 'Shutting down...'
        exit(1)

    hangman.printHeader(words)
    hangman.startGame()

if __name__ == '__main__':
    main()
