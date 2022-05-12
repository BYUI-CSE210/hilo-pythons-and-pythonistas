
"""
    Update the code and the comments as you change the code for your game.  You will be graded on following the
    Rules listed and your program meets all of the Requirements found on 
    https://byui-cse.github.io/cse210-course-competency/abstraction/materials/hilo-specification.html
"""


class Director:
    playerClass = Player()
    gameClass = Game()
    guess = ''
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        self.guess = input('Higher or lower? (h/l) ')
        pass

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if self.gameClass.newCard > self.gameClass.prevCard:
            if self.guess == 'h':
                self.playerClass.addPoints()
            elif self.guess == 'l':
                self.playerClass.removePoints()

        if self.gameClass.newCard < self.gameClass.prevCard:
            if self.guess == 'l':
                self.playerClass.addPoints()
            if self.guess == 'h':
                 self.playerClass.removePoints() 

        if self.playerClass.score <= 0:
            self.is_playing = False          

        if not self.is_playing:
            return

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        print(f'Your current score is: {self.playerClass.score}')
        if self.is_playing == False:
            print('You have lost. How unlucky.')
        
        if self.is_playing == True:
            yesOrNo = input('Would you like to play again? (y/n) ')
            if yesOrNo == 'n':
                exit()
    

        if not self.is_playing:
            return
