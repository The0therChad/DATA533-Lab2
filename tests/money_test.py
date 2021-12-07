import io
import sys
import unittest
from CardGame.Blackjack.money import Money

class MoneyTest(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.money = Money(200)
    
    def test_constructor(self) -> None:
        with self.assertRaises(TypeError):
            Money("100")
        with self.assertRaises(TypeError):
            Money(100.0)
        with self.assertRaises(ValueError):
            Money(0)
        with self.assertRaises(ValueError):
            Money(-100)
        self.assertEqual(self.money.value, 200)
    
    def test_bet(self) -> None:
        # The bet() method prompts the user for input, so we must simulate user
        # input by writing to a text stream and having STDIN read from it
        test_input = io.BytesIO(b"100\n")
        sys.stdin = test_input

        # Test betting half of total money
        money = self.money
        self.assertEqual(money.bet(), 100)  

        # Test betting ALL of current money
        money = Money(200)
        input_text = b"200\n"
        test_input.write(input_text)
        test_input.seek(-len(input_text), io.SEEK_CUR)
        self.assertEqual(money.bet(), 200)

        # Test giving bad input
        money = Money(100)
        input_text = b"a\ndkjfhe\n50\n"
        test_input.write(input_text)
        test_input.seek(-len(input_text), io.SEEK_CUR)
        self.assertEqual(money.bet(), 50)

        # Test giving an amount greater than the current amount held
        money = Money(100)
        input_text = b"9999\n101\n76\n"
        test_input.write(input_text)
        test_input.seek(-len(input_text), io.SEEK_CUR)
        self.assertEqual(money.bet(), 76)

        # Test giving a negative or zero ammount
        money = Money(100)
        input_text = b"-9000\n-530\n0\n36\n"
        test_input.write(input_text)
        test_input.seek(-len(input_text), io.SEEK_CUR)
        self.assertEqual(money.bet(), 36)

        # Restore STDIN back to Keyboard
        test_input.close()
        sys.stdin = sys.__stdin__
    
    def test_payout(self) -> None:
        with self.assertRaises(TypeError):
            self.money.payout(20.5, 1)
        with self.assertRaises(TypeError):
            self.money.payout(50, "2.0")
        self.money.payout(50, 1.5)
        self.assertEqual(self.money.value, 275)
        self.money.payout(25, 1)
        self.assertEqual(self.money.value, 300)
        self.money.payout(100, -1.0)
        self.assertEqual(self.money.value, 200)
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()
    
    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()