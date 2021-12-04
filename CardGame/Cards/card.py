class Card:
    """Class to implement playing cards"""

    ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    suits = {
        "clubs": "\u2663",
        "diamonds": "\u2662",
        "hearts": "\u2661",
        "spades": "\u2660",
    }
    colours = {"clubs": "Black", "diamonds": "Red", "hearts": "Red", "spades": "Black"}
    points = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)

    def __init__(self, rank: str, suit: str) -> None:
        if not isinstance(rank, str) or not isinstance(suit, str):
            raise TypeError("class constructor arguments must be strings")
        rank = rank.upper()
        suit = suit.lower()
        if rank not in Card.ranks and rank != "1":
            raise ValueError("Improper rank: select 1-10, or J, Q, K, or A")
        if suit not in Card.suits.keys():
            raise ValueError(
                "Improper suit: select either 'clubs', 'diamonds', 'hearts', or 'spades"
            )

        if rank == "1":
            self._rank = "A"
        else:
            self._rank = rank
        self._suit = suit

    def __str__(self) -> str:
        return f"{self._rank}{Card.suits[self._suit]}"

    def __repr__(self) -> str:
        return f"{self._rank}{Card.suits[self._suit]}"

    def getColour(self) -> str:
        return Card.colours[self._suit]

    def getRank(self) -> str:
        return self._rank

    def getSuit(self) -> str:
        return self._suit.capitalize()

    def getValue(self) -> int:
        if Card.points is not None:
            return Card.points[Card.ranks.index(self._rank)]

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Card):
            return False
        return self._rank == __o._rank and self._suit == __o._suit

    def __ne__(self, __o: object) -> bool:
        if not isinstance(__o, Card):
            return True
        return not self == __o

    @classmethod
    def setPoints(cls, points: tuple[int] or None) -> None:
        if points is None:
            cls.points = points
            return

        error_msg = "'points' must be either a list or tuple of 13 ints or None"
        if type(points) not in (list, tuple) or len(points) != 13:
            raise TypeError(error_msg)
        # Now check that points contains ints and ONLY ints
        for value in points:
            if not isinstance(value, int):
                raise TypeError(error_msg)
        cls.points = tuple(points)
