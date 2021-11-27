from card import Card

class Hand():
    def __init__(self, cards: list[Card]) -> None:
        if not isinstance(cards, list) or not isinstance(cards, tuple):
            raise TypeError("'cards' must be list or tuple of Card type objects")
        self.cards = cards
    
    def getValue(self) -> int:
        pass

    def discard(self):
        pass

    def addCard(self):
        pass