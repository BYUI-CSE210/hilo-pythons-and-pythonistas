'''
Class Author: Alvaro Loran 
Description: This player class will keep track of the points and player guesses.
'''


class Player:
    def __init__(self):
        self.score = 300

    
    def showPoints(self):
        print(self.score)


    def addPoints(self):
        self.score += 100

    def removePoints(self):
        self.score -= 75