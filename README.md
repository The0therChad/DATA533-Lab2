# **CardGame Package Documentation**

[![Build Status](https://app.travis-ci.com/The0therChad/DATA533-Lab3.svg?branch=main)](https://app.travis-ci.com/The0therChad/DATA533-Lab3)

## **Cards Subpackage**

The cards subpackage contains three modules that define playing cards, with classes to make a deck and hands containing cards.

### **card Module**

The card module defines the "Card" class accepting parameters for the rank of the card and the suit of the card. The class checks to make sure both the rank and the suit are accetable values corresponding to a typical deck of playing cards. A list also initialized to give point values to each rank of card. Specifically, counting face cards as 10, and aces as 11.

- **\_\_str__ / \_\_repr__** defines the string representation of the Card objects to display the proper rank and suit in plaintext.
- **getColour** returns the colour of a card, as a string,  corresponding to its suit.
- **getRank** returns the rank of a card as a string.
- **getSuit** returns the suit of a card as a string.
- **getValue** returns the value of a card, as an integer, based on its rank by pulling the corresponding point value from the list, by index, in the Card class.
- **\_\_eq__ / \_\_ne__** defines method to check whether two cards are the same or not.
- **setPoints** class method that allows you to redefine the point values that correspond to each card rank.

### **hand Module**

The hand module defines the "Hand" class accepting a single parameter as a list of "Card" objects as defined above.

- **getTotalPoints** returns the sum of the card values in the hand.
- **discardByCard** accepts a single "Card" object as a parameter, then removes the card matching the provided card from the hand. Returns the removed card as a "Card" object.
- **discardByIndex** accepts an integer as a parameter for the index, then removes the card in the hand at the corresponding index. Returns the removed card as a "Card" object.
- **discardHand** removes every card from the hand by setting the hand to an empty list.
- **addCard** accepts a single "Card" object as a parameter, then adds that card to the hand.
- **addCards** accepts a single parameter as a list of "Card" objects and adds them to the current hand. The function checks to make sure the list contains only "Card" objects.
- **search** accepts two optional parameters for suit and rank as strings used to search the hand for any instance of a card matching one or both of the given parameters. Returns an integer for the index of the searched card in the hand, and an empty search returns all indices.
- **\_\_add__** defines addition for two "Hand" objects, returning a new hand containing the contents of both hands added together.
- **\_\_str__** defines the string representation of a hand.

### **deck Module**

The deck module defines the "Deck" class which inherits from the "Hand" class and initializes a full 52 card deck with one of each card in a list.

- **shuffle** uses the shuffle function from the random package to shuffle the order of the cards in the deck.
- **drawCard** removes the top card from the deck and returns it. Uses the pop function to remove and return the last item from the list of cards that make up the deck.
- **drawCards** accepts an optional integer parameter to draw some number of cards from the top of the deck. This function then calls the "drawCard" function defined above the corresponding number of times and returns a list of the cards drawn.
- **addToBottom** accepts a "Card" object as a parameter, and adds it to the top of the deck by inserting it into the first position of the list of cards that make up the deck.
- **addCard** this function calls the "addToBottom" method. This function is needed to overwrite the parent class's method to prevent adding a card to the top of the deck.

## **Blackjack Subpackage**

### **money Module**

The money module defines the "Money" class, which handles the money for the player, implementing betting and payouts for blackjack. Takes an optional parameter to define the starting amount of money.

- **bet** prompts the user for an integer input to define the desired bet value. Checks input to verify integer type, and prompts again if it is not. Returns the bet amount as an integer.
- **payout** accepts two parameters, amount(int) of the bet, and multiplier(int or float) to payout money in the event of a winning bet. The function returns an integer value corresponding to the amount of money won(amount * multiplier).
- **blackjack** accepts one parameter for the amount(int) of the bet to payout money in the event of a blackjack for the player. Prints a message and returns an integer value corresponding to the amount of money won.
- **deal_blackjack** prints out a message in the event of a dealer blackjack.
- **setWin** a class method that accepts one parameter as an integer to change the money total required to win the game.

### **person Module**

The person module contains two classes, one to define a player for blackjack, and the other to define the dealer for the game. The "Player" class accepts two optional parameters to initialize their hand and money for the game. It also contains functions to manage their hand and money. The "Dealer" class inherits from the "Player" class and accepts an extra parameter, as a "Deck" object, as they dealer will be managing the deck for the game.

- **Player Class** accepts two parameters hand(Hand object) and money(Money object) to initialize the player's hand and money pool.

  - **getHandPoints** counts the total number of points in the player's hand while accounting for multiple aces by counting the first ace as 11, and each subsequent ace as 1. Returns an integer value for the total points in the hand.
  - **addToHand** accepts one parameter as a "Hand" object to add cards to the player's hand. If the player has no hand, then the input becomes their hand.
  - **addCardToHand** accepts a single parameter as a "Card" object to add it to the hand.
  - **showMoney** returns a string displaying the current amount of money in the player's pool, and the amount required to win the game.
  - **discardHand** calls the "discardHand" function on the player's hand to empty their hand.
  - **displayHand** returns a string displaying the player's hand and the total point value of their hand by calling the "getHandPoints" function on the hand.
  - **hit_stand** checks if the player has a natural blackjack, then prompts them for input to either hit or stand. The function will return True if the player hit, False if they stand, and prompt for input again if they offered invalid input.

- **Dealer Class** inherits from the "Player" class, taking the same "Hand" and "Money" parameters as well as a "Deck" parameter.
  
  - **dealCard** returns a card as a "Card" object by drawing one from the deck with the "drawCard" function on the deck.
  - **dealHand** accepts a single integer parameter to define the desired hand size. Returns a "Hand" object containing the defined number of cards as drawn from the deck by calling the "dealCard" function on itself for 1 card, or the "drawCards" function on the deck for multiple.
  - **hit_stand** overwrites the "hit_stand" function from the parent "Player" class to remove the prompts, as the dealer's play is autonomous and defined by point values of their hand. The dealer will hit until their hand value totals 17 or more. Returns a boolean, False if the dealer's play is done, and True if the dealer gets to hit again.

### **game Module**

The game module defines the "Game" class, which initializes the starting game state for blackjack, and contains functions to begin and manage the play of the game. Accepts one optional parameter to define the number of players(multiple players is not implemented at this time). The game is initialized by creating a deck, shuffling it, giving it to the dealer, initializing each player with the default starting amount of money, then dealing two cards to the player and one card to the dealer using the corresponding functions as defined above.

- **newRound** this function reinitializes the deck, shuffles it, and deals new hands to the player and dealer by calling the corresponding functions again.
- **run** this function begins the game:
  - Tracking whether the game is still live, then starting by showing the player's starting money and prompting for a bet.
  - Prints the player's hand, then the dealer's hand.
  - Deals one more card to the dealer, but does not show the user.
  - It is now the player's turn to either hit or stand if they do not already have a natural blackjack.
    - The player is dealt another card if they call for a hit, then prompted again to hit or stand.
    - The player continues until they hit blackjack, go bust and discard their hand, or choose to stand.
    - The player's points are then recorded if they stand.
  - The dealer's turn then proceeds automatically, hitting if their hand's value is 16 or below, and discarding their hand if they go bust.
  - Prompts for the user to press enter after each hit to allow readability during play.
  - The dealer's points are then recorded once their turn is done.
  - The player's points are then compared to the dealer's and the payout is administered accordingly.
    - If there is a tie, then the player wins no money and is returned their original bet.
    - If the player hit blackjack, they then receive their original bet back plus 1.5 times their bet in winnings.
    - If the player stood on a higher score than the dealer, then their original bet is returned plus 1 times their bet in winnings.
    - Otherwise, the dealer won that round and no money is payed out to the player.
  - The player's money is then checked for the win or loss condition.
    - If the player's money is 0 or below, then the player has lost, and the game ends.
    - If the player's money is above the defined threshold(default $1000), then they have won, and the game ends.
- **ctrl_c_handler** allows the player to exit the game gracefully at any point by pressing "Ctrl + c".
