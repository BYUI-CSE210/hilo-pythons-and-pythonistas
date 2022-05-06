# hilo
Starter template for the Hilo game
Update the readme with the rules for the game and the name of your team members.

# Rules
Hilo is played according to the following rules.

The player starts the game with 300 points.
Individual cards are represented as a number from 1 to 13.
The current card is displayed.
The player guesses if the next one will be higher or lower.
The the next card is displayed.
The player earns 100 points if they guessed correctly.
The player loses 75 points if they guessed incorrectly.
If a player reaches 0 points the game is over.
If a player has more than 0 points they decide if they want to keep playing.
If a player decides not to play again the game is over.

# Team Members Names
Gloria Estrella Navarrete

Team Assignments:

Alvaro: Player class

Gloria: Game class

Camden: Main (Pt. 1)
	-display prev. card
	-display the guess
	-dispaly next/current cards
	-compare guess to current and prev card

Chris: Main (Pt.2)
	-Determine score and display it/ provide it to player class
	-Ask player if they want to play again. (Y/N)
	-Display win/lose message.


Game Design:

	player (Class) 
Responsibility: 
	- Keep track of points.

Behaviors:
	- show points 
	- keep track of guess
	- add points
	- remove points 

State:
	- points
	- guess



	Game (class)
Responsibility:
	- Keep track of cards and guess. 

Behaviors:
	- display states (The card is: ? AND Next card was: ?)
	- generate random card
	- update current card state
	- update prev. card state

State: 
	- Prev. card
	- Current card

	

	Main (function)

Responsibility:

Behaviors:
	-display prev. card
	-display the guess
	-dispaly next/current cards
	-compare guess to current and prev card
	-Determine score and display it/ provide it to player class
	-Ask player if they want to play again. (Y/N)
	-Display win/lose message. 