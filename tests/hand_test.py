import unittest
from CardGame.Cards.card import Card
from CardGame.Cards.hand import Hand


class HandTest(unittest.TestCase):
    def setUp(self) -> None:
        self.h1 = Hand([Card("A", "hearts"), Card("10", "spades")])
        return super().setUp()

    def test_init(self) -> None:
        with self.assertRaises(TypeError):
            Hand("hand")
        with self.assertRaises(TypeError):
            Hand(["card"])
        self.assertEqual(self.h1.size, 2)
        self.assertIsInstance(self.h1.cards, list)
        self.assertIs(type(self.h1.cards[0]), Card)

    def test_getTotalPoints(self) -> None:
        self.assertIsInstance(self.h1.getTotalPoints(), int)
        self.assertEqual(self.h1.getTotalPoints(), 21)

    def test_discardByCard(self) -> None:
        with self.assertRaises(TypeError):
            self.h1.discardByCard(10)
        with self.assertRaises(ValueError):
            self.h1.discardByCard(Card("9", "clubs"))
        self.assertIsInstance(self.h1.discardByCard(Card("10", "spades")), Card)
        self.assertIsInstance(self.h1, Hand)
        self.assertEqual(self.h1.size, 1)

    def test_discardByIndex(self) -> None:
        with self.assertRaises(TypeError):
            self.h1.discardByIndex("ace")
        with self.assertRaises(IndexError):
            self.h1.discardByIndex(5)
        self.assertIsInstance(self.h1.discardByIndex(0), Card)
        self.assertIsInstance(self.h1, Hand)
        self.assertEqual(self.h1.size, 1)

    def test_discardHand(self) -> None:
        self.assertEqual(self.h1.size, 2)
        self.h1.discardHand()
        self.assertEqual(self.h1.size, 0)
        self.assertIsInstance(self.h1, Hand)

    def test_addCard(self) -> None:
        with self.assertRaises(TypeError):
            self.h1.addCard("card")
        self.h1.addCard(Card("5", "diamonds"))
        self.assertIn(Card("5", "diamonds"), self.h1.cards)
        self.assertEqual(self.h1.size, 3)

    def test_addCards(self) -> None:
        with self.assertRaises(TypeError):
            self.h1.addCards("cards")
        with self.assertRaises(TypeError):
            self.h1.addCards([Card("3", "clubs"), "card"])
        self.h1.addCards([Card("2", "spades"), Card("4", "hearts")])
        self.assertIn(Card("4", "hearts"), self.h1.cards)
        self.assertEqual(self.h1.size, 4)

    def test_search(self) -> None:
        # Test parameter type enforcement
        with self.assertRaises(TypeError):
            self.h1.search(suit=5, rank=[])
        with self.assertRaises(ValueError):
            self.h1.search(suit="circles")
        with self.assertRaises(ValueError):
            self.h1.search(rank="20")
        # Test empty search
        self.assertIsInstance(self.h1.search(), list)
        self.assertEqual(self.h1.search(), [0, 1])
        # Test search by suit
        self.assertIsInstance(self.h1.search(suit="hearts"), list)
        self.assertEqual(self.h1.search(suit="hearts"), [0])
        self.assertEqual(self.h1.search(suit="clubs"), [])
        # Test search by rank
        self.assertIsInstance(self.h1.search(rank="10"), list)
        self.assertEqual(self.h1.search(rank="10"), [1])
        self.assertEqual(self.h1.search(rank="5"), [])
        # Test search by both suit and rank
        self.assertIsInstance(self.h1.search(suit="hearts", rank="A"), list)
        self.assertEqual(self.h1.search(suit="hearts", rank="A"), [0])
        self.assertEqual(self.h1.search(suit="hearts", rank="10"), [])
        self.assertEqual(self.h1.search(suit="spades", rank="A"), [])

    def test_add(self) -> None:
        with self.assertRaises(TypeError):
            self.h1 + "hand"
        new_hand = self.h1 + self.h1
        self.assertIsInstance(new_hand, Hand)
        self.assertIsInstance(self.h1.cards, list)
        self.assertEqual(new_hand.size, 4)

    def test_str(self) -> None:
        self.assertIsInstance(str(self.h1), str)

    def tearDown(self) -> None:
        return super().tearDown()
