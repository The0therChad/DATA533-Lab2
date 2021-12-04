import io
import sys
import unittest
from CardGame.Blackjack.person import Dealer
from CardGame.Cards.deck import Deck
from CardGame.Cards.hand import Hand
from CardGame.Cards.card import Card

class DealerTest(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        # Re-initialize the deck at the start of each test (cards are sorted)
        DealerTest.dealer.deck = Deck()
    
    def test_hit(self) -> None:
        dealer = DealerTest.dealer
        # Test points > 21 condition
        dealer.addToHand(dealer.dealHand(3))    # K, Q, J of Spades, 30 points
        self.assertFalse(dealer.hit_stand())

        # Test 17 <= points < 21 condition
        dealer.discardHand()
        dealer.addToHand(dealer.dealHand(2))    # 10, 9 of spades, 19 points
        self.assertFalse(dealer.hit_stand())

        # Test points < 17 condition
        dealer.discardHand()
        dealer.addToHand(dealer.dealHand(2))    # 8, 7 of spades, 15 points
        # When the function returns true, it expects the user to press enter, so
        # we must simulate pressing enter by putting a newline character in a
        # text stream and having STDIN read from that stream
        sys.stdin = io.StringIO("\n")
        self.assertTrue(dealer.hit_stand())
        sys.stdin = sys.__stdin__   # Restore STDIN to keyboard
        

        # Test points = 21 condition
        dealer.discardHand()
        dealer.addToHand(Hand([Card("A", "spades"), Card("K", "diamonds")]))
        self.assertFalse(dealer.hit_stand())

        dealer.discardHand()
        dealer.addToHand(
            Hand([
                Card("9", "clubs"),
                Card("5", "hearts"),
                Card("7", "spades")
            ])
        )
        self.assertFalse(dealer.hit_stand())

    
    def tearDown(self) -> None:
        return super().tearDown()
    
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.dealer = Dealer(deck=Deck())
    
    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()