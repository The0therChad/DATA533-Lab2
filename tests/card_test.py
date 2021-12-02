import unittest
from CardGame.Cards.card import Card

class CardTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_card_equality(self):
        self.assertEqual(CardTest.card1, CardTest.card3)
        self.assertEqual(CardTest.card2, CardTest.card4)
        self.assertNotEqual(CardTest.card2, CardTest.card1)
        self.assertNotEqual(CardTest.card2, CardTest.card3)
        self.assertNotEqual(CardTest.card4, CardTest.card1)
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.card1 = Card("A", "spades")
        cls.card2 = Card("J", "diamonds")
        cls.card3 = Card("A", "spades")
        cls.card4 = Card("J", "diamonds")
    
    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()