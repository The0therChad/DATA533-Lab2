# DATA533-Lab2

We are developing a card game package. The first subpackage will define the cards being used. That will include card values, suits, size of hands, and deck. There will be functions to shuffle the deck, draw from the deck, discard from the hand, and compare cards. The second subpackage will define the rules and play for blackjack. The modules will deal hands for the dealer and the player, then prompt the user to stand or hit. There will also be a module to implement betting, with a value set to win the game or lose the game.

## CardGame Package Documentation
### Cards Subpackage
The cards subpackage contains three modules that define playing cards, with classes to make a deck and hands containing cards.

### card Module
The card module defines the "Card" class accepting parameters for the rank of the card and the suit of the card. The class checks to make sure both the rank and the suit are accetable values corresponding to a typical deck of playing cards. A list also initialized to give point values to each rank of card. Specifically, counting face cards as 10, and aces as 11.

- **\_\_str__ / \_\_repr__** defines the string representation of the Card objects to display the proper rank and suit in plaintext.
- **getColour** returns the colour of a card, as a string,  corresponding to its suit.
- **getRank** returns the rank of a card as a string.
- **getSuit** returns the suit of a card as a string.
- **getValue** returns the value of a card, as an integer, based on its rank by pulling the corresponding point value from the list, by index, in the Card class.
- **\_\_eq__ / \_\_ne__** defines method to check whether two cards are the same or not.
- **setPoints** class method that allows you to redefine the point values that correspond to each card rank.

### hand Module
The hand module defines the "Hand" class accepting a single parameter as a list of "Card" objects as defined above.

- **getTotalPoints** returns the sum of the card values in the hand.
