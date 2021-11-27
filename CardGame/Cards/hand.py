from card import Card


class Hand:
    def __init__(self, cards: list[Card]) -> None:
        if not isinstance(cards, list) and not isinstance(cards, tuple):
            raise TypeError("'cards' must be list or tuple of Card type objects")
        self.cards = cards

    def getTotalPoints(self) -> int:
        return sum([card.getValue() for card in self.cards])

    def discard(self, card: Card):
        return self.cards.remove(card)

    def addCard(self, card: Card):
        return self.cards.append(card)


if __name__ == "__main__":
    card1 = Card("8", "spades")
    card2 = Card("A", "diamonds")
    card3 = Card("J", "clubs")

    hand = Hand([card1, card2])
    print(hand.getTotalPoints())

    hand.addCard(card3)
    print(hand.cards)

    hand.discard(card2)
    print(hand.cards)
