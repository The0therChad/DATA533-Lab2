from card import Card


class Hand():
    def __init__(self, cards: list[Card]) -> None:
        if not isinstance(cards, list) and not isinstance(cards, tuple):
            raise TypeError("'cards' must be list or tuple of Card type objects")
        self.cards = cards
        self.size = len(self.cards)

    def getTotalPoints(self) -> int:
        return sum([card.getValue() for card in self.cards])

    def discardByCard(self, card: Card) -> Card:
        self.size -= 1
        index = self.cards.index(card)
        return self.cards.pop(index)
    
    def discardByIndex(self, index: int) -> Card:
        self.size -= 1
        return self.cards.pop(index)

    def addCard(self, card: Card) -> None:
        self.cards.append(card)
        self.size += 1

    def __str__(self) -> str:
        string = [str(card) for card in self.cards]
        value_string = "\tTotal Value: %d" % self.getTotalPoints()
        return str(string) + value_string


if __name__ == "__main__":
    card1 = Card("8", "spades")
    card2 = Card("A", "diamonds")
    card3 = Card("J", "clubs")

    hand = Hand([card1, card2])
    print(hand.getTotalPoints())

    hand.addCard(card3)
    print(hand, hand.size)

    # removed = hand.discardByCard(card2)
    removed = hand.discardByIndex(0)
    # print(hand.cards)
    print(hand, hand.size)
    print(removed)
