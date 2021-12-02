import unittest
from CardGame.Cards.card import Card

class CardTest(unittest.TestCase):
    def test_card(self):
        card = Card("A", "spades")
        self.assertEqual(card.getValue(), 11)