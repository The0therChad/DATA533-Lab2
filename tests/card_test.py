import unittest
from CardGame.Cards.card import Card

class CardTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_equality(self) -> None:
        self.assertEqual(CardTest.card1, CardTest.card3)
        self.assertEqual(CardTest.card2, CardTest.card4)
        self.assertNotEqual(CardTest.card2, CardTest.card1)
        self.assertNotEqual(CardTest.card2, CardTest.card3)
        self.assertNotEqual(CardTest.card4, CardTest.card1)
    
    def test_points(self) -> None:
        self.assertEqual(CardTest.card1.getValue(), 11)
        self.assertEqual(CardTest.card2.getValue(), 10)
        self.assertEqual(CardTest.card5.getValue(), 2)
        self.assertEqual(CardTest.card6.getValue(), 4)
        self.assertEqual(CardTest.card7.getValue(), 7)
    
    def test_constructor(self) -> None:
        with self.assertRaises(TypeError):
            Card(7, "spades")
        with self.assertRaises(ValueError):
            Card("d", "hearts")
        with self.assertRaises(ValueError):
            Card("A", "not-a-real-suit")
        self.assertEqual(Card("1", "clubs").getRank(), "A")
        self.assertEqual(Card("7", "SPAdeS").getSuit(), "Spades")
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.card1 = Card("A", "spades")
        cls.card2 = Card("J", "diamonds")
        cls.card3 = Card("A", "spades")
        cls.card4 = Card("J", "diamonds")

        cls.card5 = Card("2", "hearts")
        cls.card6 = Card("4", "clubs")
        cls.card7 = Card("7", "diamonds")
    
    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()
        cards = (cls.card1, cls.card2, cls.card3, cls.card4, cls.card5, 
                 cls.card6, cls.card7)
        for card in cards:
            del card