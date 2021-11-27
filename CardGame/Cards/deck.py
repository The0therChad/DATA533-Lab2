from random import shuffle

from hand import Hand
from card import Card


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
    
    def addToBottom(self, card: Card) -> None:
        self.cards.insert(0, card)
        self.size += 1
    
    # Overwrite parent class's method so card doesn't get added to top of deck
    def addCard(self, card: Card) -> None:
        self.addToBottom(card)


if __name__ == "__main__":
    test = Deck()
    print(test.cards)

    test.shuffle()
    print(test.cards)

    # print(test.drawCard())
    # print(test.cards)
    # print(test.drawCard())
    # print(test.cards)
