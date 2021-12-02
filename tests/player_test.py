import unittest
from CardGame.Blackjack.person import Player
from CardGame.Cards.deck import Deck


class PlayerTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    @classmethod
    def setUpClass(cls) -> None:
        cls.p1 = Player()
        cls.deck = Deck()
        cls.deck.shuffle()
        return super().setUpClass()
