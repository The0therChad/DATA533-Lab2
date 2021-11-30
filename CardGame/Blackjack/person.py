from ..Cards.card import Card
from ..Cards.deck import Deck
from ..Cards.hand import Hand
from .money import Money

class Player():
    def __init__(self, hand: Hand = None, money: Money = None) -> None:
        self.hand = hand
        self.money = money
    
    def getHandPoints(self) -> int:
        score = self.hand.getTotalPoints()
        ace_count = len(self.hand.search(rank="A"))
        if ace_count > 1:
            score -= ((ace_count - 1) * 10)
        return score
    
    def addToHand(self, hand: Hand) -> None:
        if not isinstance(hand, Hand):
            raise TypeError("'hand' must be type Hand")
        if self.hand is None:
            self.hand = hand
        else:
            self.hand += hand

class Dealer(Player):
    def __init__(self, deck: Deck, hand: Hand = None, money: Money = None) -> None:
        super().__init__(hand=hand, money=money)
        self.deck = deck
    
    def dealCard(self) -> Card:
        return self.deck.drawCard()

    def dealHand(self, num_cards: int) -> Hand:
        if not isinstance(num_cards, int):
            raise TypeError("'num_cards' must be an integer")
        if num_cards < 1:
            raise ValueError("'num_cards' must be a positive value")
        
        if num_cards == 1:
            return self.dealCard()
        else:
            return Hand(self.deck.drawCards(min(num_cards, self.deck.size)))