import io
import sys
import unittest
from CardGame.Blackjack.money import Money
from CardGame.Blackjack.person import Player
from CardGame.Cards.card import Card
from CardGame.Cards.hand import Hand


class PlayerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.p1 = Player(hand=Hand([]), money=Money())
        return super().setUp()

    def test_addToHand(self) -> None:
        with self.assertRaises(TypeError):
            self.p1.addToHand(hand=5)
        self.p1.addToHand(Hand([Card("A", "hearts")]))
        self.assertEqual(self.p1.hand.size, 1)
        self.assertIs(type(self.p1.hand), Hand)
        self.p1.addToHand(Hand([Card("7", "hearts"), Card("3", "clubs")]))
        self.assertEqual(self.p1.hand.size, 3)
        self.assertIs(type(self.p1.hand), Hand)

    def test_addCardToHand(self) -> None:
        with self.assertRaises(ValueError):
            self.p1.addCardToHand(card=4)
        self.p1.addCardToHand(Card("A", "hearts"))
        self.assertEqual(self.p1.hand.size, 1)
        self.assertIs(type(self.p1.hand), Hand)
        self.p1.addCardToHand(Card("9", "spades"))
        self.assertEqual(self.p1.hand.size, 2)
        self.assertIs(type(self.p1.hand), Hand)

    def test_getHandPoints(self) -> None:
        self.assertEqual(self.p1.getHandPoints(), 0)
        self.p1.addCardToHand(Card("A", "hearts"))
        self.assertEqual(self.p1.getHandPoints(), 11)
        self.p1.addCardToHand(Card("A", "spades"))
        self.assertEqual(self.p1.getHandPoints(), 12)
        self.p1.addCardToHand(Card("A", "clubs"))
        self.assertEqual(self.p1.getHandPoints(), 13)
        self.p1.addCardToHand(Card("7", "diamonds"))
        self.assertEqual(self.p1.getHandPoints(), 20)

    def test_showMoney(self) -> None:
        self.assertIsInstance(self.p1.showMoney(), str)
        self.assertEqual(self.p1.showMoney(), "You have $100, and need $1000 to win.")
        self.p1.money = Money(200)
        self.assertIsInstance(self.p1.showMoney(), str)
        self.assertEqual(self.p1.showMoney(), "You have $200, and need $1000 to win.")

    def test_discardHand(self) -> None:
        self.assertEqual(self.p1.hand.size, 0)
        self.p1.addToHand(Hand([Card("7", "hearts"), Card("3", "clubs")]))
        self.assertEqual(self.p1.hand.size, 2)
        self.p1.discardHand()
        self.assertEqual(self.p1.hand.size, 0)
        self.assertIs(type(self.p1.hand), Hand)

    def test_displayHand(self) -> None:
        self.assertIsInstance(self.p1.displayHand(), str)

    def test_hit_stand(self) -> None:
        # Test natural blackjack
        self.p1.addToHand(hand=Hand([Card("A", "hearts"), Card("10", "spades")]))
        self.assertFalse(self.p1.hit_stand())

        self.p1.hand = Hand([])
        # Test player input of "hit"
        sys.stdin = io.StringIO("hit")
        self.assertTrue(self.p1.hit_stand())
        # Test player input of "stand"
        sys.stdin = io.StringIO("stand")
        self.assertFalse(self.p1.hit_stand())
        # Test incorrect player input followed by "hit"
        sys.stdin = io.StringIO("42\nhit")
        self.assertTrue(self.p1.hit_stand())
        # Test many incorrect player inputs followed by "hit"
        sys.stdin = io.StringIO("wrong\nwrong\nwrong\nwrong\nhit")
        self.assertTrue(self.p1.hit_stand())

        sys.stdin = sys.__stdin__

    def tearDown(self) -> None:
        return super().tearDown()

    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()
