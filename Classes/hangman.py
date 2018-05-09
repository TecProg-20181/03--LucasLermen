from os import system

class Hangman():
    def __init__(self, secretWord, guesses):
        self.guesses = guesses
        self.secretWord = secretWord
        self.lettersGuessed = []

    def printHeader(self, words):
        print "\033[91m-------------------------------------------------\033[33m"
        print "\033[91mWelcome to the game, Hangam!\033[33m"
        print "\033[91mI am thinking of a word that is\033[33m", len(self.secretWord), "\033[91mletters long.\033[33m"
        print "\033[91mThe word have\033[33m", words.differentLettersSize(), "\033[91mdifferent letters\033[33m"
        print "\033[91m-------------------------------------------------\033[33m"


    def isWordGuessed(self):
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                pass
            else:
                return False

        return True

    def getGuessedWord(self):
        guessed = ''
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                guessed += letter
            else:
                guessed += '_'
        return guessed

    def getAvailableLetters(self):
        import string
        # 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase
        for letter in available:
            if letter in self.lettersGuessed:
                available = available.replace(letter, '')
        return available

    def resultLetter(self, letter):
        if letter in self.lettersGuessed:
            guessed = self.getGuessedWord()
            return 'Oops! You have already guessed that letter: ' + guessed

        self.lettersGuessed.append(letter)
        guessed = self.getGuessedWord()

        if letter in self.secretWord:
            return 'Good Guess: ' + guessed

        self.guesses -=1
        return 'Oops! That letter is not in my word: ' + guessed

    def gameResult(self):
        if self.isWordGuessed():
            return 'Congratulations, you won!'
        else:
            return 'Sorry, you ran out of guesses. The word was ' + self.secretWord + '.'

    def startGame(self):
        while self.isWordGuessed() == False and self.guesses >0:
            print 'You have ', self.guesses, 'guesses left.'

            print 'Available letters', self.getAvailableLetters()
            letter = raw_input('Please guess a letter: ')

            print self.resultLetter(letter)

            print '--------------------------------------------------'

        print self.gameResult()
