import random
import string

WORDLIST_FILENAME = "words.txt"

class Words():
    def __init__(self, guesses):
        self.inFile = ''
        self.line = ''
        self.wordlist = ''
        self.chosenWord = ''
        self.guesses = guesses
        self.wordDifLetters = []

    def differentLettersSize(self):
        return len(self.wordDifLetters)

    def wordListSize(self):
        return len(self.wordlist)

    def loadWordList(self):
        print "Loading word list from file..."

        # inFile: file
        self.inFile = open(WORDLIST_FILENAME, 'r', 0)
        # line: string
        self.line = self.inFile.readline()
        self.wordlist = string.split(self.line)

        print self.wordListSize(), "words loaded."

    def printChangingInfo(self):
        print '---------------------------------------'
        print 'You have only', self.guesses,'guesses'
        print 'Your word have',self.differentLettersSize(),'different letters'
        print 'Changing word...'

    def differentLetters(self):
        self.wordDifLetters = []
        for letter in self.chosenWord:
            if letter in self.wordDifLetters:
                pass
            else:
                self.wordDifLetters.append(letter)

    def randomWord(self):
        self.chosenWord = random.choice(self.wordlist)
        self.differentLetters()

    def chooseWord(self):
        self.loadWordList()
        self.randomWord()

        while self.differentLettersSize() > self.guesses:
            self.printChangingInfo()
            self.randomWord()

        return self.chosenWord
