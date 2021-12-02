from __future__ import annotations

from .card import Card


class Hand:
    def __init__(self, cards: list[Card] = []) -> None:
        error_msg = "'cards' must be list or tuple of Card type objects"
        if not isinstance(cards, list) and not isinstance(cards, tuple):
            raise TypeError(error_msg)
        for card in cards:
            if not isinstance(card, Card):
                raise TypeError(error_msg)
        self.cards = cards
        self.size = len(self.cards)

    def getTotalPoints(self) -> int:
        return sum([card.getValue() for card in self.cards])

    def discardByCard(self, card: Card) -> Card:
        if not isinstance(card, Card):
            raise TypeError("'card' must be type Card")
        self.size -= 1
        index = self.cards.index(card)
        return self.cards.pop(index)

    def discardByIndex(self, index: int) -> Card:
        if not isinstance(index, int):
            raise TypeError("'index' must be type int")
        if index not in range(len(self.cards)):
            raise IndexError("'index' out of list bounds")
        self.size -= 1
        return self.cards.pop(index)

    def discardHand(self) -> None:
        self.cards = []

    def addCard(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("'card' must be type Card")
        self.cards.append(card)
        self.size += 1

    def addCards(self, cards: list[Card]) -> None:
        error_msg = "'cards' must be list or tuple of Card type objects"
        if type(cards) not in (list, tuple):
            raise TypeError(error_msg)
        for card in cards:
            if not isinstance(card, Card):
                raise TypeError(error_msg)
        self.cards.extend(cards)
        self.size += len(cards)

    # This function returns a list of indices representing all cards that match
    # the search parameters. Users can search by suit, rank, or both.
    def search(self, suit: str = None, rank: str = None) -> int:
        NoneType = type(None)
        if type(suit) not in (str, NoneType) or type(rank) not in (str, NoneType):
            raise TypeError("'rank' and 'suit' must be 'str' type or None")
        if suit and suit.lower() not in Card.suits.keys():
            raise ValueError("invalid suit")
        if rank and rank.upper() not in Card.ranks:
            raise ValueError("invalid rank")

        # Empty search, so return all indices
        if suit is None and rank is None:
            return list(range(self.size))

        indices = []
        for i, card in enumerate(self.cards):
            if rank is not None and suit is None:
                if card.getRank().upper() == rank.upper():
                    indices.append(i)
            elif rank is None and suit is not None:
                if card.getSuit().lower() == suit.lower():
                    indices.append(i)
            elif rank is not None and suit is not None:
                if (
                    card.getRank().upper() == rank.upper()
                    and card.getSuit().lower() == suit.lower()
                ):
                    indices.append(i)
        return indices

    def __add__(self, other: Hand) -> Hand:
        if not isinstance(other, Hand):
            raise TypeError("Both operands must be 'Hand' type")
        card_list = list(self.cards)
        card_list.extend(other.cards)
        return Hand(card_list)

    def __str__(self) -> str:
        string = [str(card) for card in self.cards]
        return str(string)
