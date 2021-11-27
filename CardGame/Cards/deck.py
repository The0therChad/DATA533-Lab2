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