from random import shuffle

from .hand import Hand
from .card import Card


class Deck(Hand):
    def __init__(self) -> None:
        ranks = Card.ranks
        suits = Card.suits.keys()
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
        self.size = len(self.cards)

    def shuffle(self) -> None:
        shuffle(self.cards)

    def drawCard(self) -> Card:
        self.size -= 1
        return self.cards.pop()
    
    def drawCards(self, num: int = 1) -> list[Card]:
        if not isinstance(num, int):
            raise TypeError("'num' must be an integer")
        if num < 1:
            raise ValueError("'num' must be a positive integer")
        
        return [self.drawCard() for i in range(min(num, self.size))]
    
    def addToBottom(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("'card' must be object of type Card")
        self.cards.insert(0, card)
        self.size += 1
    
    # Overwrite parent class's method so card doesn't get added to top of deck
    def addCard(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("'card' must be object of type Card")
        self.addToBottom(card)
