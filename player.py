'''
Class Author: Alvaro Loran 
Description: This player class will keep track of the points and player guesses.
'''


class Player:
    def __init__(self):
        self.score = 300
        self.currentGuess = int
        self.prevGuess = int

    
    def showPoints(self):
        print(self.score)

    #This class is called by the newGuess method to update the previous guess
    def updatePrevGuess(self):
        self.prevGuess = self.currentGuess

    def newGuess(self, newGuess):
        self.updatePrevGuess()
        self.currentGuess = newGuess

    def addPoints(self):
        self.score += 100

    def removePoints(self):
        self.score -= 75