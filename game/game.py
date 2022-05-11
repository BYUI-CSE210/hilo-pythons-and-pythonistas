from random import randint

class Game:
    """Handles the cards"""

    def __init__(self):
        """constructs a new game
        
        args:
            self(Game):an instance of the game 
        """

        self.current = ''
        self.next = ''

    def innitialize(self):
        """Draws an innitial card.
        
        Args:
            self(Game):an instance of the game
        """
        self.current = randint(1,13)
    

    def draw_card(self):
        """
        Draws the next card.

        Args:
            self(Game):an instance of the game
        
        """


        self.next = randint(1,13)

    def next_turn(self):
        """
        Turns the "next card" into the "current" card in preparation for the nexdt turn.

        Args:
            self(Game):an instance of the game
        """
        self.current = self.next
