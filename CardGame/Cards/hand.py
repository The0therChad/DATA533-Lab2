from card import Card

class Hand():
    def __init__(self, cards: list[Card]) -> None:
        if not isinstance(cards, list) and not isinstance(cards, tuple):
            raise TypeError("'cards' must be list or tuple of Card type objects")
        self.cards = cards
    
    def getTotalPoints(self) -> int:
        return sum([card.getValue() for card in self.cards])

    def discard(self):
        pass

    def addCard(self):
        pass


if __name__ == "__main__":
    card1 = Card("8", "spades")
    card2 = Card("A", "diamonds")
    card3 = Card("J", "clubs")

    hand = Hand([card1, card2, card3])
    print(hand.getTotalPoints())