class Card():
    ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    suits = {
        "clubs": "\u2663", 
        "diamonds": "\u2662", 
        "hearts": "\u2661", 
        "spades": "\u2660"
    }
    colours = {
        "clubs": "Black", 
        "diamonds": "Red", 
        "hearts": "Red", 
        "spades": "Black"
    }

    def __init__(self, rank: str, suit: str) -> None:
        if not isinstance(rank, str) or not isinstance(suit, str):
            raise TypeError("class constructor arguments must be strings")
        if rank not in Card.ranks and rank != "1":
            raise ValueError("Improper rank: select 1-10, or J, Q, K, or A")
        if suit not in Card.suits.keys():
            raise ValueError("Improper suit: select either 'clubs', 'diamonds', 'hearts', or 'spades")
        
        if rank == "1":
            self._rank = "A"
        else:
            self._rank = rank
        self._suit = suit
    
    def __str__(self) -> str: 
        return f"{self._rank}{Card.suits[self._suit]}"
    
    def getColour(self) -> str:
        return Card.colours[self._suit]
    
    def getRank(self) -> str:
        return self._rank
    
    def getSuit(self):
        return self._suit.capitalize()
    
    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Card):
            return False
        return self._rank == __o._rank and self._suit == __o._suit
    
    def __ne__(self, __o: object) -> bool:
        if not isinstance(__o, Card):
            return True
        return not self == __o


if __name__ == "__main__":
    card = Card("1", "spades")
    print(card.getRank(), card.getSuit(), card.getColour())
    print(card)
    card2 = Card("A", "hearts")
    print(card2)
    print(card != card2)
    print(card != card)
    print(card < card2)