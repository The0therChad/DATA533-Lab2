from ..Cards.card import Card
from ..Cards.deck import Deck
from ..Cards.hand import Hand
from .money import Money

class Person():
    def __init__(self, hand: Hand = None, money: Money = None) -> None:
        self.hand = hand
        self.money = money
    
    def getHandPoints(self) -> int:
        score = self.hand.getTotalPoints()
        ace_count = len(self.hand.search(rank="A"))
        if ace_count > 1:
            score -= ((ace_count - 1) * 10)
        return score
