import unittest
from CardGame.Cards.deck import Deck
from CardGame.Cards.card import Card


class DeckTest(unittest.TestCase):
    def setUp(self) -> None:
        self.deck = Deck()
        return super().setUp()

    def test_init(self) -> None:
        self.assertIsInstance(self.deck.cards, list)
        for suit in Card.suits.keys():
            for rank in Card.ranks:
                self.assertIn(Card(rank, suit), self.deck.cards)
        self.assertEqual(self.deck.size, 52)

    def test_shuffle(self) -> None:
        threes = self.deck.search(rank="3")
        self.deck.shuffle()
        self.assertNotEqual(threes, self.deck.search(rank="3"))
        self.assertEqual(self.deck.size, 52)
        self.assertIsInstance(self.deck, Deck)

    def test_drawCard(self) -> None:
        self.assertIsInstance(self.deck.drawCard(), Card)
        self.assertEqual(self.deck.size, 51)
        self.assertEqual(self.deck.drawCard(), Card("Q", "spades"))
        self.assertIsInstance(self.deck, Deck)

    def test_drawCards(self) -> None:
        with self.assertRaises(TypeError):
            self.deck.drawCards("ten")
        with self.assertRaises(ValueError):
            self.deck.drawCards(-1)
        self.assertIsInstance(self.deck.drawCards(3), list)
        self.assertIsInstance(self.deck.drawCards(1)[0], Card)
        self.assertEqual(len(self.deck.drawCards(10)), 10)
        self.assertEqual(self.deck.drawCards(1), [Card("Q", "hearts")])
        self.assertEqual(len(self.deck.drawCards(40)), 37)

    def test_addToBottom(self) -> None:
        with self.assertRaises(TypeError):
            self.deck.addToBottom("ace")
        self.deck.addToBottom(Card("A", "hearts"))
        self.assertEqual(self.deck.size, 53)
        self.assertEqual(len(self.deck.search(suit="hearts", rank="A")), 2)
        self.assertEqual(self.deck.cards[0], Card("A", "hearts"))

    def test_addCard(self) -> None:
        with self.assertRaises(TypeError):
            self.deck.addCard("card")
        self.deck.addCard(Card("A", "hearts"))
        self.assertEqual(self.deck.cards[0], Card("A", "hearts"))

    def tearDown(self) -> None:
        return super().tearDown()
